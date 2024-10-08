import os
import numpy as np
from scipy.spatial.transform import Rotation as R
from typing import List

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



