from PySide6.QtCore import QThread, Signal
import numpy as np
import time
import rtde_control
import rtde_receive
from pypylon import pylon
import cv2
from global_data import GlobalData
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities
from utils.robotiq_gripper_control import RobotiqGripper
from ur_robot_calib_params import read_calib_data

class Test_Thread_1(QThread):
    """Thread for test 1. Basic test, pick and place with aruco markers."""

    finished_signal = Signal()  # Signal emitted when test is completed
    stop_signal = Signal()  # Signal for stopping the test

    def __init__(self, global_data: GlobalData):
        super(Test_Thread_1, self).__init__()
        self.global_data = global_data
        self.logger = self.global_data.logger
        self.is_running = True

    def run(self):
        """Main test process."""
        try:
            # Initialize robot interface
            self.rtde_r = rtde_receive.RTDEReceiveInterface(self.global_data.ip_address)
            
            # Need to have robot parameters
            urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
            calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'
            a, d, alpha = read_calib_data.load_dh_parameters_from_urcontrol(urcontrol_file)
            delta_theta, delta_a, delta_d, delta_alpha = read_calib_data.load_mounting_calibration_parameters(calibration_file)

            # turning on the light
            if self.global_data.light_test:
                if not utilities.enable_digital_output(self.global_data.ip_address, self.global_data.light_output_id):
                    raise RuntimeError("Failed to turn on light.")
                
            first_TCP = self.rtde_r.getActualTCPPose()
            first_TCP_tf = utilities.pose_vector_to_tf_matrix(first_TCP)
            first_joints = np.array(self.rtde_r.getActualQ())
            first_robot_tf = utilities.fk_with_corrections(first_joints, a, d, alpha, delta_theta, delta_a, delta_d, delta_alpha)
            self.rtde_r.disconnect()

            self.rtde_c = rtde_control.RTDEControlInterface(self.global_data.ip_address)
            gripper = RobotiqGripper(self.rtde_c)

            # Initialize camera
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.camera.Open()

            # Load user-defined camera settings (configured via Pylon Viewer)
            self.camera.UserSetSelector.SetValue("UserSet1")
            self.camera.UserSetLoad.Execute()
            
            # Capture an image using the camera
            grab_result = self.camera.GrabOne(2000)  # Timeout 2 second
            if grab_result.GrabSucceeded():
                self.logger.info("Image captured successfully")
                image = grab_result.Array
                image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
            else:
                self.logger.warning("Failed to capture image.")
                raise TimeoutError("Failed to capture image.")
            
            # detection of things in the image
            ids, corners, tvecs, rvecs, transf_matrices = utilities.EstimateMarkerPositionFromImage(image,
                                                                                                   self.global_data.camera_matrix, 
                                                                                                   self.global_data.dist_coeffs, 
                                                                                                   0.022, 
                                                                                                   dictionary_name=cv2.aruco.DICT_4X4_250)

            if ids is None or len(ids) == 0:
                self.logger.warning("Žádné markery nebyly detekovány.")
                self.cleanup()
                return
            
            # Marker mapping: ID → transformation matrix
            marker_dict = {int(id_): tf for id_, tf in zip(ids.flatten(), transf_matrices)}   
            
            if not self.is_running:
                self.logger.warning("Test stopped by user.")
                self.cleanup()
                return  # Exit thread safely
            
            # Generating points by configuration
            if self.global_data.calib_config_test == 0:
                # Eye-in-Hand
                self.logger.info("Calibration test Eye-in-Hand process started.")

                gripper.activate()
                gripper.set_speed(15)
                gripper.open()

                for i in range(5):
                    pick_id = i
                    place_id = i + 10

                    if not self.is_running:
                        self.logger.warning("Test stopped by user.")
                        self.cleanup()
                        return  # Exit thread safely

                    self.rtde_c.moveL(first_TCP, speed=0.1, acceleration=0.15)

                    if pick_id in marker_dict and place_id in marker_dict:
                        tf_pick_camera = marker_dict[pick_id]
                        tf_place_camera = marker_dict[place_id]

                        # === PICK part ===
                        pick_list = utilities.generate_pick_poses_z_down(tf_pick_camera)
                        pick_list_global = [first_robot_tf @ self.global_data.X_matrix @ p for p in pick_list]

                        best_pick_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pick_list_global)
                        best_pick = utilities.tf_matrix_to_pose_vector(best_pick_tf)

                        if not self.is_running:
                            self.logger.warning("Test stopped by user.")
                            self.cleanup()
                            return  # Exit thread safely

                        # Offset in the direction of the local Z axis of the object by -5 cm (in its coordinate system)
                        offset_above = np.eye(4)
                        offset_above[:3, 3] = np.array([0, 0, -0.05])  # shift of 5 cm in local Z axis
                        pick_tf_above = best_pick_tf @ offset_above
                        pick_pose_above = utilities.tf_matrix_to_pose_vector(pick_tf_above)

                        # Pick sequence
                        self.logger.info(f"Picking marker {pick_id} from {best_pick}")
                        self.rtde_c.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
                        self.rtde_c.moveL(best_pick, speed=0.1, acceleration=0.15)

                        # Close gripper
                        gripper.close()

                        self.rtde_c.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

                        # === PLACE part ===
                        place_list = utilities.generate_pick_poses_z_down(tf_place_camera)
                        place_list_global = [first_robot_tf @ self.global_data.X_matrix @ p for p in place_list]

                        best_place_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, place_list_global)
                        
                        # according to the height of the cube + 10%
                        offset_place = np.eye(4)
                        offset_place[:3, 3] = np.array([0, 0, -0.033])
                        best_place_tf = best_place_tf @ offset_place
                        place_tf_above = best_place_tf @ offset_above

                        best_place = utilities.tf_matrix_to_pose_vector(best_place_tf)
                        place_pose_above = utilities.tf_matrix_to_pose_vector(place_tf_above)

                        self.logger.info(f"Placing marker {pick_id} to marker {place_id} at {best_place}")
                        self.rtde_c.moveL(place_pose_above, speed=0.1, acceleration=0.15)
                        self.rtde_c.moveL(best_place, speed=0.1, acceleration=0.15)

                        # Open gripper
                        gripper.open()

                        self.rtde_c.moveL(place_pose_above, speed=0.2, acceleration=0.3)

                    else:
                        self.logger.warning(f"Marker {pick_id} or {place_id} was not detected - skipped.")

            else:
                # Eye-to-Hand
                self.logger.info("Calibration test Eye-to-Hand process started.")

                gripper.activate()
                gripper.set_speed(15)
                gripper.open()

                for i in range(5):
                    pick_id = i
                    place_id = i + 10

                    self.rtde_c.moveL(first_TCP, speed=0.1, acceleration=0.15)

                    if not self.is_running:
                        self.logger.warning("Test stopped by user.")
                        self.cleanup()
                        return  # Exit thread safely

                    if pick_id in marker_dict and place_id in marker_dict:
                        tf_pick_camera = marker_dict[pick_id]
                        tf_place_camera = marker_dict[place_id]

                        # === PICK part ===
                        pick_list = utilities.generate_pick_poses_z_down(tf_pick_camera)
                        pick_list_global = [self.global_data.X_matrix @ p for p in pick_list]

                        best_pick_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pick_list_global)
                        best_pick = utilities.tf_matrix_to_pose_vector(best_pick_tf)

                        if not self.is_running:
                            self.logger.warning("Test stopped by user.")
                            self.cleanup()
                            return  # Exit thread safely

                        # Offset in the direction of the local Z axis of the object by -5 cm (in its coordinate system)
                        offset_above = np.eye(4)
                        offset_above[:3, 3] = np.array([0, 0, -0.05])  # shift of 5 cm in local Z axis
                        pick_tf_above = best_pick_tf @ offset_above
                        pick_pose_above = utilities.tf_matrix_to_pose_vector(pick_tf_above)

                        # Pick sequence
                        self.logger.info(f"Picking marker {pick_id} from {best_pick}")
                        self.rtde_c.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
                        self.rtde_c.moveL(best_pick, speed=0.1, acceleration=0.15)

                        # Close gripper
                        gripper.close()

                        self.rtde_c.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

                        # === PLACE part ===
                        place_list = utilities.generate_pick_poses_z_down(tf_place_camera)
                        place_list_global = [self.global_data.X_matrix @ p for p in place_list]

                        best_place_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, place_list_global)
                        
                        # according to the height of the cube + 10%
                        offset_place = np.eye(4)
                        offset_place[:3, 3] = np.array([0, 0, -0.033])
                        best_place_tf = best_place_tf @ offset_place

                        place_tf_above = best_place_tf @ offset_above

                        best_place = utilities.tf_matrix_to_pose_vector(best_place_tf)
                        place_pose_above = utilities.tf_matrix_to_pose_vector(place_tf_above)

                        self.logger.info(f"Placing marker {pick_id} to marker {place_id} at {best_place}")
                        self.rtde_c.moveL(place_pose_above, speed=0.1, acceleration=0.15)
                        self.rtde_c.moveL(best_place, speed=0.1, acceleration=0.15)

                        # Open gripper
                        gripper.open()

                        self.rtde_c.moveL(place_pose_above, speed=0.2, acceleration=0.3)

                    else:
                        self.logger.warning(f"Marker {pick_id} or {place_id} was not detected - skipped.")

            self.rtde_c.moveL(first_TCP, speed=0.1, acceleration=0.15)
            self.rtde_c.disconnect()
            
            
            if not self.is_running:
                self.logger.warning("Test stopped by user.")
                self.cleanup()
                return  # Exit thread safely
            
            # turning off the light
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

        
