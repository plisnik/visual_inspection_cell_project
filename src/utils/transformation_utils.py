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





