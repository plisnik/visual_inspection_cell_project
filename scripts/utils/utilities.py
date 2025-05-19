import os
import yaml
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from numpy.typing import NDArray
from scipy.spatial.transform import Rotation as R
from typing import List, Tuple, Dict, Optional, Union, Any
import rtde_receive
import rtde_control
import rtde_io
import time
import shutil
import stat
import zipfile
from datetime import datetime
from pypylon import pylon
import cv2
from utils.robot_interface import RobotInterface

def dh_matrix(theta: float, a: float, d: float, alpha: float) -> np.ndarray:
    """
    Creates a Denavit-Hartenberg (DH) transformation matrix based on the given parameters.

    The DH parameters describe the relationship between two consecutive frames in a robotic manipulator,
    where each joint is associated with a matrix that transforms coordinates from one frame to another.

    Parameters:
        theta (float): Joint angle in radians (rotation about the z-axis).
        a (float): Link length (distance along the x-axis to the next joint).
        d (float): Link offset (distance along the z-axis between links).
        alpha (float): Link twist (angle in radians between the z-axes of two consecutive frames).

    Returns:
        np.ndarray: A 4x4 homogeneous transformation matrix representing the transformation from one link to the next.

    Notes:
        The resulting matrix follows the standard DH convention:
        - The first three rows and columns represent the rotation matrix.
        - The last column represents the translation vector.
        - The final row is always [0, 0, 0, 1], indicating that it is a homogeneous transformation.
    """

    # Validate input types
    if not all(isinstance(param, (float, int)) for param in [theta, a, d, alpha]):
        raise ValueError("All input parameters must be numbers (float or int).")
    
    # Construct and return the DH transformation matrix
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

def fk_with_corrections(joint_angles: np.ndarray, a: np.ndarray, d: np.ndarray, alpha: np.ndarray,
                        delta_theta: np.ndarray, delta_a: np.ndarray, delta_d: np.ndarray, delta_alpha: np.ndarray) -> np.ndarray:
    """
    Computes the forward kinematics for a robotic manipulator based on the given joint angles and DH parameters,
    including their respective corrections (delta values).

    Parameters:
        joint_angles (np.ndarray): Array of joint angles in radians for each joint.
        a (np.ndarray): Array of link lengths (distance along the x-axis to the next joint).
        d (np.ndarray): Array of link offsets (distance along the z-axis between links).
        alpha (np.ndarray): Array of link twists (angles in radians between the z-axes of two consecutive frames).
        delta_theta (np.ndarray): Corrections for joint angles (in radians).
        delta_a (np.ndarray): Corrections for link lengths.
        delta_d (np.ndarray): Corrections for link offsets.
        delta_alpha (np.ndarray): Corrections for link twists.

    Returns:
        np.ndarray: A 4x4 homogeneous transformation matrix representing the transformation from the base to the tool (end-effector).

    Notes:
        - The resulting matrix represents the overall transformation from the base of the robot to the end-effector.
        - Each individual transformation matrix is computed using the DH convention, with correction factors applied.
    """
    # Initialize the total transformation matrix as an identity matrix
    T = np.eye(4)

    # Compute the total transformation matrix
    for i in range(6):
        T_i = dh_matrix(joint_angles[i] + delta_theta[i], a[i] + delta_a[i], d[i] + delta_d[i], alpha[i] + delta_alpha[i])
        T = T @ T_i  # Matrix multiplication

    return T

def fk_default(joint_angles: np.ndarray, a: np.ndarray, d: np.ndarray, alpha: np.ndarray) -> np.ndarray:
    """
    Computes the forward kinematics for a robotic manipulator based on the given joint angles and DH parameters,
    without applying any corrections (delta values).

    Parameters:
        joint_angles (np.ndarray): Array of joint angles in radians for each joint.
        a (np.ndarray): Array of link lengths (distance along the x-axis to the next joint).
        d (np.ndarray): Array of link offsets (distance along the z-axis between links).
        alpha (np.ndarray): Array of link twists (angles in radians between the z-axes of two consecutive frames).

    Returns:
        np.ndarray: A 4x4 homogeneous transformation matrix representing the transformation from the base to the tool (end-effector).

    Notes:
        - The resulting matrix represents the overall transformation from the base of the robot to the end-effector.
        - Each individual transformation matrix is computed using the DH convention, without applying any correction factors.
    """
    # Initialize the total transformation matrix as an identity matrix
    T = np.eye(4)

    # Compute the total transformation matrix
    for i in range(6):
        T_i = dh_matrix(joint_angles[i], a[i], d[i], alpha[i])
        T = T @ T_i  # Matrix multiplication

    return T

def pose_vector_to_tf_matrix(params: np.ndarray) -> np.ndarray:
    """
    Creates a 4x4 transformation matrix from a vector of position and rotation.

    This function takes a 6D vector representing position and rotation,
    and constructs a 4x4 homogeneous transformation matrix.

    Parameters:
        params (np.ndarray): A 6D vector in the form [tx, ty, tz, rx, ry, rz]
            where [tx, ty, tz] is the translation (in any unit)
            and [rx, ry, rz] is the rotation (in radians)

    Returns:
        np.ndarray: A 4x4 homogeneous transformation matrix

    Notes:
        - The function uses scipy.spatial.transform.Rotation for rotation calculations
        - The rotation is applied using the xyz convention (rotations about fixed axes)
        - The returned matrix is in the form:
          [R R R tx]
          [R R R ty]
          [R R R tz]
          [0 0 0  1]
          where R represents the 3x3 rotation matrix and [tx, ty, tz] is the translation
    """
    # Split the vector into translation and rotation
    tx, ty, tz = params[:3]
    rx, ry, rz = params[3:]
    
    # Create rotation matrix (in radians)
    rotation_matrix = R.from_rotvec([rx, ry, rz]).as_matrix()
    
    # Create 4x4 transformation matrix
    transformation_matrix = np.eye(4)
    transformation_matrix[:3, :3] = rotation_matrix  # Place rotation matrix
    transformation_matrix[:3, 3] = [tx, ty, tz]  # Place translation vector
    
    return transformation_matrix

def tf_matrix_to_pose_vector(transformation_matrix: np.ndarray) -> np.ndarray:
    """
    Converts a 4x4 transformation matrix into a 6D vector representing position and rotation.

    This function takes a 4x4 homogeneous transformation matrix and extracts
    the translation and rotation information to construct a 6D vector.

    Parameters:
        transformation_matrix (np.ndarray): A 4x4 homogeneous transformation matrix

    Returns:
        np.ndarray: A 6D vector in the form [tx, ty, tz, rx, ry, rz]
            where [tx, ty, tz] is the translation (in any unit)
            and [rx, ry, rz] is the rotation (in radians)

    Notes:
        - The rotation is computed using the rotation matrix extracted from the transformation matrix.
        - The rotation vector is derived using the rotation matrix to represent rotations about the fixed axes.
    """
    # Extract translation vector from the transformation matrix
    tx, ty, tz = transformation_matrix[:3, 3]

    # Extract rotation matrix
    rotation_matrix = transformation_matrix[:3, :3]
    
    # Calculate rotation vector from the rotation matrix
    rotation = R.from_matrix(rotation_matrix)
    rx, ry, rz = rotation.as_rotvec()

    # Construct and return the 6D pose vector
    return np.array([tx, ty, tz, rx, ry, rz])

