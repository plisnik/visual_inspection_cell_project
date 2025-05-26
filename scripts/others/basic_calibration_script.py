import numpy as np
import time
import rtde_control
import rtde_receive
from pypylon import pylon
import cv2
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities, utilities_camera
from ur_robot_calib_params import read_calib_data

# ==== PARAMETERS – adjust as needed ====
ip_address = "192.168.209.135"  # Robot IP address
light_output_id = 0             # Digital output ID
light_on = True                 # Turn on light?

calib_config = 1                # 0 = Eye-in-Hand, 1 = Eye-to-Hand

calib_method = "TSAI"
# Mapping method names to cv2 constants
method_map = {
    'TSAI': cv2.CALIB_HAND_EYE_TSAI,
    'PARK': cv2.CALIB_HAND_EYE_PARK,
    'HORAUD': cv2.CALIB_HAND_EYE_HORAUD,
    'ANDREFF': cv2.CALIB_HAND_EYE_ANDREFF,
    'DANIILIDIS': cv2.CALIB_HAND_EYE_DANIILIDIS,
    'LI (world)': cv2.CALIB_ROBOT_WORLD_HAND_EYE_LI,
    'SHAH (world)': cv2.CALIB_ROBOT_WORLD_HAND_EYE_SHAH,
}

data_set = "data_sets/data_set_to_05_09_vice_blize"

image_folder = "cam_pictures"
tcp_pose_folder = "tcp_pose_tf"
joints_pose_folder = "joints_pose"
robot_pose_folder = "robot_pose_tf"
obj_pose_folder = "obj_pose_tf"

# === ChArUco board parameters ===
square_length = 0.016
marker_length = 0.012
board_rows = 8
board_cols = 10
# square_length = 0.03
# marker_length = 0.022
# board_rows = 6
# board_cols = 8
board_size = (board_cols, board_rows)
board_width = board_cols * square_length
board_height = board_rows * square_length
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
charuco_board = cv2.aruco.CharucoBoard(board_size, square_length, marker_length, aruco_dict)
charuco_board.setLegacyPattern(True)
charuco_detector = cv2.aruco.CharucoDetector(charuco_board)

# Parameters for point generation
scale_factor = 0.75  # factor for rectangle in image
distance = 0.25      # in meters
# ============================================

