import numpy as np
import os
import sys
import cv2
import glob
from scipy.spatial.transform import Rotation as R
from scipy.linalg import inv
import utilities_camera
import utilities

def main():
    # Initialization of parameters
    # Number of internal corners of the chessboard and their real size
    pattern_size = (7, 6)  # Number of inner corners in the chessboard (columns, rows)
    square_size = 0.03     # Size of each square on the chessboard in meters

    # Preparation of object points - 'pattern_points' represents the 3D positions of the chessboard corners in the real world
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)  # Create an array of zeros for 3D points
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)  # Generate 2D indices for corners
    pattern_points *= square_size  # Scale the points by the size of the squares

    # Initialization of variables
    corner_list = []  # List to store detected corners in images
    obj_pose_tf_list = []  # List to store the poses of the chessboard

    set_number = 0  # Dataset number to be used in folder naming
    data_set = f"data_set_{set_number:02d}"  # Formatted dataset folder name (e.g., "data_set_00")

    # Folder where images are stored
    image_folder = os.path.join(data_set, 'cam_pictures')  # Path to the folder containing camera pictures

    # Load all images with the .png extension from the 'cam_pictures' folder
    image_list = [cv2.imread(file) for file in glob.glob(f"{image_folder}/*.png")]  # Read all PNG images

    # Check if all images were loaded correctly
    for i, img in enumerate(image_list):
        if img is None:
            print(f"Image {i} was not loaded correctly.")  # Print a message if an image failed to load

    # Call the calibrate_lens function to compute the camera matrix and distortion coefficients using the loaded images
    camera_matrix, dist_coeffs = utilities_camera.calibrate_lens(image_list, pattern_points, pattern_size)

    # Print calibration results
    print("Camera calibration matrix:")
    print(camera_matrix)
    print("\nDistortion coefficients:")
    print(dist_coeffs)

    # Check if the corners folder exists; if not, create and save corner images
    corners_folder = os.path.join(data_set, 'cam_corners')
    if not os.path.exists(corners_folder):
        os.makedirs(corners_folder)
        save_corner_image = True
    else:
        save_corner_image = False

    # Iterate through each image in the list
    for i, img in enumerate(image_list):
        # Convert the image to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        found, corners = utilities_camera.find_corners(img,pattern_size)

        if save_corner_image:
            # Draw corners on the image and save it
            image_corner = utilities_camera.draw_corners(img, corners, pattern_size)
            filename = f"image_corner_{i:02}.png"
            filepath = os.path.join(corners_folder, filename)
            cv2.imwrite(filepath, image_corner)

        # Append the found corners to the list
        corner_list.append(corners)

        # Raise an exception if corners were not found in the image
        if not found:
            raise Exception(f"Failed to find corners in img # {i}")

        # Calculate the object pose (rvec, tvec) using the camera matrix and distortion coefficients
        rvec, tvec = utilities_camera.get_object_pose(pattern_points, corners, camera_matrix, dist_coeffs)
        combined_vector = np.concatenate((tvec, rvec))

        # Create a transformation matrix from the pose vector and append it to the list
        object_pose_tf = utilities.pose_vector_to_tf_matrix(combined_vector)
        obj_pose_tf_list.append(object_pose_tf)


    #----------------------------------------------------------------------------------------------------

    # Load all robot poses into a list
    robot_pose_tf_folder = os.path.join(data_set, 'robot_pose_tf')
    rob_pose_tf_list = utilities.load_npy_data(robot_pose_tf_folder)
    R_base2gripper, t_base2gripper = utilities.decompose_tf_matrices(rob_pose_tf_list)
    # Invert the object pose transformation matrices and decompose them
    inv_rob_pose_tf_list = utilities.invert_tf_matrices(rob_pose_tf_list)
    R_gripper2base, t_gripper2base = utilities.decompose_tf_matrices(inv_rob_pose_tf_list)

    # Decompose the transformation matrices into rotation and translation components
    R_cam2target, t_cam2target = utilities.decompose_tf_matrices(obj_pose_tf_list)
    inv_obj_pose_tf_list = utilities.invert_tf_matrices(obj_pose_tf_list)
    R_target2cam, t_target2cam = utilities.decompose_tf_matrices(inv_obj_pose_tf_list)
    
    # Perform Hand-Eye calibration
    R_base2camera, t_base2camera = cv2.calibrateHandEye(
        R_gripper2base, t_gripper2base,
        R_cam2target, t_cam2target,
        method=cv2.CALIB_HAND_EYE_TSAI # You can choose another method, e.g., 'CALIB_HAND_EYE_PARK', etc.
    )

    # Construct the resulting transformation matrix X (robot base to camera)
    T_base2camera = np.eye(4)
    T_base2camera[:3, :3] = np.array(R_base2camera)
    T_base2camera[:3, 3] = np.array(t_base2camera).flatten()

    print("Resulting transformation matrix X (robot base to camera):")
    print(T_base2camera)

    
    # Perform Robot-World/Hand-Eye calibration
    R_camera2base_W, t_camera2base_W, R_target2gripper_W, t_target2gripper_W = cv2.calibrateRobotWorldHandEye(
        R_gripper2base, t_gripper2base,
        R_target2cam, t_target2cam,
        method=cv2.CALIB_ROBOT_WORLD_HAND_EYE_SHAH # You can choose another method, e.g., 'CALIB_HAND_EYE_PARK', etc.
    )

    # Construct the resulting transformation matrix X (robot base to camera)
    # It should come out inverted (camera to robot base), I don't know why it doesn't come out that way
    T_base2camera_W = np.eye(4)
    T_base2camera_W[:3, :3] = np.array(R_camera2base_W)
    T_base2camera_W[:3, 3] = np.array(t_camera2base_W).flatten()

    print("Resulting transformation matrix X (robot base to camera):")
    print(T_base2camera_W)

    # Construct the resulting transformation matrix X (gripper to target)
    T_gripper2target = np.eye(4)
    T_gripper2target[:3, :3] = np.array(R_target2gripper_W)
    T_gripper2target[:3, 3] = np.array(t_target2gripper_W).flatten()

    print("Resulting transformation matrix Z (gripper to target):")
    print(T_gripper2target)

    print("Resulting transformation matrix Z (gripper to target) inverted:")
    print(np.linalg.inv(T_gripper2target))






if __name__ == '__main__':
    sys.exit(main())


'''
# inicializace matic 
    A, B = [], []

    for i in range(1,len(image_list)):
        p = rob_pose_list[i-1], obj_pose_list[i-1]
        n = rob_pose_list[i], obj_pose_list[i]
        A.append(np.dot(inv(p[0]), n[0]))
        B.append(np.dot(inv(p[1]), n[1]))

    inv_A = invert_transformations(A)

'''