def decompose_tf_matrices(T_list: list) -> tuple:
    """
    Decomposes a list of 4x4 transformation matrices into their rotational and translational components.

    This function takes a list of homogeneous transformation matrices and separates each matrix into its
    corresponding rotation matrix and translation vector.

    Parameters:
        T_list (list): A list of 4x4 homogeneous transformation matrices.

    Returns:
        tuple: A tuple containing:
            - R_list (list): A list of 3x3 rotation matrices.
            - t_list (list): A list of 3x1 translation vectors.

    Notes:
        - Each transformation matrix is expected to be in the form:
          [[R, t],
           [0, 1]]
          where R is the rotation matrix and t is the translation vector.
        - The function reshapes the translation vector into a 3x1 format for consistency.
    """
    R_list = []  # List to store rotation matrices
    t_list = []  # List to store translation vectors

    # Loop through each transformation matrix in the provided list
    for T in T_list:
        R_list.append(T[:3, :3])    # Extract and append the rotation matrix (3x3)
        t_list.append(T[:3, 3].reshape(3, 1))  # Extract and append the translation vector (3x1)

    return R_list, t_list  # Return the lists of rotation matrices and translation vectors

def invert_tf_matrices(T_list: list) -> list:
    """
    Inverts a list of 4x4 transformation matrices.

    This function takes a list of homogeneous transformation matrices and computes their inverses.

    Parameters:
        T_list (list): A list of 4x4 homogeneous transformation matrices.

    Returns:
        list: A list containing the inverted 4x4 transformation matrices.

    Notes:
        - Each transformation matrix is expected to be in the form:
          [[R, t],
           [0, 1]]
          where R is the rotation matrix and t is the translation vector.
        - The inversion of a transformation matrix is computed using NumPy's linear algebra module.
    """
    T_inv_list = []  # List to store inverted transformation matrices

    # Loop through each transformation matrix in the provided list
    for T in T_list:
        T_inv = np.linalg.inv(T)  # Compute the inverse of the transformation matrix
        T_inv_list.append(T_inv)  # Append the inverted matrix to the list

    return T_inv_list  # Return the list of inverted transformation matrices

def batch_convert_poses_to_matrices(input_folder: str, output_folder: str) -> None:
    """
    Processes all position files in the input folder and saves them as transformation matrices.

    This function reads all .npy files containing position data [x, y, z, rx, ry, rz] from the input folder,
    converts them to transformation matrices, and saves the results in the output folder.

    Parameters:
        input_folder (str): Path to the folder containing input .npy files with position data.
        output_folder (str): Path to the folder where output transformation matrices will be saved.

    Returns:
        None

    Notes:
        - Input files should be in .npy format and contain arrays of shape (6,) representing [x, y, z, rx, ry, rz].
        - Output files will be named 'pose{XX}_tf.npy' where XX is a zero-padded two-digit number.
        - This function relies on the pose_vector_to_tf_matrix() function to convert position vectors to matrices.
        - The function prints a message for each successfully saved transformation matrix.
    """
    # Get a list of all .npy files in the input folder
    input_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.npy')])

    for i, input_file in enumerate(input_files):
        input_path = os.path.join(input_folder, input_file)
        
        # Load position and rotation vector from .npy file
        params = np.load(input_path)
        
        # Convert to transformation matrix
        T = pose_vector_to_tf_matrix(params)
        
        # Create output filename
        output_file = f'pose{i:02d}_tf.npy'
        output_path = os.path.join(output_folder, output_file)
        
        # Save transformation matrix
        np.save(output_path, T)
        print(f'Saved transformation matrix to {output_path}')

def load_npy_data(folder: str) -> List[np.ndarray]:
    """
    Loads all .npy files from a specified folder and stores them as a list of numpy arrays.

    This function reads all .npy files in the given folder and returns their contents as a list.
    It can handle various types of data, including transformation matrices and joint angle vectors.

    Parameters:
        folder (str): Path to the folder containing .npy files.

    Returns:
        List[np.ndarray]: A list of numpy arrays, each representing the content of a .npy file.

    Raises:
        FileNotFoundError: If the specified folder does not exist.
        ValueError: If a .npy file cannot be loaded.

    Notes:
        - Files are sorted alphabetically before loading.
        - Each .npy file is expected to contain a single numpy array of any shape.
        - Non-.npy files in the folder are ignored.
    """
    try:
        # Get a sorted list of all .npy files in the folder
        npy_files = sorted([f for f in os.listdir(folder) if f.endswith('.npy')])
        
        # Initialize a list to store data
        data_list = []
        
        # Load individual files and add them to the list
        for file in npy_files:
            file_path = os.path.join(folder, file)
            try:
                data = np.load(file_path)
                data_list.append(data)
            except Exception as e:
                raise ValueError(f"Error loading file {file}: {str(e)}")
        
        return data_list

    except FileNotFoundError:
        raise FileNotFoundError(f"The folder {folder} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while processing the folder {folder}: {str(e)}")

def calculate_error_between_matrices(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
    """
    Computes the error vector (translational and rotational errors) between two transformation matrices.

    This function takes two 4x4 homogeneous transformation matrices and calculates
    the difference in their translation and rotation components.

    Parameters:
        mat1 (np.ndarray): The first 4x4 transformation matrix.
        mat2 (np.ndarray): The second 4x4 transformation matrix.

    Returns:
        np.ndarray: An error vector in the form [tx_error, ty_error, tz_error, rx_error, ry_error, rz_error],
            where tx, ty, tz are the translational errors and rx, ry, rz are the rotational errors (in radians).

    Notes:
        - The translational error is calculated as the difference between the translation components of the matrices.
        - The rotational error is calculated by converting the rotation matrices to rotation vectors and finding their difference.
    """
    # Extracting translations from both matrices
    translation1 = mat1[:3, 3]
    translation2 = mat2[:3, 3]
    
    # Calculate translational error (difference in translations)
    translation_error = translation1 - translation2
    
    # Extracting rotation matrices from both matrices
    rotation_matrix1 = mat1[:3, :3]
    rotation_matrix2 = mat2[:3, :3]
    
    # Convert rotation matrices to rotation vectors
    rot_vec1 = R.from_matrix(rotation_matrix1).as_rotvec(degrees=False)
    rot_vec2 = R.from_matrix(rotation_matrix2).as_rotvec(degrees=False)
    
    # Calculate rotational error
    rotation_error = rot_vec1 - rot_vec2
    
    # Combine translational and rotational errors into a single vector
    error_vector = np.concatenate([translation_error, rotation_error])
    
    return error_vector

def extract_joint_angles_from_txt(filename: str) -> np.ndarray:
    """
    Reads joint angles from a text file.

    This function opens a text file and reads a single line containing joint angles
    in the format [angle1, angle2, angle3, angle4, angle5, angle6].

    Parameters:
        filename (str): Path to the text file containing joint angles.

    Returns:
        np.ndarray: An array of 6 float values representing joint angles in radians.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file format is incorrect or cannot be parsed.

    Notes:
        - The file should contain a single line with 6 comma-separated values.
        - Values in the file should already be in radians.
        - The function assumes the angles are enclosed in square brackets.
    """
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()  # Read first line and remove whitespace
            # Remove square brackets and split the line by comma
            angles = line.strip('[]').split(',')
            # Convert values from string to float (already in radians)
            joint_angles = np.array([float(angle) for angle in angles])
        return joint_angles
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} was not found.")
    except ValueError as e:
        raise ValueError(f"Error parsing the file {filename}: {str(e)}")

