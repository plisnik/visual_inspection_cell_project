import cv2
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities

# EYE-IN-HAND: KAMERA NA ROBOTU
# Definování cesty ke složce temporary_data_set a jejím podsložkám
data_set = "data_sets\\dataset_20250311_152014"

obj_pose_folder = os.path.join(data_set, 'obj_pose_tf')  # Path to the folder containing camera pictures
robot_pose_folder = os.path.join(data_set, 'robot_pose_tf')  # Path to the folder containing camera pictures
rob_pose_tf_list = utilities.load_npy_data(robot_pose_folder)
obj_pose_tf_list = utilities.load_npy_data(obj_pose_folder)

# Decompose the transformation matrices into rotation and translation components
R_grip2base, t_grip2base = utilities.decompose_tf_matrices(rob_pose_tf_list)
# Invert the object pose transformation matrices and decompose them
inv_rob_pose_tf_list = utilities.invert_tf_matrices(rob_pose_tf_list)
R_base2grip, t_base2grip = utilities.decompose_tf_matrices(inv_rob_pose_tf_list)
# Decompose the transformation matrices into rotation and translation components
R_target2cam, t_target2cam = utilities.decompose_tf_matrices(obj_pose_tf_list)
inv_obj_pose_tf_list = utilities.invert_tf_matrices(obj_pose_tf_list)
R_cam2target, t_cam2target = utilities.decompose_tf_matrices(inv_obj_pose_tf_list)

# Perform Hand-Eye calibration - Eye-in-Hand
R_cam2grip, t_cam2grip = cv2.calibrateHandEye(
   R_grip2base, t_grip2base,
   R_target2cam, t_target2cam,
   method=cv2.CALIB_HAND_EYE_ANDREFF # You can choose another method, e.g., 'CALIB_HAND_EYE_PARK', etc.
)

# Construct the resulting transformation matrix X (camera to gripper)
T_cam2grip = np.eye(4)
T_cam2grip[:3, :3] = np.array(R_cam2grip)
T_cam2grip[:3, 3] = np.array(t_cam2grip).flatten()

print("Resulting transformation matrix X (camera to gripper):")
print(T_cam2grip)

# Perform Hand-Eye calibration - Eye-in-Hand
R_cam2grip, t_cam2grip = cv2.calibrateHandEye(
   R_grip2base, t_grip2base,
   R_target2cam, t_target2cam,
   method=cv2.CALIB_HAND_EYE_DANIILIDIS # You can choose another method, e.g., 'CALIB_HAND_EYE_PARK', etc.
)

# Construct the resulting transformation matrix X (camera to gripper)
T_cam2grip = np.eye(4)
T_cam2grip[:3, :3] = np.array(R_cam2grip)
T_cam2grip[:3, 3] = np.array(t_cam2grip).flatten()

print("Resulting transformation matrix X (camera to gripper):")
print(T_cam2grip)

# Perform Hand-Eye calibration - Eye-in-Hand
R_cam2grip, t_cam2grip = cv2.calibrateHandEye(
   R_grip2base, t_grip2base,
   R_target2cam, t_target2cam,
   method=cv2.CALIB_HAND_EYE_HORAUD # You can choose another method, e.g., 'CALIB_HAND_EYE_PARK', etc.
)

# Construct the resulting transformation matrix X (camera to gripper)
T_cam2grip = np.eye(4)
T_cam2grip[:3, :3] = np.array(R_cam2grip)
T_cam2grip[:3, 3] = np.array(t_cam2grip).flatten()

print("Resulting transformation matrix X (camera to gripper):")
print(T_cam2grip)

# Perform Hand-Eye calibration - Eye-in-Hand
R_cam2grip, t_cam2grip = cv2.calibrateHandEye(
   R_grip2base, t_grip2base,
   R_target2cam, t_target2cam,
   method=cv2.CALIB_HAND_EYE_PARK # You can choose another method, e.g., 'CALIB_HAND_EYE_PARK', etc.
)

# Construct the resulting transformation matrix X (camera to gripper)
T_cam2grip = np.eye(4)
T_cam2grip[:3, :3] = np.array(R_cam2grip)
T_cam2grip[:3, 3] = np.array(t_cam2grip).flatten()

print("Resulting transformation matrix X (camera to gripper):")
print(T_cam2grip)

# Perform Hand-Eye calibration - Eye-in-Hand
R_cam2grip, t_cam2grip = cv2.calibrateHandEye(
   R_grip2base, t_grip2base,
   R_target2cam, t_target2cam,
   method=cv2.CALIB_HAND_EYE_TSAI # You can choose another method, e.g., 'CALIB_HAND_EYE_PARK', etc.
)

# Construct the resulting transformation matrix X (camera to gripper)
T_cam2grip = np.eye(4)
T_cam2grip[:3, :3] = np.array(R_cam2grip)
T_cam2grip[:3, 3] = np.array(t_cam2grip).flatten()

print("Resulting transformation matrix X (camera to gripper):")
print(T_cam2grip)

# Perform Robot-World/Hand-Eye calibration - Eye-in-Hand
R_base2target_W, t_base2target_W, R_grip2cam_W, t_grip2cam_W = cv2.calibrateRobotWorldHandEye(
   R_target2cam, t_target2cam,
   R_base2grip, t_base2grip,
   method=cv2.CALIB_ROBOT_WORLD_HAND_EYE_SHAH # You can choose another method, e.g., 'CALIB_ROBOT_WORLD_HAND_EYE_SHAH', etc.
)

T_grip2cam_W = np.eye(4)
T_grip2cam_W[:3, :3] = np.array(R_grip2cam_W)
T_grip2cam_W[:3, 3] = np.array(t_grip2cam_W).flatten()

print("Resulting transformation matrix X (camera to gripper):")
T_cam2grip_W = np.linalg.inv(T_grip2cam_W)
print(T_cam2grip_W)

# Perform Robot-World/Hand-Eye calibration - Eye-in-Hand
R_base2target_W, t_base2target_W, R_grip2cam_W, t_grip2cam_W = cv2.calibrateRobotWorldHandEye(
   R_target2cam, t_target2cam,
   R_base2grip, t_base2grip,
   method=cv2.CALIB_ROBOT_WORLD_HAND_EYE_LI # You can choose another method, e.g., 'CALIB_ROBOT_WORLD_HAND_EYE_SHAH', etc.
)

T_grip2cam_W = np.eye(4)
T_grip2cam_W[:3, :3] = np.array(R_grip2cam_W)
T_grip2cam_W[:3, 3] = np.array(t_grip2cam_W).flatten()

print("Resulting transformation matrix X (camera to gripper):")
T_cam2grip_W = np.linalg.inv(T_grip2cam_W)
print(T_cam2grip_W)
