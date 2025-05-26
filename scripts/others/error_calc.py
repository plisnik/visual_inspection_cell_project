import numpy as np
import cv2
import os
import sys
from typing import List, Tuple
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities
from scipy.spatial.transform import Rotation as R


def rot_trans_error_all_pairs(
    T_A_list: List[np.ndarray], 
    T_B_list: List[np.ndarray], 
    T_X: np.ndarray, 
    n: int
) -> Tuple[float, float]:
    """
    Computes average rotation and translation error using all unique pose pairs (i != j). 
    Designed for eye-in-hand configuration.
    
    For eye-to-hand configuration, the matrix multiplication order needs to be swapped in calculations.

    Parameters:
        T_A_list (List[np.ndarray]): List of 4x4 robot transformation matrices
        T_B_list (List[np.ndarray]): List of 4x4 camera transformation matrices
        T_X (np.ndarray): 4x4 estimated transformation matrix (from B to A)
        n (int): Maximum number of poses to use for calculation

    Returns:
        Tuple[float, float]: Mean squared rotation error (rad), mean squared translation error (m)
    """
    rot_errors = []
    trans_errors = []

    R_X = T_X[:3, :3]
    t_X_trans = T_X[:3, 3]
    num = min(n, len(T_A_list))  # use all available or up to n

    for i in range(num):
        for j in range(num):
            if i == j:
                continue

            # ROTATION ERROR
            RX1 = T_A_list[i][:3, :3] @ R_X @ T_B_list[i][:3, :3]
            RX2 = T_A_list[j][:3, :3] @ R_X @ T_B_list[j][:3, :3]
            delta_R = RX1 @ np.linalg.inv(RX2)
            angle = np.linalg.norm(R.from_matrix(delta_R).as_rotvec())
            rot_errors.append(angle)

            # TRANSLATION ERROR
            t_1 = T_A_list[i][:3, :3] @ R_X @ T_B_list[i][:3, 3] + T_A_list[i][:3, :3] @ t_X_trans + T_A_list[i][:3, 3]
            t_2 = T_A_list[j][:3, :3] @ R_X @ T_B_list[j][:3, 3] + T_A_list[j][:3, :3] @ t_X_trans + T_A_list[j][:3, 3]
            delta_t = t_1 - t_2
            trans_errors.append(np.linalg.norm(delta_t)**2)

    e_R = np.mean(rot_errors)
    e_T = np.mean(trans_errors)
    return e_R, e_T


def reprojection_error(
    object_points: np.ndarray, 
    image_points_measured: List[np.ndarray], 
    rvecs: List[np.ndarray], 
    tvecs: List[np.ndarray], 
    camera_matrix: np.ndarray, 
    dist_coeffs: np.ndarray, 
    n: int
) -> float:
    """
    Calculates the reprojection error for camera calibration validation.

    Parameters:
        object_points (np.ndarray): 3D object points (e.g., checkerboard corners) with shape (N, 3)
        image_points_measured (List[np.ndarray]): Corresponding 2D points from images with shape (N, 2)
        rvecs (List[np.ndarray]): Rotation vectors for each image
        tvecs (List[np.ndarray]): Translation vectors for each image
        camera_matrix (np.ndarray): Camera intrinsic matrix
        dist_coeffs (np.ndarray): Distortion coefficients
        n (int): Maximum number of images to process

    Returns:
        float: Mean reprojection error in pixels
    """
    total_error = 0
    num_points = 0
    errors = [] 
    num = min(n, len(image_points_measured))

    for i in range(num):
        obj_points_projected, _ = cv2.projectPoints(object_points, rvecs[i], tvecs[i], camera_matrix, dist_coeffs)
        if obj_points_projected.shape != image_points_measured[i].shape:
            continue
        error = cv2.norm(image_points_measured[i], obj_points_projected, cv2.NORM_L1) / len(obj_points_projected)
        errors.append(error)
        total_error += error
        num_points += 1

    mean_error = total_error / num_points
    return mean_error


def absolute_error_eye_in_hand(
    rob_pose_tf_list: List[np.ndarray], 
    obj_pose_tf_list: List[np.ndarray], 
    X_matrix: np.ndarray, 
    real_pose: List[np.ndarray], 
    n: int
) -> np.ndarray:
    """
    Calculates the average absolute positional error for eye-in-hand configuration.
    
    Parameters:
        rob_pose_tf_list (List[np.ndarray]): List of robot pose transformation matrices
        obj_pose_tf_list (List[np.ndarray]): List of detected object pose transformation matrices from camera
        X_matrix (np.ndarray): Hand-eye calibration matrix
        real_pose (List[np.ndarray]): List of real object positions in world coordinate system (without rotation)
        n (int): Maximum number of poses to process
        
    Returns:
        np.ndarray: Average absolute positional error for each axis [x, y, z]
        
    Raises:
        ValueError: If input lists have different lengths
    """
    if len(rob_pose_tf_list) != len(obj_pose_tf_list) or len(rob_pose_tf_list) != len(real_pose):
        raise ValueError("All position lists must have the same length")
    
    error_sum = 0.0
    num_points = 0
    num = min(n, len(rob_pose_tf_list))
    
    for i in range(num):
        # Calculate detected position in world coordinate system
        world_T_object = rob_pose_tf_list[i] @ X_matrix @ obj_pose_tf_list[i]
        
        # Extract position (translation part) from transformation matrix
        detected_position = world_T_object[:3, 3]
        
        # Calculate error for this point
        error = np.abs(np.array(real_pose[i]) - detected_position)
        error_sum += error
        num_points += 1
    
    return error_sum / num_points


