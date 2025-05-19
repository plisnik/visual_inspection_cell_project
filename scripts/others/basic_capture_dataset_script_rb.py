import numpy as np
import time
from pypylon import pylon
import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities, utilities_camera, robot_interface
from ur_robot_calib_params import read_calib_data

# ==== PARAMETERS - customize as needed ====
# ip_address = "192.168.209.133"  # IP address of the robot
ip_address = "192.168.209.133"  # IP address of the robot
light_output_id = 0             # Digital Output ID
light_on = True                 # Turn on the light?

calib_config = 0                # 0 = Eye-in-Hand, 1 = Eye-to-Hand

data_set = "data_sets/basic_data_set_in_05_06"
image_folder = "cam_pictures"
tcp_pose_folder = "tcp_pose_tf"
joints_pose_folder = "joints_pose"
robot_pose_folder = "robot_pose_tf"
obj_pose_folder = "obj_pose_tf"

# === Parameters of the ChArUco board ===
square_length = 0.03
marker_length = 0.022
board_rows = 6
board_cols = 8
board_size = (board_cols, board_rows)
board_width = board_cols * square_length
board_height = board_rows * square_length
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
charuco_board = cv2.aruco.CharucoBoard(board_size, square_length, marker_length, aruco_dict)
charuco_board.setLegacyPattern(True)
charuco_detector = cv2.aruco.CharucoDetector(charuco_board)

# Parameters for generating points
scale_factor = 0.75  # factor for the rectangle in the image
distance = 0.38     # in metre
# ============================================

def main():
    print("Starting calibration...")
    robot = robot_interface.RobotInterface(ip_address, mode="plc_opcua")

    # Checking whether a folder already exists
    if os.path.exists(data_set):
        print(f"The folder '{data_set}' already exists. Choose a different name or delete it first.")
        sys.exit(1)

    # Create a new folder
    os.makedirs(data_set)

    # Creating subfolders and updating variables to their full paths
    image_path = os.path.join(data_set, image_folder)
    tcp_path = os.path.join(data_set, tcp_pose_folder)
    joints_path = os.path.join(data_set, joints_pose_folder)
    robot_path = os.path.join(data_set, robot_pose_folder)
    obj_path = os.path.join(data_set, obj_pose_folder)

    for folder in [image_path, tcp_path, joints_path, robot_path, obj_path]:
        os.makedirs(folder)

    # Switching on the light
    if light_on:
        if not utilities.enable_digital_output_rb(robot, light_output_id):
            raise RuntimeError("Failed to turn on the light")

    # Initialize camera
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    camera.Open()

    # Load user-defined camera settings (configured via Pylon Viewer)
    camera.UserSetSelector.SetValue("UserSet1")
    camera.UserSetLoad.Execute()

    # Try to enable freedrive mode
    success, message = utilities.enable_freedrive_mode_rb(robot)
    if success:
        print("Freedrive mode enabled")
    else:
        raise RuntimeError(f"Failed to enable freedrive mode: {message}")
    time.sleep(1)

    # Start image acquisition
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 

    while camera.IsGrabbing():
        grab_result = camera.RetrieveResult(500, pylon.TimeoutHandling_Return)
        if grab_result.GrabSucceeded():
            frame = grab_result.Array
            frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
            frame_final, x_rect, y_rect, rect_width, rect_height = utilities_camera.draw_scalable_rectangle(frame,scale_factor)
            # Shrink for display
            window_image = cv2.resize(frame_final, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)

            # Image display
            cv2.imshow("Camera", window_image)

            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord("q")):  # ESC or 'q' for quit
                image = frame_final.copy()
                break
            elif key == ord("s"):  # Press "s" 
                # Cleanup
                grab_result.Release()
                camera.StopGrabbing()
                cv2.destroyAllWindows()
                exit()

    # Cleanup
    grab_result.Release()
    camera.StopGrabbing()
    cv2.destroyAllWindows()

    if image is None:
        raise RuntimeError("Failed to save camera image.")
    else:
        print("Image successfully captured.")

    # Try to disable freedrive mode
    success, message = utilities.disable_freedrive_mode_rb(robot)
    if success:
        print("Freedrive mode disabled")
    else:
        raise RuntimeError(f"Failed to disable freedrive mode: {message}")
    print("čekám")
    time.sleep(10)

    img_height, img_width, channel = image.shape

    if calib_config == 0:
        # Eye-in-Hand calibration
        source_axis = np.array([0, 0, 1]) # robot axis aligned with the camera axis
        circle_points = utilities.generate_points_on_circle(20, 0.15, distance, source_axis)
        # circle_points_2 = utilities.generate_points_on_circle(8, 0.05, distance, source_axis)
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
        # Eye-to-Hand calibration
        source_axis = np.array([1, 0, 0]) # robot axis (board) aligned with the camera axis
        # circle_points = utilities.generate_points_on_circle(8, 0.15, distance, source_axis)
        circle_points_2 = utilities.generate_points_on_circle_2(
            img_width,img_height,
            board_width, board_height,
            rect_width, rect_height,
            x_rect, y_rect,
            8, source_axis
            )
        plane_positions = utilities.generate_plane_points(
            img_width, img_height,
            board_width, board_height,
            rect_width, rect_height,
            x_rect, y_rect,
            source_axis
            )
        # Combine lists: origin point + valid camera positions + circular points/_2
        points = [[0, 0, 0, 0, 0, 0]] + plane_positions + circle_points_2

    first_TCP = np.array(robot.get_actual_tcp_pose())
    first_tf = utilities.pose_vector_to_tf_matrix(first_TCP)
    
    # Calibration files
    urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
    calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'
    a, d, alpha = read_calib_data.load_dh_parameters_from_urcontrol(urcontrol_file)
    delta_theta, delta_a, delta_d, delta_alpha = read_calib_data.load_mounting_calibration_parameters(calibration_file)

    for i, point in enumerate(points):
        print(f"\nBod {i+1}/{len(points)}")

        point_tf = utilities.pose_vector_to_tf_matrix(point)
        point_base_tf = first_tf @ point_tf
        point_base = utilities.tf_matrix_to_pose_vector(point_base_tf)

        robot.moveL(point_base, speed=0.25, acceleration=0.25)
        time.sleep(0.5)

        grab_result = camera.GrabOne(2000)
        if not grab_result.GrabSucceeded():
            raise TimeoutError("Couldn't get a picture from the camera")

        image = grab_result.Array
        image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
        path = utilities_camera.save_current_frame(image_path, image)
        print(f"Saved image: {path}")

        actual_TCP = np.array(robot.get_actual_tcp_pose())
        actual_joints = np.array(robot.get_actual_joints())

        tf_matrix = utilities.pose_vector_to_tf_matrix(actual_TCP)
        robot_fk = utilities.fk_with_corrections(actual_joints, a, d, alpha, delta_theta, delta_a, delta_d, delta_alpha)

        utilities.save_pose_data(tcp_path, tf_matrix)
        utilities.save_pose_data(robot_path, robot_fk)
        utilities.save_joints_data(joints_path, actual_joints)

    camera.Close()

    robot.moveL(first_TCP, speed=0.1, acceleration=0.15)
    time.sleep(1)

    # Switch off light
    if light_on:
        utilities.disable_digital_output_rb(robot, light_output_id)

if __name__ == "__main__":
    main()
