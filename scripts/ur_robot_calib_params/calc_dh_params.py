import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from scipy.optimize import least_squares
from read_calib_data import load_dh_parameters_from_urcontrol, load_mounting_calibration_parameters
from typing import List
from utils.utilities import fk_with_corrections, load_npy_data
import nevergrad as ng

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

    Args:
        file_path (str): Path to the .conf file (e.g. 'calibration/mounting.conf').
        delta_theta (list): List of delta_theta values (length 6).
        delta_a (list): List of delta_a values (length 6).
        delta_d (list): List of delta_d values (length 6).
        delta_alpha (list): List of delta_alpha values (length 6).
    """
    with open(file_path, 'w') as f:
        f.write("[mounting]\n")
        f.write(f"delta_theta = {format_list(delta_theta)}\n")
        f.write(f"delta_a = {format_list(delta_a)}\n")
        f.write(f"delta_d = {format_list(delta_d)}\n")
        f.write(f"delta_alpha = {format_list(delta_alpha)}\n")


def format_list(values: list) -> str:
    """
    Formats a list of floats into a string suitable for .conf output.

    Args:
        values (list): List of float values.

    Returns:
        str: Formatted string.
    """
    return "[ " + ", ".join(f"{v:.17g}" for v in values) + "]"


def main():
    data_set = "data_sets/basic_data_set"
    urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
    calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'

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
    x0 = np.zeros(24)

    # Optimalization
    result = least_squares(objective_function, x0, args=(thetas_list, a, d, alpha, target_matrices))

    # Resulting correction parameters
    delta_theta_opt = result.x[:6]
    delta_a_opt = result.x[6:12]
    delta_d_opt = result.x[12:18]
    delta_alpha_opt = result.x[18:24]

    print("Optimized delta_a:", delta_a_opt)
    print("Optimized delta_d:", delta_d_opt)
    print("Optimized delta_alpha:", delta_alpha_opt)
    print("Optimized delta_theta:", delta_theta_opt)

    file_path = 'scripts/ur_robot_calib_params/UR_calibration/calibration_experiment.conf'
    save_mounting_config(file_path, delta_theta_opt, delta_a_opt, delta_d_opt, delta_alpha_opt)

    # Loading and processing the calibrATION.conf file
    delta_theta, delta_a, delta_d, delta_alpha = load_mounting_calibration_parameters(calibration_file)
    print("DH Parameters from calibration.conf:")
    print("Delta_a:", delta_a)
    print("Delta_d:", delta_d)
    print("Delta_alpha:", delta_alpha)
    print("Delta_theta:", delta_theta)

    print("Rozdíl:")
    print(delta_theta - delta_theta_opt)
    print(delta_a - delta_a_opt)
    print(delta_d - delta_d_opt)
    print(delta_alpha - delta_alpha_opt)


if __name__ == '__main__':
    sys.exit(main())