def read_position_from_txt(filename: str) -> np.ndarray:
    """
    Reads position and orientation data from a text file.

    This function opens a text file and reads a single line containing
    position and orientation data in the format [tx, ty, tz, rx, ry, rz].

    Parameters:
        filename (str): Path to the text file containing position and orientation data.

    Returns:
        np.ndarray: An array of 6 float values representing position (in units used in the file)
                    and orientation (in radians) [tx, ty, tz, rx, ry, rz].

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file format is incorrect or cannot be parsed.

    Notes:
        - The file should contain a single line with 6 comma-separated values.
        - The first three values (tx, ty, tz) represent translation.
        - The last three values (rx, ry, rz) represent rotation in radians.
        - The function assumes the values are enclosed in square brackets.
    """
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()  # Read first line and remove whitespace
            # Remove square brackets and split the line by comma
            coordinates = line.strip('[]').split(',')
            # Convert values from string to float
            coordinate_xyzr = np.array([float(coordinate) for coordinate in coordinates])
        return coordinate_xyzr
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} was not found.")
    except ValueError as e:
        raise ValueError(f"Error parsing the file {filename}: {str(e)}")

def check_robot_connection_rb(robot: RobotInterface) -> bool:
    try:
        state = robot.isConnected()
        return state
    except Exception as e:
        print(f"Chyba při připojení k robotu: {e}")
        return False

def check_robot_connection(ip_address: str) -> bool:
    try:
        rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)
        state = rtde_r.isConnected()
        rtde_r.disconnect()
        return state
    except Exception as e:
        print(f"Chyba při připojení k robotu: {e}")
        return False

def enable_digital_output_rb(robot: RobotInterface, output_id: int) -> bool:
    """ Zapne digitální výstup na UR robotu a vrátí jeho stav. """
    try:
        robot.setStandardDigitalOutput(output_id, True)
        time.sleep(0.1)  # Počkáme, aby se výstup správně nastavil

        state = robot.getStandardDigitalOutput(output_id)

        return state

    except Exception as e:
        return False  # Pokud nastane chyba, vrátíme False jako indikaci neúspěchu

def enable_digital_output(ip_address: str, output_id: int) -> bool:
    """ Zapne digitální výstup na UR robotu a vrátí jeho stav. """
    try:
        rtde_IO = rtde_io.RTDEIOInterface(ip_address)
        rtde_IO.setStandardDigitalOut(output_id, True)
        time.sleep(0.1)  # Počkáme, aby se výstup správně nastavil
        rtde_IO.disconnect()

        rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)
        state = rtde_r.getDigitalOutState(output_id)
        rtde_r.disconnect()

        return state

    except Exception as e:
        return False  # Pokud nastane chyba, vrátíme False jako indikaci neúspěchu

def disable_digital_output_rb(robot: RobotInterface, output_id: int) -> bool:
    """ Vypne digitální výstup na UR robotu a vrátí jeho stav. """
    try:
        robot.setStandardDigitalOutput(output_id, False)
        time.sleep(0.1)

        state = robot.getStandardDigitalOutput(output_id)

        return state

    except Exception:
        return True  # Pokud nastane chyba, vrátíme True jako indikaci, že výstup není LOW

def disable_digital_output(ip_address: str, output_id: int) -> bool:
    """ Vypne digitální výstup na UR robotu a vrátí jeho stav. """
    try:
        rtde_IO = rtde_io.RTDEIOInterface(ip_address)
        rtde_IO.setStandardDigitalOut(output_id, False)
        time.sleep(0.1)
        rtde_IO.disconnect()

        rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)
        state = rtde_r.getDigitalOutState(output_id)
        rtde_r.disconnect()

        return state

    except Exception:
        return True  # Pokud nastane chyba, vrátíme True jako indikaci, že výstup není LOW

def connect_to_camera(exist_camera) -> pylon.InstantCamera | None:
   """
   Connects to the first available Basler camera and loads UserSet1 configuration.

   Returns:
       pylon.InstantCamera | None: Initialized camera object if connection successful,
                                  None if connection fails.

   Raises:
       RuntimeError: If no camera is found.
       Exception: For other camera connection or configuration errors.
   """
   try:
       if exist_camera:
           del exist_camera
            
       # Get the transport layer factory
       tl_factory = pylon.TlFactory.GetInstance()
       
       # Look for available devices
       devices = tl_factory.EnumerateDevices()
       if not devices:
           raise RuntimeError("No camera found.")
           
       # Create and open camera object
       camera = pylon.InstantCamera(tl_factory.CreateFirstDevice())
       camera.Open()
       # Load user-defined camera settings (configured via Pylon Viewer)
       camera.UserSetSelector.SetValue("UserSet1")
       camera.UserSetLoad.Execute()
       camera.Close()
       
       return camera
       
   except Exception as e:
       print(f"Error connecting to camera: {e}")
       return None

def save_calibration_results_yaml(
    file_path: str,
    camera_matrix: np.ndarray,
    dist_coeffs: np.ndarray,
    X_matrix: np.ndarray,
    position_vector: np.ndarray,
    config: int,
    method: str
) -> Tuple[bool, str]:
    """
    Saves calibration results to a YAML file.

    Args:
        file_path (str): Path to the YAML file.
        camera_matrix (np.ndarray): Camera calibration matrix.
        dist_coeffs (np.ndarray): Distortion coefficients.
        X_matrix (np.ndarray): Transformation matrix (camera to base/gripper).
        position_vector (np.ndarray): Pose vector [tx, ty, tz, rx, ry, rz].
        config (int): Calibration configuration (e.g., Eye-in-Hand or Eye-to-Hand).
        method (str): Calibration method used.

    Returns:
        Tuple (bool, str): 
            - `True` if the file was successfully saved, otherwise `False`.
            - Message indicating success or the encountered error.
    """
    try:
        # Format data into a structured dictionary
        data = {
            "camera_matrix": [row.tolist() for row in camera_matrix],
            "dist_coeffs": [dist_coeffs.ravel().tolist()],  
            "X_matrix": [row.tolist() for row in X_matrix],
            "position_vector": [position_vector.ravel().tolist()],
            "calibration_config": config,
            "calibration_method": method
        }
        
        # Custom YAML float representation (6 decimal places)
        def custom_representer(dumper, value):
            """Custom YAML representation for float values."""
            return dumper.represent_scalar('tag:yaml.org,2002:float', f'{value:.6f}')
        
        # Register custom float representer
        yaml.add_representer(float, custom_representer)

        # Save data to YAML file
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, default_flow_style=None, allow_unicode=True)

        return True, f"Calibration results saved to {file_path}"

    except Exception as e:
        return False, f"Error saving calibration results: {str(e)}"