# ==== PARAMETERS – adjust as needed ====
calib_config = 0                # 0 = Eye-in-Hand, 1 = Eye-to-Hand

calib_method = "PARK"
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
# Alternative board parameters (commented out):
# square_length = 0.016
# marker_length = 0.012
# board_rows = 8
# board_cols = 10
board_size = (board_cols, board_rows)
board_width = board_cols * square_length
board_height = board_rows * square_length
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
charuco_board = cv2.aruco.CharucoBoard(board_size, square_length, marker_length, aruco_dict)
charuco_board.setLegacyPattern(True)
charuco_detector = cv2.aruco.CharucoDetector(charuco_board)

# ============================================


def main() -> None:
    """
    Main function that performs camera calibration, hand-eye calibration, and error analysis.
    
    Returns:
        None
    """
    number = 24

    # Check if folder exists
    if not os.path.exists(data_set):
        print(f"Folder '{data_set}' does not exist.")
        sys.exit(1)  # Exit program with error code

    # Create subfolder paths and update variables to their full paths
    image_path = os.path.join(data_set, image_folder)
    robot_path = os.path.join(data_set, robot_pose_folder)

    # Load all PNG images from the folder
    image_list = [
        cv2.imread(os.path.join(image_path, file)) 
        for file in os.listdir(image_path) if file.endswith(".png")
    ]

    if not image_list:
        raise ValueError("No calibration images found in the specified folder.")
    image_list = image_list[:number]

    # Initialize lists for detected ChArUco corners and IDs
    all_charuco_corners = []
    all_charuco_ids = []
    valid_indices = []  # List to store valid image indices
    image_size = None

    # Process each image
    for idx, image in enumerate(image_list):
        if image is None:
            continue  # Skip invalid images
        
        if image_size is None:
            image_size = image.shape[:2]  # Store image size from the first valid image

        # Detect ChArUco corners and IDs
        charuco_corners, charuco_ids, _, _ = charuco_detector.detectBoard(image)

        if charuco_corners is not None and charuco_ids is not None:
            all_charuco_corners.append(charuco_corners)
            all_charuco_ids.append(charuco_ids)
            valid_indices.append(idx)  # Store index of valid images

    if not all_charuco_corners:
        raise ValueError("No valid ChArUco corners detected in the images.")

    # Initialize camera matrix and distortion coefficients
    camera_matrix = np.zeros((3, 3), dtype=np.float64)
    dist_coeffs = np.zeros((5,), dtype=np.float64)

    # Perform camera calibration
    retval, camera_matrix, dist_coeffs, rvecs, tvecs, _, _, repro_error = cv2.aruco.calibrateCameraCharucoExtended(
        all_charuco_corners, 
        all_charuco_ids, 
        charuco_board, 
        image_size, 
        camera_matrix, 
        dist_coeffs
    )

    if not retval:
        raise ValueError("Camera calibration failed.")

    # Process object positions
    obj_pose_tf_list = []
    for tvec, rvec in zip(tvecs, rvecs):
        tvec = tvec.flatten()
        rvec = rvec.flatten()

        # Create pose vector and convert it to a transformation matrix
        pose_vector = np.hstack((tvec, rvec))
        transformation_matrix = utilities.pose_vector_to_tf_matrix(pose_vector)

        obj_pose_tf_list.append(transformation_matrix)

    # Load robot positions
    rob_pose_tf_list = utilities.load_npy_data(robot_path)
    rob_pose_tf_list = [rob_pose_tf_list[i] for i in valid_indices]

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

    # Get object points for reprojection error calculation
    obj_points = charuco_board.getChessboardCorners()

    # Load real pose data
    real_pose_file = "poloha_robota_presne\\tcp_pose_vector.txt"
    with open(real_pose_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 3:  # Assume first three elements are x, y, z
                real_pose = np.array([float(parts[0]), float(parts[1]), float(parts[2])])

    real_pose_list = [real_pose.copy() for _ in range(len(rob_pose_tf_list))]
    
    # Calculate and display error metrics
    repro_err = reprojection_error(obj_points, all_charuco_corners, rvecs, tvecs, camera_matrix, dist_coeffs, number)
    print(f"Reprojection error: {repro_err}")
    print("Mean reprojection error: ", np.mean(repro_error))

    e_R, e_T = rot_trans_error_all_pairs(rob_pose_tf_list, obj_pose_tf_list, X_matrix, number)
    print(f"Rotation error (all pairs): {e_R}")
    print(f"Translation error (all pairs): {e_T}")

    abs_error_x, abs_error_y, abs_error_z = absolute_error_eye_in_hand(rob_pose_tf_list, obj_pose_tf_list, X_matrix, real_pose_list, number)
    print(f"Average absolute error per axis: {abs_error_x, abs_error_y, abs_error_z}")
    abs_error = np.linalg.norm(np.array([abs_error_x, abs_error_y, abs_error_z]))
    print(f"Average absolute error: {abs_error*1000} mm")


if __name__ == "__main__":
    main()