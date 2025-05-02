from PySide6.QtCore import QThread, Signal
import numpy as np
import time
import rtde_control
import rtde_receive
from pypylon import pylon
import cv2
from typing import Tuple
from global_data import GlobalData
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities, utilities_camera
from utils.robotiq_gripper_control import RobotiqGripper
from ur_robot_calib_params import read_calib_data

# test pomocí hrotu - nutno vyzkoušet

class Test_Thread_3(QThread):
    """Thread for test 3. Test  s kalibračním hrotem."""

    finished_signal = Signal()  # Signal emitted when test is completed
    stop_signal = Signal()  # Signal for stopping the test

    def __init__(self, global_data: GlobalData):
        super(Test_Thread_3, self).__init__()
        self.global_data = global_data
        self.logger = self.global_data.logger
        self.is_running = True

    def run(self):
        """Main test process."""
        try:
            # Initialize robot interface
            self.rtde_r = rtde_receive.RTDEReceiveInterface(self.global_data.ip_address)
            
            # Potřeba mít parametry robota
            urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
            calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'
            a, d, alpha = read_calib_data.load_dh_parameters_from_urcontrol(urcontrol_file)
            delta_theta, delta_a, delta_d, delta_alpha = read_calib_data.load_mounting_calibration_parameters(calibration_file)

            # zapnutí světla
            if self.global_data.light_test:
                if not utilities.enable_digital_output(self.global_data.ip_address, self.global_data.light_output_id):
                    raise RuntimeError("Failed to turn on light.")
                
            first_TCP = self.rtde_r.getActualTCPPose()
            first_TCP_tf = utilities.pose_vector_to_tf_matrix(first_TCP)

            first_joints = np.array(self.rtde_r.getActualQ())
            first_robot_tf = utilities.fk_with_corrections(first_joints, a, d, alpha, delta_theta, delta_a, delta_d, delta_alpha)
            self.rtde_r.disconnect()

            self.rtde_c = rtde_control.RTDEControlInterface(self.global_data.ip_address)

            # Initialize camera
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.camera.Open()

            # Load user-defined camera settings (configured via Pylon Viewer)
            self.camera.UserSetSelector.SetValue("UserSet1")
            self.camera.UserSetLoad.Execute()
            
            # Snímek
            # Capture an image using the camera
            grab_result = self.camera.GrabOne(2000)  # Timeout 2 second
            if grab_result.GrabSucceeded():
                self.logger.info("Image captured successfully")
                image = grab_result.Array
                image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
            else:
                self.logger.warning("Failed to capture image.")
                raise TimeoutError("Failed to capture image.")
            
            # ChArUco calibration parameters
            self.square_length: float = 0.03
            self.marker_length: float = 0.022
            self.board_rows: int = 6
            self.board_cols: int = 8
            self.board_size: Tuple[int, int] = (self.board_cols, self.board_rows)
            self.board_width: float = self.board_cols * self.square_length
            self.board_height: float = self.board_rows * self.square_length
            self.aruco_dict: cv2.aruco.Dictionary = cv2.aruco.getPredefinedDictionary(
                cv2.aruco.DICT_4X4_250
            )
            self.charuco_board: cv2.aruco.CharucoBoard = cv2.aruco.CharucoBoard(
                self.board_size,
                self.square_length,
                self.marker_length,
                self.aruco_dict
            )
            self.charuco_board.setLegacyPattern(True)
            self.charuco_detector: cv2.aruco.CharucoDetector = cv2.aruco.CharucoDetector(
                self.charuco_board)
            # Detect ChArUco corners and IDs
            charuco_corners, charuco_ids, _, _ = self.charuco_detector.detectBoard(image)

            if charuco_ids is None or len(charuco_ids) == 0:
                self.logger.warning("Žádná detection board nebyla detekována.")
                self.cleanup()
                return

            # pro samostatné zjištění polohy desky - LEVÝ HORNÍ ROH
            tvec = np.zeros((3,1))
            rvec = np.zeros((3,1))
            retval, rvec, tvec = cv2.aruco.estimatePoseCharucoBoard(charuco_corners, 
                                                                    charuco_ids, 
                                                                    self.charuco_board, 
                                                                    self.global_data.camera_matrix, 
                                                                    self.global_data.dist_coeffs, 
                                                                    rvec, tvec, useExtrinsicGuess=False)
            
            if retval == False:
                self.logger.warning("Žádná pozice detection board nebyla vypočtena.")
                self.cleanup()
                return
            
            # Create pose vector and convert it to a transformation matrix
            pose_vector = np.hstack((tvec.flatten(), rvec.flatten()))
            pose_tf = utilities.pose_vector_to_tf_matrix(pose_vector)

            if not self.is_running:
                self.logger.warning("Test stopped by user.")
                self.cleanup()
                return  # Exit thread safely

            # Generování bodů podle konfigurace
            if self.global_data.calib_config_test == 0:
                # Eye-in-Hand
                self.logger.info("Calibration test 3 Eye-in-Hand process started.")

                self.rtde_c.moveL(first_TCP, speed=0.1, acceleration=0.15)

                # není nutné řešit natočení...
                tf_matrix_list = utilities.generate_pick_poses(pose_tf)
                pose_list_global = []
                for i in tf_matrix_list:
                    pose_list_global.append(first_robot_tf @ self.global_data.X_matrix @ i)

                best_pose_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pose_list_global)

                # Offset ve směru lokální osy Z objektu o -1 cm (v jeho souřadném systému)
                offset_above = np.eye(4)
                offset_above[:3, 3] = np.array([0, 0, -0.01])  # posun o 5 cm v lokální Z ose  
                best_pose_tf = best_pose_tf @ offset_above
                best_pose = utilities.tf_matrix_to_pose_vector(best_pose_tf)

                self.rtde_c.moveL(best_pose, speed=0.1, acceleration=0.15)
                self.logger.info(f"Pointing to board (levý horní roh)")  
                time.sleep(2)

            else:
                # Eye-to-Hand
                self.logger.info("Calibration test 3 Eye-to-Hand process started.")

                self.rtde_c.moveL(first_TCP, speed=0.1, acceleration=0.15)

                # není nutné řešit natočení...
                tf_matrix_list = utilities.generate_pick_poses(pose_tf)
                pose_list_global = []
                for i in tf_matrix_list:
                    pose_list_global.append(self.global_data.X_matrix @ i)

                best_pose_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pose_list_global)

                # Offset ve směru lokální osy Z objektu o -1 cm (v jeho souřadném systému)
                offset_above = np.eye(4)
                offset_above[:3, 3] = np.array([0, 0, -0.01])
                best_pose_tf = best_pose_tf @ offset_above
                best_pose = utilities.tf_matrix_to_pose_vector(best_pose_tf)

                self.rtde_c.moveL(best_pose, speed=0.1, acceleration=0.15)
                self.logger.info(f"Pointing to board (levý horní roh)")  
                time.sleep(2)

            self.rtde_c.moveL(first_TCP, speed=0.1, acceleration=0.15)
            self.rtde_c.disconnect()
            
            if not self.is_running:
                self.logger.warning("Test stopped by user.")
                self.cleanup()
                return  # Exit thread safely
            
            # vypnutí světla
            utilities.disable_digital_output(self.global_data.ip_address, self.global_data.light_output_id)

            # Finalize calibration
            self.finished_signal.emit()

        except Exception as e:
            error_msg = f"Test error: {str(e)}"
            self.logger.critical(error_msg, exc_info=True)
            self.stop()

        finally:
            self.cleanup()
            
    def stop(self):
        """Stops test safely."""
        self.logger.info("Stopping test process...")
        self.is_running = False  # Stops any loops inside run()
        
        if self.isRunning():  # Ensures the thread is running before waiting
            self.quit()  # Asks the thread to exit safely
            self.wait()  # Waits until the thread fully exits

        self.stop_signal.emit()  # Notifies that the process has stopped

    def cleanup(self):
        """Releases resources at the end of test."""
        self.logger.info("Cleaning up test resources...")
        try:
            if hasattr(self, "camera") and self.camera:
                self.camera.Close()
                del self.camera  # Release object
                self.camera = None
                self.logger.info("Camera closed.")
        except Exception as e:
            self.logger.error(f"Cleanup error: {str(e)}", exc_info=True)

        