def load_calibration_results_yaml(file_path: str) -> Tuple[bool, Optional[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int, str]], str]:
    """
    Loads calibration results from a YAML file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        Tuple (bool, Optional[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int, str]], str): 
            - `True` if the file was successfully loaded, otherwise `False`.
            - A tuple containing:
                - camera_matrix (np.ndarray)
                - dist_coeffs (np.ndarray)
                - X_matrix (np.ndarray)
                - position_vector (np.ndarray)
                - calibration_config (int)
                - calibration_method (str)
            - Message indicating success or the encountered error.
    """
    try:
        # Open and read the YAML file
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # Convert back to NumPy arrays
        camera_matrix = np.array(data["camera_matrix"])
        dist_coeffs = np.array(data["dist_coeffs"])
        X_matrix = np.array(data["X_matrix"])
        position_vector = np.array(data["position_vector"])
        calibration_config = data["calibration_config"]
        calibration_method = data["calibration_method"]

        return True, (camera_matrix, dist_coeffs, X_matrix, position_vector, calibration_config, calibration_method), f"Calibration results loaded from {file_path}"

    except Exception as e:
        return False, None, f"Error loading calibration results: {str(e)}"

def save_dataset(source_folder: str, folder_path: str) -> Tuple[bool, str]:
    """
    Saves the contents of a specified folder as a ZIP archive in the target directory.

    Args:
        source_folder (str): Path to the folder containing the dataset to save.
        folder_path (str): Path to the target directory where the ZIP file will be saved.

    Returns:
        Tuple[bool, str]: 
            - `True` if the dataset was successfully saved, otherwise `False`.
            - Message indicating success or the encountered error.
    """
    if not os.path.exists(source_folder):
        return False, f"Source folder '{source_folder}' does not exist!"

    if not os.path.exists(folder_path):
        return False, f"Target folder '{folder_path}' does not exist!"

    # Generate a unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = os.path.join(folder_path, f"dataset_{timestamp}.zip")

    try:
        # Create ZIP archive
        shutil.make_archive(zip_filename[:-4], 'zip', source_folder)
        return True, f"Dataset saved as ZIP: {zip_filename}"
    
    except Exception as e:
        return False, f"Error saving dataset: {str(e)}"

