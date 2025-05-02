import numpy as np
import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities

# ==== PARAMETRY – uprav si podle potřeby ====
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

data_set = "data_sets/basic_data_set_in_mereni_02_05"

image_folder = "cam_pictures"
tcp_pose_folder = "tcp_pose_tf"
joints_pose_folder = "joints_pose"
robot_pose_folder = "robot_pose_tf"
obj_pose_folder = "obj_pose_tf"

# === Parametry ChArUco desky ===
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
    
    # Kontrola, zda složka už existuje
    if not os.path.exists(data_set):
        print(f"Složka '{data_set}' neexistuje.")
        sys.exit(1)  # Ukončí program s chybovým kódem

    # Vytvoření podsložek a aktualizace proměnných na jejich plné cesty
    image_path = os.path.join(data_set, image_folder)
    robot_path = os.path.join(data_set, robot_pose_folder)
    obj_path = os.path.join(data_set, obj_pose_folder)

    print("Spouštím výpočet kalibrace...")
    camera_matrix, dist_coeffs, obj_pose_tf_list, rob_pose_tf_list = utilities.calibrate_camera_with_charuco(
        image_path, charuco_detector, charuco_board, robot_path, obj_path
    )

    if calib_config == 0:
        X_matrix, pose_vector = utilities.eye_in_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, calib_method, method_map)
    else:
        X_matrix, pose_vector = utilities.eye_to_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, calib_method, method_map)

    print("\nKalibrace dokončena.")
    print(f"Kamera: {camera_matrix}")
    print(f"koeficienty: {dist_coeffs}")
    print(f"X_matrix:\n{X_matrix}")
    print(f"Pose vector: {pose_vector}")

    file_path = "calibration_results/basic_calib_in_02_05.yaml"
    # Save calibration data using the updated function
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
