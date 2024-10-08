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
    obj_pose_list = []  # List to store the poses of the chessboard

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
    camera_matrix, dist_coeffs = utilities_camera.calibrate_lens(image_list)

    # Print calibration results
    print("Camera calibration matrix:")
    print(camera_matrix)
    print("\nDistortion coefficients:")
    print(dist_coeffs)

    # Check if the corners folder exists; if not, create and save corner images
    corners_folder = os.path.join(data_set, 'cam_corners_pic')
    if not os.path.exists(corners_folder):
        os.makedirs(corners_folder)
        save_corner_image = True
    else:
        save_corner_image = False

    # Iterate through each image in the list
    for i, img in enumerate(image_list):
        # Convert the image to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        found, corners = utilities_camera.find_corners(img)

        if save_corner_image:
            # Draw corners on the image and save it
            image_corner = utilities_camera.draw_corners(img, corners)
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
        object_pose = utilities.create_tf_mat_from_vec(combined_vector)
        obj_pose_list.append(object_pose)



    exit("Zpráva: Ukončení skriptu.")

    input_folder='robot_pose_set_00'

    # Složka s transformačními maticemi
    folder_path_robot_pose = 'robot_pose_tf_set_00'
    os.makedirs(folder_path_robot_pose, exist_ok=True)

    #process_positon_files(input_folder, folder_path_robot_pose)

    # Načtení všech transformačních matic do seznamu
    rob_pose_list = load_transformation_matrices(folder_path_robot_pose)

    # inicializace matic - dále trochu změna na maticích - záleží na směrech atd
    A, B = [], []

    for i in range(1,len(image_list)):
        p = rob_pose_list[i-1], obj_pose_list[i-1]
        n = rob_pose_list[i], obj_pose_list[i]
        A.append(np.dot(inv(p[0]), n[0]))
        B.append(np.dot(inv(p[1]), n[1]))

    inv_A = invert_transformations(A)

    # Předpokládáme, že máme seznamy transformačních matic (4x4) pro robota a kameru
    # Tyto matice je třeba rozdělit na rotační a translační části.
    # Předpokládáme, že rob_pose_list obsahuje 4x4 transformační matice pro robota
    # A že camera_to_chessboard_list obsahuje 4x4 transformační matice z kalibrace kamery

    # Rozložíme matice na rotační a translační složky - MOŽNÁ NEBUDE POTŘEBA->PODLE TOHO ULOŽENÍ
    R_base2gripper, t_base2gripper = decompose_transformations(rob_pose_list)

    # inv_obj_pose_list = invert_transformations(obj_pose_list)
    R_cam2target, t_cam2target = decompose_transformations(obj_pose_list)

    # Provedeme Hand-Eye kalibraci
    R_target2gripper, t_target2gripper = cv2.calibrateHandEye(
        R_base2gripper, t_base2gripper,
        R_cam2target, t_cam2target,
        method=cv2.CALIB_HAND_EYE_TSAI  # Můžete zvolit jinou metodu, například 'CALIB_HAND_EYE_PARK' atd.
    )

    # Složení výsledné transformační matice X (kamera vůči robotu)
    T_target2gripper = np.eye(4)
    T_target2gripper[:3, :3] = R_target2gripper
    T_target2gripper[:3, 3] = t_target2gripper.flatten()

    print("Výsledná transformační matice X (ne kamera vůči robotu):")
    print(T_target2gripper)

    print("Výsledná transformační matice X invertovaná:")
    print(np.linalg.inv(T_target2gripper))

if __name__ == '__main__':
    sys.exit(main())