def extract_zip_dataset(zip_path: str, extract_folder: str) -> Tuple[bool, Optional[str]]:
    """
    Extracts a ZIP file into the specified folder.
    If an error occurs, it returns `False` along with an error message.

    Args:
        zip_path (str): Path to the ZIP file.
        extract_folder (str): Folder where the ZIP contents should be extracted.

    Returns:
        Tuple[bool, Optional[str]]: 
            - `True` if extraction was successful, otherwise `False`.
            - Error message if an error occurs, otherwise `None`.
    """
    try:
        # Ensure the parent directory exists
        os.makedirs(os.path.dirname(extract_folder), exist_ok=True)

        # Ensure the extraction folder exists and is empty
        if os.path.exists(extract_folder):
            for filename in os.listdir(extract_folder):
                file_path = os.path.join(extract_folder, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
        else:
            os.makedirs(extract_folder)

        # Extract ZIP file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)

        return True, None  # Successful extraction

    except Exception as e:
        return False, str(e)  # Return error message

def eye_in_hand_calibration(
    rob_pose_tf_list: List[NDArray[np.float64]], 
    obj_pose_tf_list: List[NDArray[np.float64]], 
    method_str: str, 
    method_map: Dict[str, int]
) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Computes the calibration transformation matrix for an Eye-in-Hand configuration.

    Args:
        rob_pose_tf_list (List[np.ndarray]): List of 4x4 transformation matrices representing 
                                             robot poses (gripper to base).
        obj_pose_tf_list (List[np.ndarray]): List of 4x4 transformation matrices representing 
                                             target poses (object to camera).
        method_str (str): The name of the calibration method to be used.
        method_map (Dict[str, int]): Mapping of method names to OpenCV calibration constants.

    Returns:
        Tuple[np.ndarray, np.ndarray]: 
            - 4x4 transformation matrix (camera to gripper)
            - 1x6 pose vector (translation + rotation in axis-angle representation)
    
    Raises:
        ValueError: If the specified calibration method is not supported.
    """

    # Validate the calibration method
    if method_str not in method_map:
        raise ValueError(f"Unsupported calibration method: {method_str}. "
                         f"Supported methods are: {', '.join(method_map.keys())}")

    calibration_method = method_map[method_str]

    # Decompose transformation matrices of the robot (gripper to base)
    R_grip2base, t_grip2base = decompose_tf_matrices(rob_pose_tf_list)
    # Invert the robot pose transformation matrices and decompose them
    inv_rob_pose_tf_list = invert_tf_matrices(rob_pose_tf_list)
    R_base2grip, t_base2grip = decompose_tf_matrices(inv_rob_pose_tf_list)

    # Decompose transformation matrices of the object
    R_target2cam, t_target2cam = decompose_tf_matrices(obj_pose_tf_list)

    if method_str in ("LI (world)", "SHAH (world)"):
        # Perform Robot-World/Hand-Eye calibration
        R_base2target_W, t_base2target_W, R_grip2cam_W, t_grip2cam_W = cv2.calibrateRobotWorldHandEye(
            R_target2cam, t_target2cam,
            R_base2grip, t_base2grip,
            method=calibration_method # You can choose another method, e.g., 'CALIB_ROBOT_WORLD_HAND_EYE_SHAH', etc.
        )

        T_grip2cam_W = np.eye(4)
        T_grip2cam_W[:3, :3] = np.array(R_grip2cam_W)
        T_grip2cam_W[:3, 3] = np.array(t_grip2cam_W).flatten()
        T_cam2grip = np.linalg.inv(T_grip2cam_W)

    else:
        # Perform Hand-Eye calibration
        R_cam2grip, t_cam2grip = cv2.calibrateHandEye(
            R_grip2base, t_grip2base,
            R_target2cam, t_target2cam,
            method=calibration_method
        )

        # Construct the final transformation matrix
        T_cam2grip = np.eye(4)
        T_cam2grip[:3, :3] = np.array(R_cam2grip)
        T_cam2grip[:3, 3] = np.array(t_cam2grip).flatten()

    # Convert to pose vector
    pose_vector = tf_matrix_to_pose_vector(T_cam2grip)

    return T_cam2grip, pose_vector

def eye_to_hand_calibration(
    rob_pose_tf_list: List[NDArray[np.float64]], 
    obj_pose_tf_list: List[NDArray[np.float64]], 
    method_str: str, 
    method_map: Dict[str, int]
) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Computes the calibration transformation matrix for an Eye-to-Hand configuration.

    Args:
        rob_pose_tf_list (List[np.ndarray]): List of 4x4 transformation matrices representing 
                                             robot poses (base to gripper).
        obj_pose_tf_list (List[np.ndarray]): List of 4x4 transformation matrices representing 
                                             target poses (object to camera).
        method_str (str): The name of the calibration method to be used.
        method_map (Dict[str, int]): Mapping of method names to OpenCV calibration constants.

    Returns:
        Tuple[np.ndarray, np.ndarray]: 
            - 4x4 transformation matrix (camera to base)
            - 1x6 pose vector (translation + rotation in axis-angle representation)
    
    Raises:
        ValueError: If the specified calibration method is not supported.
    """

    # Validate the calibration method
    if method_str not in method_map:
        raise ValueError(f"Unsupported calibration method: {method_str}. "
                         f"Supported methods are: {', '.join(method_map.keys())}")

    calibration_method = method_map[method_str]

    # Invert and decompose transformation matrices of the robot
    inv_rob_pose_tf_list = invert_tf_matrices(rob_pose_tf_list)
    R_base2grip, t_base2grip = decompose_tf_matrices(inv_rob_pose_tf_list)

    # Decompose transformation matrices of the object
    R_target2cam, t_target2cam = decompose_tf_matrices(obj_pose_tf_list)
    inv_obj_pose_tf_list = invert_tf_matrices(obj_pose_tf_list)
    R_cam2target, t_cam2target = decompose_tf_matrices(inv_obj_pose_tf_list)
    

    if calibration_method in (cv2.CALIB_ROBOT_WORLD_HAND_EYE_LI, cv2.CALIB_ROBOT_WORLD_HAND_EYE_SHAH):
        # Perform Robot-World/Hand-Eye calibration
        R_base2cam_W, t_base2cam_W, R_grip2target_W, t_grip2target_W = cv2.calibrateRobotWorldHandEye(
            R_cam2target, t_cam2target,
            R_base2grip, t_base2grip,
            method=calibration_method # You can choose another method, e.g., 'CALIB_ROBOT_WORLD_HAND_EYE_SHAH', etc.
        )

        T_base2cam_W = np.eye(4)
        T_base2cam_W[:3, :3] = np.array(R_base2cam_W)
        T_base2cam_W[:3, 3] = np.array(t_base2cam_W).flatten()
        T_cam2base = np.linalg.inv(T_base2cam_W)

    else:
        # Perform Hand-Eye calibration
        R_cam2base, t_cam2base = cv2.calibrateHandEye(
            R_base2grip, t_base2grip,
            R_target2cam, t_target2cam,
            method=calibration_method
        )

        # Construct the final transformation matrix
        T_cam2base = np.eye(4)
        T_cam2base[:3, :3] = np.array(R_cam2base)
        T_cam2base[:3, 3] = np.array(t_cam2base).flatten()

    # Convert to pose vector
    pose_vector = tf_matrix_to_pose_vector(T_cam2base)

    return T_cam2base, pose_vector

def save_obj_pose_data(directory: str, data: np.ndarray) -> Tuple[Optional[str], Optional[str]]:
    """
    Saves a transformation matrix or other numerical data to a file named pose_tf_XX.npy in the specified directory.

    Args:
        directory (str): Path to the folder where the file should be saved (e.g., "output/robot_pose_tf").
        data (np.ndarray): Data to be saved (e.g., transformation matrix).

    Returns:
        Tuple[Optional[str], Optional[str]]: 
            - Path to the saved file if successful, otherwise None.
            - Error message if saving fails, otherwise None.
    """
    try:
        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Find the lowest available XX number
        existing_files = [f for f in os.listdir(directory) if f.startswith("obj_pose_tf_") and f.endswith(".npy")]
        existing_numbers = sorted(int(f[12:14]) for f in existing_files if f[12:14].isdigit())

        new_number = 0
        while new_number in existing_numbers:
            new_number += 1

        filename = f"obj_pose_tf_{new_number:02d}.npy"
        save_path = os.path.join(directory, filename)

        # Save data using numpy
        np.save(save_path, data)
        return save_path, None  # Success, no error

    except Exception as e:
        return None, str(e)  # Return error message on failure

def calibrate_camera_with_charuco(
    image_folder: str, 
    charuco_detector: cv2.aruco.CharucoDetector, 
    charuco_board: cv2.aruco.CharucoBoard, 
    robot_pose_folder: str, 
    obj_pose_folder: str, 
    num_dist_coeffs: int = 5
) -> Tuple[Union[NDArray[np.float64], None], 
           Union[NDArray[np.float64], None], 
           Union[List[NDArray[np.float64]], None], 
           Union[List[NDArray[np.float64]], None], 
           Union[str, None]]:
    """
    Performs camera calibration using a ChArUco board and processes related data.

    Args:
        image_folder (str): Path to the folder containing calibration images.
        charuco_detector (cv2.aruco.CharucoDetector): ChArUco board detector.
        charuco_board (cv2.aruco.CharucoBoard): ChArUco board configuration.
        robot_pose_folder (str): Path to the folder containing robot pose data.
        obj_pose_folder (str): Path to the folder where object poses will be saved.
        num_dist_coeffs (int, optional): Number of distortion coefficients. Default is 5.

    Returns:
        Tuple[np.ndarray | None, np.ndarray | None, List[np.ndarray] | None, List[np.ndarray] | None, str | None]:
            - camera_matrix: 3x3 camera intrinsic matrix (or None if failed)
            - dist_coeffs: Distortion coefficients (or None if failed)
            - obj_pose_tf_list: List of transformation matrices for object positions (or None if failed)
            - rob_pose_tf_list: List of transformation matrices for robot positions (or None if failed)
            - error_message: Error description if calibration failed, otherwise None
    """

    try:
        # Load all PNG images from the folder
        image_list = [
            cv2.imread(os.path.join(image_folder, file)) 
            for file in os.listdir(image_folder) if file.endswith(".png")
        ]

        if not image_list:
            raise ValueError("No calibration images found in the specified folder.")

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
        dist_coeffs = np.zeros((num_dist_coeffs,), dtype=np.float64)

        # Perform camera calibration
        retval, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.aruco.calibrateCameraCharuco(
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
        # Check if the folder is empty
        save_enabled = not os.listdir(obj_pose_folder)  # True if folder is empty
        obj_pose_tf_list = []
        for tvec, rvec in zip(tvecs, rvecs):
            tvec = tvec.flatten()
            rvec = rvec.flatten()

            # Create pose vector and convert it to a transformation matrix
            pose_vector = np.hstack((tvec, rvec))
            transformation_matrix = pose_vector_to_tf_matrix(pose_vector)

            # Save transformation matrix only if the folder was initially empty
            if save_enabled:
                save_obj_pose_data(obj_pose_folder, transformation_matrix)

            obj_pose_tf_list.append(transformation_matrix)

        # Load robot positions
        rob_pose_tf_list = load_npy_data(robot_pose_folder)
        rob_pose_tf_list = [rob_pose_tf_list[i] for i in valid_indices]

        return camera_matrix, dist_coeffs, obj_pose_tf_list, rob_pose_tf_list  # No error

    except Exception as e:
        raise e # Re-raise the exception for external handling

def rotation_from_vector_to_vector(source: NDArray[np.float64], target: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Creates a rotation matrix that aligns a given source vector with a target vector.

    Args:
        source (np.ndarray): Initial vector that should be rotated.
        target (np.ndarray): Target vector to which the source vector should be aligned.

    Returns:
        np.ndarray: 3x3 rotation matrix.
    """
    # Normalize input vectors
    source = source / np.linalg.norm(source)
    target = target / np.linalg.norm(target)

    # Check if already aligned
    if np.allclose(source, target):
        return np.eye(3)  # Identity matrix, no rotation needed
    if np.allclose(source, -target):
        # If opposite, find perpendicular vector to rotate 180°
        perp_vector = np.array([1, 0, 0]) if not np.allclose(source, [1, 0, 0]) else np.array([0, 1, 0])
        return rotation_from_vector_to_vector(source, perp_vector) @ rotation_from_vector_to_vector(perp_vector, target)

    # Compute the rotation axis (cross product)
    v = np.cross(source, target)
    s = np.linalg.norm(v)
    c = np.dot(source, target)

    # Skew-symmetric cross-product matrix
    vx = np.array([[   0,   -v[2],  v[1]],
                   [ v[2],     0,  -v[0]],
                   [-v[1],  v[0],     0]], dtype=np.float64)

    # Rodrigues' rotation formula
    R = np.eye(3) + vx + np.dot(vx, vx) * ((1 - c) / (s ** 2))

    return R

def generate_points_on_circle(
    num_points: int, radius: float, a: float, source: NDArray[np.float64] = np.array([0, 0, 1])
) -> List[NDArray[np.float64]]:
    """
    Generates a list of points in the format [tx, ty, tz, rx, ry, rz],
    where the points lie on a circle centered at (0,0,0) and their local 
    orientation is aligned with the apex of a cone.

    Args:
        num_points (int): Number of points on the circle.
        radius (float): Radius of the circle. [m]
        a (float): Apex height of the cone. [m]
        source (np.ndarray): Normal vector defining the plane.

    Returns:
        List[np.ndarray]: List of points [tx, ty, tz, rx, ry, rz].
    """
    
    # Ensure source is a unit vector
    source = source / np.linalg.norm(source)

    # Define default plane (XY) and apex
    target = np.array([0, 0, 1], dtype=np.float64)  # Výchozí normála
    apex = source * a  # Vrchol kužele podle `source`

    # Compute rotation matrix to align `target` with `source`
    R = rotation_from_vector_to_vector(target, source)

    points = []

    for i in range(num_points):
        theta = 2 * np.pi * i / num_points
        # Body generované v XY rovině
        p = np.array([radius * np.cos(theta), radius * np.sin(theta), 0], dtype=np.float64)

        # Transformace bodu pomocí rotace
        p_transformed = R @ p  # Rotujeme body kružnice do správné roviny

        # Směrový vektor ke kuželu (po transformaci)
        target_vector = apex - p_transformed
        target_vector = target_vector / np.linalg.norm(target_vector)  # Normalizace

        # Rotace body kružnice tak, aby odpovídaly `source → target_vector`
        R_align = rotation_from_vector_to_vector(source, target_vector)

        # Konverze na Rodriguesův rotační vektor
        rvec, _ = cv2.Rodrigues(R_align)
        rvec = rvec.flatten()

        # Uložení bodu a rotace
        points.append(np.array([p_transformed[0], p_transformed[1], p_transformed[2], rvec[0], rvec[1], rvec[2]], dtype=np.float64))

    return points

# otestovat v2 s výpočtem maximálního úhlu
def generate_points_on_circle_2(
    img_width: int, img_height: int,
    rect_real_width: float, rect_real_height: float,
    rect_pixel_width: int, rect_pixel_height: int,
    rect_x: int, rect_y: int,
    num_points: int, source: NDArray[np.float64] = np.array([0, 0, 1])
) -> List[NDArray[np.float64]]:
    """
    Generates a list of points in the format [tx, ty, tz, rx, ry, rz],
    where the points lie on a circle centered at (0,0,0) and their local 
    orientation is aligned with the apex of a cone.

    Args:
        num_points (int): Number of points on the circle.
        img_width (int): Image width in pixels.
        img_height (int): Image height in pixels.
        rect_real_width (float): Rectangle width in meters.
        rect_real_height (float): Rectangle height in meters.
        rect_pixel_width (int): Rectangle width in pixels.
        rect_pixel_height (int): Rectangle height in pixels.
        rect_x (int): X-coordinate of the rectangle's top-left corner in pixels.
        rect_y (int): Y-coordinate of the rectangle's top-left corner in pixels.
        source (np.ndarray): Normal vector defining the plane.

    Returns:
        List[np.ndarray]: List of points [tx, ty, tz, rx, ry, rz].
    """
    
    # Ensure source is a unit vector
    source = source / np.linalg.norm(source)

    # Compute scaling factor (meters per pixel)
    scale_x = rect_real_width / rect_pixel_width
    scale_y = rect_real_height / rect_pixel_height

    # Compute maximum allowed movement in pixels
    max_right_pixels = img_width - (rect_x + rect_pixel_width)  # Pixels remaining on the right
    max_top_pixels = rect_y  # Pixels remaining at the top

    # Convert movement limits to meters
    max_shift_x = max_right_pixels * scale_x
    max_shift_y = max_top_pixels * scale_y
    radius = min(max_shift_x, max_shift_y)

    # Define default plane (XY) and apex
    target = np.array([0, 0, 1], dtype=np.float64)  # Výchozí normála
    apex = source * (radius*1.5)  # Vrchol kužele podle `source`

    # Compute rotation matrix to align `target` with `source`
    R = rotation_from_vector_to_vector(target, source)

    points = []

    for i in range(num_points):
        theta = 2 * np.pi * i / num_points
        # Body generované v XY rovině
        p = np.array([radius * np.cos(theta), radius * np.sin(theta), 0], dtype=np.float64)

        # Transformace bodu pomocí rotace
        p_transformed = R @ p  # Rotujeme body kružnice do správné roviny

        # Směrový vektor ke kuželu (po transformaci)
        target_vector = apex - p_transformed
        target_vector = target_vector / np.linalg.norm(target_vector)  # Normalizace

        # Rotace body kružnice tak, aby odpovídaly `source → target_vector`
        R_align = rotation_from_vector_to_vector(source, target_vector)

        # Konverze na Rodriguesův rotační vektor
        rvec, _ = cv2.Rodrigues(R_align)
        rvec = rvec.flatten()

        # Uložení bodu a rotace
        points.append(np.array([p_transformed[0], p_transformed[1], p_transformed[2], rvec[0], rvec[1], rvec[2]], dtype=np.float64))

    return points

def save_pose_data(directory: str, data: np.ndarray) -> None:
    """
    Saves a transformation matrix or other numerical data to a file named pose_tf_XX.npy in the specified directory.

    Args:
        directory (str): Path to the folder where the file should be saved (e.g., "output/robot_pose_tf").
        data (np.ndarray): Data to be saved (e.g., transformation matrix).

    Raises:
        ValueError: If the provided data is invalid.
        IOError: If the file saving fails.
    """
    # Validate input data
    if not isinstance(data, np.ndarray) or data.size == 0:
        raise ValueError("Invalid data: Must be a non-empty numpy array.")

    try:
        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Find the lowest available XX number
        existing_files = [f for f in os.listdir(directory) if f.startswith("pose_tf_") and f.endswith(".npy")]
        existing_numbers = sorted(int(f[8:10]) for f in existing_files if f[8:10].isdigit()) if existing_files else []

        new_number = 0
        while new_number in existing_numbers:
            new_number += 1

        filename = f"pose_tf_{new_number:02d}.npy"
        save_path = os.path.join(directory, filename)

        # Save data using numpy
        np.save(save_path, data)

    except Exception as e:
        raise IOError(f"Failed to save pose data: {str(e)}")

def save_joints_data(directory: str, data: np.ndarray) -> None:
    """
    Saves joint angle data to a file named joints_data_XX.npy in the specified directory.

    Args:
        directory (str): Path to the folder where the file should be saved (e.g., "output/robot_joints").
        data (np.ndarray): Joint angle data to be saved (e.g., a 1D or 2D array of joint angles).

    Raises:
        ValueError: If the provided data is invalid.
        IOError: If the file saving fails.
    """
    # Validate input data
    if not isinstance(data, np.ndarray) or data.size == 0:
        raise ValueError("Invalid data: Must be a non-empty numpy array.")

    try:
        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Find the lowest available XX number
        existing_files = [f for f in os.listdir(directory) if f.startswith("joints_data_") and f.endswith(".npy")]
        existing_numbers = sorted(int(f[12:14]) for f in existing_files if f[12:14].isdigit()) if existing_files else []

        new_number = 0
        while new_number in existing_numbers:
            new_number += 1

        filename = f"joints_data_{new_number:02d}.npy"
        save_path = os.path.join(directory, filename)

        # Save joint data using numpy
        np.save(save_path, data)

    except Exception as e:
        raise IOError(f"Failed to save joint data: {str(e)}")

def enable_freedrive_mode_rb(robot: RobotInterface) -> Tuple[bool, str]:
    """
    Activates the robot's freedrive mode, allowing manual movement without resistance.

    Args:
        ip_address (str): IP address of the robot.

    Returns:
        Tuple[bool, str]: 
            - `True` if freedrive mode was successfully activated, otherwise `False`.
            - Status message.
    """
    try:
        status = robot.freedriveMode()

        if status == 7:  # Ensures all necessary status flags are set
            return True, "Freedrive mode activated."
        else:
            return False, f"Failed to activate freedrive mode. {status}"

    except Exception as e:
        return False, f"Error activating freedrive mode: {str(e)}"

def enable_freedrive_mode(ip_address: str) -> Tuple[bool, str]:
    """
    Activates the robot's freedrive mode, allowing manual movement without resistance.

    Args:
        ip_address (str): IP address of the robot.

    Returns:
        Tuple[bool, str]: 
            - `True` if freedrive mode was successfully activated, otherwise `False`.
            - Status message.
    """
    try:
        rtde_c = rtde_control.RTDEControlInterface(ip_address)
        rtde_c.freedriveMode()
        time.sleep(0.1)

        status = rtde_c.getRobotStatus()
        rtde_c.disconnect()

        if status == 7:  # Ensures all necessary status flags are set
            return True, "Freedrive mode activated."
        else:
            return False, "Failed to activate freedrive mode."

    except Exception as e:
        return False, f"Error activating freedrive mode: {str(e)}"

def disable_freedrive_mode_rb(robot: RobotInterface) -> Tuple[bool, str]:
    """
    Deactivates freedrive mode and switches the robot back to the standard controlled mode.

    Args:
        ip_address (str): IP address of the robot.

    Returns:
        Tuple[bool, str]: 
            - `True` if freedrive mode was successfully deactivated, otherwise `False`.
            - Status message.
    """
    try:
        status = robot.endFreedriveMode()

        if status != 7:  # Ensures the robot is no longer in freedrive mode
            return True, "Freedrive mode deactivated."
        else:
            return False, "Failed to deactivate freedrive mode."

    except Exception as e:
        return False, f"Error deactivating freedrive mode: {str(e)}"

def disable_freedrive_mode(ip_address: str) -> Tuple[bool, str]:
    """
    Deactivates freedrive mode and switches the robot back to the standard controlled mode.

    Args:
        ip_address (str): IP address of the robot.

    Returns:
        Tuple[bool, str]: 
            - `True` if freedrive mode was successfully deactivated, otherwise `False`.
            - Status message.
    """
    try:
        rtde_c = rtde_control.RTDEControlInterface(ip_address)
        rtde_c.endFreedriveMode() 
        time.sleep(0.1)

        status = rtde_c.getRobotStatus()
        rtde_c.disconnect()

        if status != 7:  # Ensures the robot is no longer in freedrive mode
            return True, "Freedrive mode deactivated."
        else:
            return False, "Failed to deactivate freedrive mode."

    except Exception as e:
        return False, f"Error deactivating freedrive mode: {str(e)}"

def generate_plane_points(
    img_width: int, img_height: int,
    rect_real_width: float, rect_real_height: float,
    rect_pixel_width: int, rect_pixel_height: int,
    rect_x: int, rect_y: int,
    source: NDArray[np.float64]  # Normal vector of the target plane (must be one of the six predefined)
) -> List[NDArray[np.float64]]:
    """
    Generates 8 valid positions where the camera can move while keeping the rectangle visible.

    Args:
        img_width (int): Image width in pixels.
        img_height (int): Image height in pixels.
        rect_real_width (float): Rectangle width in meters.
        rect_real_height (float): Rectangle height in meters.
        rect_pixel_width (int): Rectangle width in pixels.
        rect_pixel_height (int): Rectangle height in pixels.
        rect_x (int): X-coordinate of the rectangle's top-left corner in pixels.
        rect_y (int): Y-coordinate of the rectangle's top-left corner in pixels.
        source (np.ndarray): Normal vector defining the plane. Must be one of:
                             [0,0,1], [0,0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]

    Returns:
        List[np.ndarray]: 8 points [tx, ty, tz, rx, ry, rz] around the initial camera position.
    """

    # Ensure source is a valid predefined normal vector
    valid_normals = [
        np.array([0, 0, 1]), np.array([0, 0, -1]),
        np.array([0, 1, 0]), np.array([0, -1, 0]),
        np.array([1, 0, 0]), np.array([-1, 0, 0])
    ]
    if not any(np.array_equal(source, valid) for valid in valid_normals):
        raise ValueError("Invalid source vector. Must be one of [0,0,1], [0,0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]")

    # Compute scaling factor (meters per pixel)
    scale_x = rect_real_width / rect_pixel_width
    scale_y = rect_real_height / rect_pixel_height

    # Compute maximum allowed movement in pixels
    max_right_pixels = img_width - (rect_x + rect_pixel_width)  # Pixels remaining on the right
    max_top_pixels = rect_y  # Pixels remaining at the top

    # Convert movement limits to meters
    max_shift_x = max_right_pixels * scale_x
    max_shift_y = max_top_pixels * scale_y

    # Define movements in XY plane (default)
    base_offsets = [
        [-max_shift_x, -max_shift_y],  # Bottom-left
        [max_shift_x, -max_shift_y],   # Bottom-right
        [-max_shift_x, max_shift_y],   # Top-left
        [max_shift_x, max_shift_y],    # Top-right
        [0, -max_shift_y],             # Center-bottom
        [0, max_shift_y],              # Center-top
        [-max_shift_x, 0],             # Center-left
        [max_shift_x, 0]               # Center-right
    ]

    # Adjust coordinate mapping based on the normal vector
    if np.array_equal(source, [0, 0, 1]) or np.array_equal(source, [0, 0, -1]):
        # XY plane (Z is constant)
        offsets = [[x, y, 0] for x, y in base_offsets]
    elif np.array_equal(source, [0, 1, 0]) or np.array_equal(source, [0, -1, 0]):
        # XZ plane (Y is constant)
        offsets = [[x, 0, y] for x, y in base_offsets]
    elif np.array_equal(source, [1, 0, 0]) or np.array_equal(source, [-1, 0, 0]):
        # YZ plane (X is constant)
        offsets = [[0, x, y] for x, y in base_offsets]

    # Generate points with zero rotation
    points = []
    for new_tx, new_ty, new_tz in offsets:
        new_rvec = np.array([0, 0, 0], dtype=np.float64)
        points.append(np.array([new_tx, new_ty, new_tz, new_rvec[0], new_rvec[1], new_rvec[2]], dtype=np.float64))

    return points

def delete_folder(folder_path: str) -> None:
    """
    Deletes a folder and all its contents, ensuring all files and subfolders are writable.

    Args:
        folder_path (str): The path to the folder to be deleted.

    Raises:
        FileNotFoundError: If the folder does not exist.
        PermissionError: If there is an issue with file permissions.
        OSError: If the folder could not be deleted.
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found to be deleted: {folder_path}")

    # Change permissions for all files and subfolders **before** deletion
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.chmod(file_path, stat.S_IWRITE)  # Set file to writable
            except Exception as e:
                raise PermissionError(f"Failed to change file permissions: {file_path}. {e}")

        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.chmod(dir_path, stat.S_IWRITE)  # Set directory to writable
            except Exception as e:
                raise PermissionError(f"Failed to change directory permissions: {dir_path}. {e}")

    try:
        shutil.rmtree(folder_path)  # Now delete everything safely
        print(f"Successfully deleted folder: {folder_path}")

    except PermissionError as e:
        raise PermissionError(f"Permission denied: {folder_path}. {e}")

    except OSError as e:
        raise OSError(f"Error deleting folder: {folder_path}. {e}")
    
def generate_pick_poses_z_down(pick_tf: np.ndarray) -> list[np.ndarray]:
    """
    Generates 4 pick poses with Z axis flipped downward and rotated around local Z axis.

    Args:
        pick_tf (np.ndarray): 4x4 transformation matrix of the detected object.

    Returns:
        List[np.ndarray]: 4 transformation matrices [Z flipped + 0°, 90°, 180°, 270° around local Z].
    """
    # 180° rotace kolem X → převrátí Z osu dolů
    R_x_180 = np.array([
        [1,  0,  0],
        [0, -1,  0],
        [0,  0, -1]
    ])

    # Homogenní verze
    R_homogeneous = np.eye(4)
    R_homogeneous[:3, :3] = R_x_180

    # Aplikuj převrácení Z směrem dolů
    base_tf = pick_tf @ R_homogeneous

    # Rotace o 90° kolem Z
    R_z_90 = np.array([
        [0, -1, 0],
        [1,  0, 0],
        [0,  0, 1]
    ])
    Rz_hom = np.eye(4)
    Rz_hom[:3, :3] = R_z_90

    # Generuj 4 otočení kolem lokální Z osy
    poses = []
    for i in range(4):
        Rz_i = np.linalg.matrix_power(Rz_hom, i)
        tf_i = base_tf @ Rz_i
        poses.append(tf_i)

    return poses

def generate_pick_poses(pick_tf: np.ndarray) -> list[np.ndarray]:
    """
    Generates 4 pick poses rotated around local Z axis.

    Args:
        pick_tf (np.ndarray): 4x4 transformation matrix of the detected object.

    Returns:
        List[np.ndarray]: 4 transformation matrices [Z flipped + 0°, 90°, 180°, 270° around local Z].
    """

    base_tf = pick_tf

    # Rotace o 90° kolem Z
    R_z_90 = np.array([
        [0, -1, 0],
        [1,  0, 0],
        [0,  0, 1]
    ])
    Rz_hom = np.eye(4)
    Rz_hom[:3, :3] = R_z_90

    # Generuj 4 otočení kolem lokální Z osy
    poses = []
    for i in range(4):
        Rz_i = np.linalg.matrix_power(Rz_hom, i)
        tf_i = base_tf @ Rz_i
        poses.append(tf_i)

    return poses

def angle_distance_matrix(R1, R2):
    R_diff = R1.T @ R2
    cos_angle = (np.trace(R_diff) - 1) / 2
    angle = np.arccos(np.clip(cos_angle, -1.0, 1.0))
    return np.abs(np.degrees(angle))  # rad → deg

def find_closest_rotation_matrix(reference_matrix, rot_matrices):
    """
    Najde nejpodobnější rotační matici ze seznamu vzhledem k referenční matici.
    Vypisuje různé metriky vzdálenosti.
    """

    ref_rot = reference_matrix[:3, :3]

    print("Referenční matice:")
    print(ref_rot)

    min_distance = float('inf')
    best_index = None

    print("\nPorovnání s ostatními maticemi:")

    for i, matrix in enumerate(rot_matrices):
        current_rot = matrix[:3, :3]

        dist_angle = angle_distance_matrix(ref_rot, current_rot)

        print(f"\nMatice #{i}:")
        print(current_rot)
        print(f"Úhlová vzdál.: {dist_angle:.4f}°")

        # Hlavní metriku vyber zde (např. úhlová vzdálenost)
        distance = dist_angle

        if distance < min_distance:
            min_distance = distance
            best_index = i

    print(f"\nNejbližší matice je #{best_index} s úhlovou vzdáleností {min_distance:.4f}°")
    return rot_matrices[best_index]

def EstimateMarkerPositionFromImage(image: np.ndarray, camera_matrix: np.ndarray, dist_coeffs: np.ndarray, marker_length: float, dictionary_name: int = cv2.aruco.DICT_4X4_250
                                    ) -> Tuple[Union[np.ndarray, None], Union[np.ndarray, None], Union[np.ndarray, None], Union[np.ndarray, None], List[np.ndarray]]:
    """
    Estimates the positions of ArUco markers in a given image.

    Parameters:
    -----------
    - image (np.ndarray) : 
        Input image in which ArUco markers are to be detected.
    - camera_matrix (np.ndarray) :
        Camera intrinsic matrix of shape (3, 3).
    - dist_coeffs (np.ndarray) :
        Distortion coefficients of the camera.
    - marker_length (float) :
        The length of the marker's side in the same units as used in the camera calibration.
    - dictionary_name (int, optional) :
        The predefined ArUco dictionary to use (default: cv2.aruco.DICT_4X4_250).

    Returns:
    --------
    Tuple[Union[np.ndarray, None], Union[np.ndarray, None], Union[np.ndarray, None], Union[np.ndarray, None], List[np.ndarray]]:
        - ids: Detected marker IDs (or None if no markers detected).
        - corners: Corner coordinates of detected markers (or None if no markers detected).
        - tvecs: Translation vectors of detected markers (or None if no markers detected).
        - rvecs: Rotation vectors of detected markers (or None if no markers detected).
        - transf_matrixs: List of 4x4 transformation matrices for each detected marker.
    """
    # Set up the ArUco dictionary
    aruco_dict = cv2.aruco.getPredefinedDictionary(dictionary_name)
    parameters = cv2.aruco.DetectorParameters()  # Detector parameters can be fine-tuned
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    # Detect ArUco markers
    corners, ids, rejected = detector.detectMarkers(image)    
    transf_matrices = []  # Initialize list to store transformation matrices

    if ids is not None:
        # Estimate the pose of each marker
        rvecs, tvecs, obj_points = cv2.aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)
        for i in range(tvecs.shape[0]):
            # Combine translation and rotation vectors into a pose vector
            pose_vector = np.concatenate((tvecs[i], rvecs[i]), axis=None).astype(np.float32)
            # Convert pose vector to a 4x4 transformation matrix
            transf_matrix = pose_vector_to_tf_matrix(pose_vector)
            transf_matrices.append(transf_matrix)
        
    return ids, corners, tvecs, rvecs, transf_matrices

