import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities, utilities_camera

# ==== PARAMETERS – adjust as needed ====
calib_config = 0                # 0 = Eye-in-Hand, 1 = Eye-to-Hand

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

data_set = "data_sets\data_set_in_05_15"

image_folder = "cam_pictures"
robot_pose_folder = "robot_pose_tf"
obj_pose_folder = "obj_pose_tf"

# === ChArUco board parameters ===
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

# ============================================

def main():
    # Check if the folder already exists
    if not os.path.exists(data_set):
        print(f"Folder '{data_set}' does not exist.")
        sys.exit(1)  # Exit program with error code

    # Create subfolders and update variables to their full paths
    image_path = os.path.join(data_set, image_folder)
    robot_path = os.path.join(data_set, robot_pose_folder)
    obj_path = os.path.join(data_set, obj_pose_folder)

    print("Starting calibration calculation...")
    camera_matrix, dist_coeffs, obj_pose_tf_list, rob_pose_tf_list = utilities_camera.calibrate_camera_with_charuco(
        image_path, charuco_detector, charuco_board, robot_path, obj_path
    )

    if calib_config == 0:
        X_matrix, pose_vector = utilities.eye_in_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, calib_method, method_map)
    else:
        X_matrix, pose_vector = utilities.eye_to_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, calib_method, method_map)

    print("\nCalibration completed.")
    print(f"Camera matrix: {camera_matrix}")
    print(f"Distortion coefficients: {dist_coeffs}")
    print(f"X_matrix:\n{X_matrix}")
    print(f"Pose vector: {pose_vector}")

    # file_path = "calibration_results/calibration_in_05_15.yaml"
    # # Save calibration data using the updated function
    # success, message = utilities.save_calibration_results_yaml(
    #     file_path,
    #     camera_matrix,
    #     dist_coeffs,
    #     X_matrix,
    #     pose_vector,
    #     calib_config,
    #     calib_method
    # )

if __name__ == "__main__":
    main()