def main():
    """
    Main function for automatic robot calibration using RTDE interfaces.

    This function orchestrates the complete automatic calibration process including:
    1. Setting up camera and robot connections using RTDE interfaces
    2. Initial positioning with freedrive mode and visual feedback
    3. Generating calibration positions based on configuration (eye-in-hand/eye-to-hand)
    4. Automatically moving robot to each position and capturing data
    5. Computing hand-eye calibration from collected data
    6. Saving results to YAML file

    Returns:
        None

    Notes:
        - Uses RTDE (Real-Time Data Exchange) for robot communication
        - Robot moves automatically to generated calibration positions
        - Initial position is captured through freedrive mode with visual feedback
        - Different point generation strategies for eye-in-hand vs eye-to-hand configurations
        - Camera settings are loaded from UserSet1 (configured via Pylon Viewer)
        - Light control is optional based on light_on parameter
        - Creates new dataset directory with subfolders for organized data storage
    """
    print("Starting calibration...")

    # Turn on light if enabled
    if light_on:
        if not utilities.enable_digital_output(ip_address, light_output_id):
            raise RuntimeError("Failed to turn on light")
        
    # Initialize camera
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    camera.Open()

    # Load user-defined camera settings (configured via Pylon Viewer)
    camera.UserSetSelector.SetValue("UserSet1")
    camera.UserSetLoad.Execute()

    # Try to enable freedrive mode for initial positioning
    success, message = utilities.enable_freedrive_mode(ip_address)
    if success:
        print("Freedrive mode enabled")
    else:
        raise RuntimeError(f"Failed to enable freedrive mode: {message}")
    time.sleep(1)

    # Start image acquisition for initial positioning feedback
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 

    while camera.IsGrabbing():
        grab_result = camera.RetrieveResult(500, pylon.TimeoutHandling_Return)
        if grab_result.GrabSucceeded():
            frame = grab_result.Array
            frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
            # Draw scalable rectangle for calibration board positioning
            frame_final, x_rect, y_rect, rect_width, rect_height = utilities_camera.draw_scalable_rectangle(frame,scale_factor)
            
            # Resize for display (25% of original size)
            window_image = cv2.resize(frame_final, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)

            # Display image with positioning guide
            cv2.imshow("Camera", window_image)

            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord("q")):  # ESC or 'q' to finish positioning
                image = frame_final.copy()
                break

    # Cleanup camera resources
    grab_result.Release()
    camera.StopGrabbing()
    cv2.destroyAllWindows()

    if image is None:
        raise RuntimeError("Failed to capture image from camera.")
    else:
        print("Image successfully captured.")

    # Try to disable freedrive mode before automatic movement
    success, message = utilities.disable_freedrive_mode(ip_address)
    if success:
        print("Freedrive mode disabled")
    else:
        raise RuntimeError(f"Failed to disable freedrive mode: {message}")
    time.sleep(1)

    # Get image dimensions for point generation
    img_height, img_width, channel = image.shape

    # TODO: Test generate_points_on_circle_2 function

    # Generate calibration positions based on configuration
    if calib_config == 0:
        # Eye-in-Hand calibration - camera moves with robot
        source_axis = np.array([0, 0, 1])  # robot axis aligned with camera axis
        circle_points = utilities.generate_points_on_circle(8, 0.15, distance, source_axis)
        # circle_points_2 = utilities.generate_points_on_circle(10, 0.25, distance, source_axis)
        plane_positions = utilities.generate_plane_points(
            img_width, img_height,
            board_width, board_height,
            rect_width, rect_height,
            x_rect, y_rect,
            source_axis
            )
        # Combine lists: origin point + valid camera positions + circular points
        points = [[0, 0, 0, 0, 0, 0]] + plane_positions + circle_points

    else:
        # Eye-to-Hand calibration - camera is stationary
        source_axis = np.array([1, 0, 0])  # robot axis aligned with camera axis
        # circle_points = utilities.generate_points_on_circle(8, 0.15, distance, source_axis)
        circle_points_2 = utilities.generate_points_on_circle_2(
            img_width,img_height,
            board_width, board_height,
            rect_width, rect_height,
            x_rect, y_rect,
            16, source_axis
            )
        plane_positions = utilities.generate_plane_points(
            img_width, img_height,
            board_width, board_height,
            rect_width, rect_height,
            x_rect, y_rect,
            source_axis
            )
        # Combine lists: origin point + valid camera positions + circular points_2
        points = [[0, 0, 0, 0, 0, 0]] + plane_positions + circle_points_2

    # Get initial TCP position using RTDE receive interface
    rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)
    first_TCP = rtde_r.getActualTCPPose()
    first_tf = utilities.pose_vector_to_tf_matrix(first_TCP)
    rtde_r.disconnect()
    
    # Load robot calibration files for forward kinematics
    urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
    calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'
    a, d, alpha = read_calib_data.load_dh_parameters_from_urcontrol(urcontrol_file)
    delta_theta, delta_a, delta_d, delta_alpha = read_calib_data.load_mounting_calibration_parameters(calibration_file)

    # Check if dataset folder already exists
    if os.path.exists(data_set):
        print(f"Folder '{data_set}' already exists. Choose a different name or delete it first.")
        sys.exit(1)  # Exit program with error code

    # Create new dataset folder
    os.makedirs(data_set)

    # Create subfolders and update variables to their full paths
    image_path = os.path.join(data_set, image_folder)
    tcp_path = os.path.join(data_set, tcp_pose_folder)
    joints_path = os.path.join(data_set, joints_pose_folder)
    robot_path = os.path.join(data_set, robot_pose_folder)
    obj_path = os.path.join(data_set, obj_pose_folder)

    for folder in [image_path, tcp_path, joints_path, robot_path, obj_path]:
        os.makedirs(folder)

    # Execute calibration sequence by moving to each generated point
    for i, point in enumerate(points):
        print(f"\nPoint {i+1}/{len(points)}")

        # Calculate target position relative to initial position
        point_tf = utilities.pose_vector_to_tf_matrix(point)
        point_base_tf = first_tf @ point_tf
        point_base = utilities.tf_matrix_to_pose_vector(point_base_tf)

        # Move robot to calibration position using RTDE control interface
        rtde_c = rtde_control.RTDEControlInterface(ip_address)
        rtde_c.moveL(point_base, speed=0.25, acceleration=0.25)
        time.sleep(1)
        rtde_c.disconnect()

        # Capture image at current position
        grab_result = camera.GrabOne(2000)
        if not grab_result.GrabSucceeded():
            raise TimeoutError("❌ Failed to capture image from camera")

        image = grab_result.Array
        image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
        path = utilities_camera.save_current_frame(image_path, image)
        print(f"Saved image: {path}")

        # Get actual robot pose and joint angles using RTDE receive interface
        rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)
        actual_TCP = rtde_r.getActualTCPPose()
        actual_joints = np.array(rtde_r.getActualQ())
        rtde_r.disconnect()

        # Convert to transformation matrices
        tf_matrix = utilities.pose_vector_to_tf_matrix(actual_TCP)
        robot_fk = utilities.fk_with_corrections(actual_joints, a, d, alpha, delta_theta, delta_a, delta_d, delta_alpha)

        # Save pose and joint data
        utilities.save_pose_data(tcp_path, tf_matrix)
        utilities.save_pose_data(robot_path, robot_fk)
        utilities.save_joints_data(joints_path, actual_joints)

    # Close camera after data collection
    camera.Close()

    # Return robot to initial position using RTDE control interface
    rtde_c = rtde_control.RTDEControlInterface(ip_address)
    rtde_c.moveL(first_TCP, speed=0.1, acceleration=0.15)
    time.sleep(1)
    rtde_c.disconnect()

    # Turn off light if it was enabled
    if light_on:
        utilities.disable_digital_output(ip_address, light_output_id)

    print("\nStarting calibration calculation...")
    # Perform camera calibration using ChArUco board
    camera_matrix, dist_coeffs, obj_pose_tf_list, rob_pose_tf_list = utilities_camera.calibrate_camera_with_charuco(
        image_path, charuco_detector, charuco_board, robot_path, obj_path
    )

    # Perform hand-eye calibration based on configuration
    if calib_config == 0:
        X_matrix, pose_vector = utilities.eye_in_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, calib_method, method_map)
    else:
        X_matrix, pose_vector = utilities.eye_to_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, calib_method, method_map)

    print("\nCalibration completed.")
    print(f"Camera matrix: {camera_matrix}")
    print(f"Distortion coefficients: {dist_coeffs}")
    print(f"X_matrix:\n{X_matrix}")
    print(f"Pose vector: {pose_vector}")

    # Save calibration results to YAML file
    file_path = "calibration_results/calib_to_05_09_vice_blize.yaml"
    success, message = utilities.save_calibration_results_yaml(
        file_path,
        camera_matrix,
        dist_coeffs,
        X_matrix,
        pose_vector,
        calib_config,
        calib_method
    )

if __name__ == "__main__":
    main()