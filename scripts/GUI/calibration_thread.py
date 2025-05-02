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
from utils import utilities, utilities_camera
from ur_robot_calib_params import read_calib_data

class CalibrationThread(QThread):
    """Thread for handling the calibration process."""

    progress_signal = Signal(int, str)  # Sends (percentage, message)
    finished_signal = Signal()  # Signal emitted when calibration is completed
    stop_signal = Signal()  # Signal for stopping the calibration

    def __init__(self, global_data: GlobalData):
        super(CalibrationThread, self).__init__()
        self.global_data = global_data
        self.logger = self.global_data.logger
        self.is_running = True

    def run(self):
        """Main calibration process."""
        try:
            # Generování bodů podle konfigurace
            if self.global_data.calib_config == 0:
                # Eye-in-Hand
                self.logger.info("Calibration Eye-in-Hand process started.")

                # Generate calibration points
                self.img_width, self.img_height = self.global_data.image_shape
                source_axis = np.array([0, 0, 1]) # osa robota zarovnaná s osou kamery
                circle_points = utilities.generate_points_on_circle(8, 0.15, self.global_data.distance, source_axis)
                plane_positions = utilities.generate_plane_points(
                    self.img_width, self.img_height,
                    self.global_data.board_width, self.global_data.board_height,
                    self.global_data.rect_width, self.global_data.rect_height,
                    self.global_data.x_rect, self.global_data.y_rect,
                    source_axis
                    )
                # Combine lists: origin point + valid camera positions + circular points
                self.points = [[0, 0, 0, 0, 0, 0]] + plane_positions + circle_points

            else:
                # Eye-to-Hand
                self.logger.info("Calibration Eye-to-Hand process started.")

                # Generate calibration points
                self.img_width, self.img_height = self.global_data.image_shape
                source_axis = np.array([1, 0, 0]) # osa robota (gripperu) kolmá na podložku směřující na kameru
                circle_points = utilities.generate_points_on_circle(8, 0.1, self.global_data.distance, source_axis)
                plane_positions = utilities.generate_plane_points(
                    self.img_width, self.img_height,
                    self.global_data.board_width, self.global_data.board_height,
                    self.global_data.rect_width, self.global_data.rect_height,
                    self.global_data.x_rect, self.global_data.y_rect,
                    source_axis
                    )
                # Combine lists: origin point + valid camera positions + circular points
                self.points = [[0, 0, 0, 0, 0, 0]] + plane_positions + circle_points

            # zapnutí světla
            if self.global_data.light:
                if not utilities.enable_digital_output(self.global_data.ip_address, self.global_data.light_output_id):
                    raise RuntimeError("Failed to turn on light.")
            
            self.rtde_r = rtde_receive.RTDEReceiveInterface(self.global_data.ip_address)
            first_TCP = self.rtde_r.getActualTCPPose()
            first_tf = utilities.pose_vector_to_tf_matrix(first_TCP)
            self.rtde_r.disconnect()

            # Initialize camera
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.camera.Open()

            # Load user-defined camera settings (configured via Pylon Viewer)
            self.camera.UserSetSelector.SetValue("UserSet1")
            self.camera.UserSetLoad.Execute()

            total_points = len(self.points)

            # Potřeba mít parametry robota
            urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
            calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'
            a, d, alpha = read_calib_data.load_dh_parameters_from_urcontrol(urcontrol_file)
            delta_theta, delta_a, delta_d, delta_alpha = read_calib_data.load_mounting_calibration_parameters(calibration_file)

            for i, point in enumerate(self.points):

                if not self.is_running:
                    self.logger.warning("Calibration stopped by user.")
                    self.cleanup()
                    return  # Exit thread safely

                point_tf = utilities.pose_vector_to_tf_matrix(point)
                point_base_tf = first_tf @ point_tf
                point_base = utilities.tf_matrix_to_pose_vector(point_base_tf)

                self.rtde_c = rtde_control.RTDEControlInterface(self.global_data.ip_address)
                # Pohyb na danou pozici (Lineární pohyb)
                self.rtde_c.moveL(point_base, speed=0.25, acceleration=0.25)
                time.sleep(1) # Pro stabilizaci robota
                self.rtde_c.disconnect()
                # Capture an image using the camera
                grab_result = self.camera.GrabOne(2000)  # Timeout 2 second
                if grab_result.GrabSucceeded():
                    self.logger.info("Image captured successfully")
                    image = grab_result.Array
                    image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
                else:
                    self.logger.warning("Failed to capture image.")
                    raise TimeoutError("Failed to capture image.")

                path = utilities_camera.save_current_frame(self.global_data.image_folder,image)
                self.logger.info("Image saved to: %s", path)

                self.rtde_r = rtde_receive.RTDEReceiveInterface(self.global_data.ip_address)
                actual_TCP = self.rtde_r.getActualTCPPose()
                actual_joints = np.array(self.rtde_r.getActualQ())
                self.rtde_r.disconnect()
                tf_matrix = utilities.pose_vector_to_tf_matrix(actual_TCP)
                utilities.save_pose_data(self.global_data.TCP_pose_folder, tf_matrix)
                utilities.save_joints_data(self.global_data.joints_pose_folder, actual_joints)
                robot_pose_tf = utilities.fk_with_corrections(actual_joints, a, d, alpha, delta_theta, delta_a, delta_d, delta_alpha)
                utilities.save_pose_data(self.global_data.robot_pose_folder, robot_pose_tf)

                # Update progress bar
                progress_percent = int((i + 1) / total_points * 80)
                self.progress_signal.emit(progress_percent, f"Captured point {i+1}/{total_points}")

            self.rtde_c = rtde_control.RTDEControlInterface(self.global_data.ip_address)
            self.rtde_c.moveL(first_TCP, speed=0.25, acceleration=0.25)
            self.rtde_c.disconnect()

            if not self.is_running:
                self.logger.warning("Calibration stopped by user.")
                self.cleanup()
                return  # Exit thread safely
            
            # vypnutí světla
            utilities.disable_digital_output(self.global_data.ip_address, self.global_data.light_output_id)

            # Finalize calibration
            self.calculate_calibration()
            self.progress_signal.emit(100, "Calibration completed.")
            self.finished_signal.emit()

        except Exception as e:
            error_msg = f"Calibration error: {str(e)}"
            self.logger.critical(error_msg, exc_info=True)
            self.progress_signal.emit(0, error_msg)

        finally:
            self.cleanup()
            
    def stop(self):
        """Stops calibration safely."""
        self.logger.info("Stopping calibration process...")
        self.is_running = False  # Stops any loops inside run()
        
        if self.isRunning():  # Ensures the thread is running before waiting
            self.quit()  # Asks the thread to exit safely
            self.wait()  # Waits until the thread fully exits

        self.stop_signal.emit()  # Notifies that the process has stopped

    def cleanup(self):
        """Releases resources at the end of calibration."""
        self.logger.info("Cleaning up calibration resources...")
        try:
            if hasattr(self, "camera") and self.camera:
                self.camera.Close()
                del self.camera  # Release object
                self.camera = None
                self.logger.info("Camera closed.")
        except Exception as e:
            self.logger.error(f"Cleanup error: {str(e)}", exc_info=True)

    def calculate_calibration(self):
        """Performs the calibration computation."""
        self.logger.info("Processing calibration data...")
        self.progress_signal.emit(90, "Computing calibration values...")
        camera_matrix, dist_coeffs, obj_pose_tf_list, rob_pose_tf_list = utilities.calibrate_camera_with_charuco (self.global_data.image_folder,
                                                                                                                  self.global_data.charuco_detector,
                                                                                                                  self.global_data.charuco_board,
                                                                                                                  self.global_data.robot_pose_folder,
                                                                                                                  self.global_data.obj_pose_folder)
        if self.global_data.calib_config == 0:
            X_matrix, pose_vector = utilities.eye_in_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, self.global_data.calib_method, self.global_data.method_map)
            self.global_data.final_calib_method = self.global_data.calib_method
            self.global_data.final_calib_config = self.global_data.calib_config
        else:
            X_matrix, pose_vector = utilities.eye_to_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, self.global_data.calib_method, self.global_data.method_map)
            self.global_data.final_calib_method = self.global_data.calib_method
            self.global_data.final_calib_config = self.global_data.calib_config
        
        self.global_data.camera_matrix = camera_matrix
        self.global_data.dist_coeffs = dist_coeffs
        self.global_data.X_matrix = X_matrix
        self.global_data.position_vector = pose_vector

        self.logger.info("Calibration successfully completed.")
        self.progress_signal.emit(99, "Calculation complete!")
        time.sleep(1) 
