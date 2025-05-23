import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from scipy.optimize import least_squares
from read_calib_data import load_dh_parameters_from_urcontrol, load_mounting_calibration_parameters
from typing import List
from utils.utilities import fk_with_corrections, load_npy_data

def objective_function(x: np.ndarray, thetas_list: List[np.ndarray], a: np.ndarray, d: np.ndarray, 
                       alpha: np.ndarray, target_matrices: List[np.ndarray]) -> np.ndarray:
    """
    Objective function for optimization of robot calibration parameters.

    This function calculates the error between the forward kinematics (FK) with corrections
    and the target transformation matrices for a set of joint angles.

    Parameters:
        x (np.ndarray): A 1D array of 24 correction parameters 
                        [delta_theta (6), delta_a (6), delta_d (6), delta_alpha (6)]
        thetas_list (List[np.ndarray]): List of joint angle sets, each a 1D array of 6 angles
        a (np.ndarray): Link lengths (DH parameter)
        d (np.ndarray): Link offsets (DH parameter)
        alpha (np.ndarray): Link twists (DH parameter)
        target_matrices (List[np.ndarray]): List of target 4x4 transformation matrices

    Returns:
        np.ndarray: A 1D array of errors (difference between calculated and target matrices)

    Notes:
        - The function uses the fk_with_corrections function from transformation_utils.
        - Each error is calculated as the difference between the target and calculated matrices.
        - The errors for all joint angle sets are concatenated into a single 1D array.
    """
    # Split correction parameters
    delta_theta = x[:6]
    delta_a = x[6:12]
    delta_d = x[12:18]
    delta_alpha = x[18:24]
    
    errors = []
    
    # For each set of angles and target transformation matrix
    for thetas, target_matrix in zip(thetas_list, target_matrices):
        # Calculate TCP with corrections
        T = fk_with_corrections(thetas, a, d, alpha, delta_theta, delta_a, delta_d, delta_alpha)
        
        # Difference between calculated and measured transformation matrix
        error_matrix = target_matrix - T
        errors.append(error_matrix.ravel())  # Flatten to vector
    
    return np.concatenate(errors)

def save_mounting_config(
    file_path: str,
    delta_theta: list,
    delta_a: list,
    delta_d: list,
    delta_alpha: list
    ) -> None:
    """
    Saves mounting correction data to a .conf file in a specific format.

    This function writes robot calibration correction parameters to a configuration file
    in the format expected by the robot control system. The parameters are saved in
    a specific section named [mounting] with proper formatting.

    Parameters:
        file_path (str): Path to the output .conf file (e.g., 'calibration/mounting.conf')
        delta_theta (List[float]): List of angular offset corrections for 6 joints (radians)
        delta_a (List[float]): List of link length corrections for 6 joints (meters)
        delta_d (List[float]): List of link offset corrections for 6 joints (meters)  
        delta_alpha (List[float]): List of link twist corrections for 6 joints (radians)

    Returns:
        None

    Notes:
        - All parameter lists must have exactly 6 elements (one per robot joint)
        - The file format follows the robot manufacturer's configuration standard
        - Values are formatted with high precision (17 significant digits)
    """
    with open(file_path, 'w') as f:
        f.write("[mounting]\n")
        f.write(f"delta_theta = {format_list(delta_theta)}\n")
        f.write(f"delta_a = {format_list(delta_a)}\n")
        f.write(f"delta_d = {format_list(delta_d)}\n")
        f.write(f"delta_alpha = {format_list(delta_alpha)}\n")


def format_list(values: list) -> str:
    """
    Formats a list of float values into a string suitable for configuration file output.

    This function converts a list of numerical values into a properly formatted string
    that can be written to configuration files. The format includes square brackets
    and comma separation with high precision formatting.

    Parameters:
        values (List[float]): List of numerical values to be formatted

    Returns:
        str: Formatted string in the format "[ value1, value2, value3, ... ]"

    Notes:
        - Values are formatted with 17 significant digits for maximum precision
        - The output format is compatible with robot configuration file standards
        - Empty lists will result in "[ ]"
    """
    return "[ " + ", ".join(f"{v:.17g}" for v in values) + "]"


def main():
    """
    Main function for robot calibration parameter optimization.

    This function orchestrates the complete calibration process including loading
    calibration data, optimizing correction parameters using least squares method,
    saving results to configuration file, and comparing with reference values.

    Notes:
        - The function handles the complete calibration workflow
        - File paths are defined as constants at the beginning
        - Results are both saved to file and printed for verification
        - Comparison with reference values helps validate optimization accuracy
    """
    # Configuration file paths
    data_set = "data_sets/basic_data_set"
    urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
    calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'

    # Load calibration data (joint angles and transformation matrices)
    joints_folder = os.path.join(data_set,'joints_pose')
    target_matrices_folder = os.path.join(data_set,'robot_pose_tf')
    
    thetas_list = load_npy_data(joints_folder)
    target_matrices = load_npy_data(target_matrices_folder)

    # Loading and processing the urcontrol.conf file
    a, d, alpha = load_dh_parameters_from_urcontrol(urcontrol_file)
    print("DH Parameters from urcontrol.conf:")
    print(f"a = {a}")
    print(f"d = {d}")
    print(f"alpha = {alpha}")

    # Initial estimate for the correction parameters delta_a, delta_d, delta_alpha, delta_theta
    # All parameters start at zero (no correction
    x0 = np.zeros(24)

    # Optimization using least squares method
    result = least_squares(objective_function, x0, args=(thetas_list, a, d, alpha, target_matrices))

    # Extract resulting correction parameters from optimization result
    delta_theta_opt = result.x[:6]
    delta_a_opt = result.x[6:12]
    delta_d_opt = result.x[12:18]
    delta_alpha_opt = result.x[18:24]

    print("Optimized delta_a:", delta_a_opt)
    print("Optimized delta_d:", delta_d_opt)
    print("Optimized delta_alpha:", delta_alpha_opt)
    print("Optimized delta_theta:", delta_theta_opt)

    # Save optimized parameters to configuration file
    file_path = 'scripts/ur_robot_calib_params/UR_calibration/calibration_experiment_1.conf'
    save_mounting_config(file_path, delta_theta_opt, delta_a_opt, delta_d_opt, delta_alpha_opt)

    # Loading and processing the calibrATION.conf file
    delta_theta, delta_a, delta_d, delta_alpha = load_mounting_calibration_parameters(calibration_file)
    print("DH Parameters from calibration.conf:")
    print("Delta_a:", delta_a)
    print("Delta_d:", delta_d)
    print("Delta_alpha:", delta_alpha)
    print("Delta_theta:", delta_theta)

    # Calculate and display differences between reference and optimized values
    print("Difference:")
    print(delta_theta - delta_theta_opt)
    print(delta_a - delta_a_opt)
    print(delta_d - delta_d_opt)
    print(delta_alpha - delta_alpha_opt)


if __name__ == '__main__':
    sys.exit(main())