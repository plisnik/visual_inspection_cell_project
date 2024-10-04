import configparser
import ast
import numpy as np
from typing import Tuple
import paramiko

def download_sftp_file(sftp_host: str, sftp_port: int, sftp_user: str, sftp_pass: str, remote_file_path: str, local_file_path: str) -> None:
    """
    Downloads a file from an SFTP server to the local computer.

    This function connects to the specified SFTP server, downloads the specified file,
    and saves it to the designated location on the local computer. It prints information
    about the process and any errors that occur.

    Parameters:
        sftp_host (str): The hostname of the SFTP server (IP address or domain name).
        sftp_port (int): The port for the SFTP connection (usually 22).
        sftp_user (str): The username for logging into the SFTP server.
        sftp_pass (str): The password for logging into the SFTP server.
        remote_file_path (str): The path to the file on the remote SFTP server.
        local_file_path (str): The path where the file should be saved on the local computer.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the download process, the function catches the exception
               and prints an error message.

    Notes:
    - The function uses the paramiko library for SFTP operations.
    - After successful file download, the SFTP session and SSH connection are automatically closed.
    """
    try:
        # Set up SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to SFTP server
        ssh.connect(sftp_host, port=sftp_port, username=sftp_user, password=sftp_pass)
        print(f"Connected to {sftp_host} via SFTP")

        # Start SFTP session
        sftp = ssh.open_sftp()

        # Download file from SFTP server
        sftp.get(remote_file_path, local_file_path)
        print(f"File downloaded successfully: {local_file_path}")

        # Close SFTP session and SSH connection
        sftp.close()
        ssh.close()
        print("SFTP session closed")

    except Exception as e:
        print(f"Error: {e}")

def load_dh_parameters_from_urcontrol(file_path: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Reads Denavit-Hartenberg parameters from a urcontrol.conf file.

    This function parses the urcontrol.conf file and extracts the DH parameters
    (a, d, alpha) from the [DH] section.

    Parameters:
        file_path (str): Path to the urcontrol.conf file.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing three numpy arrays:
            - a: Link lengths
            - d: Link offsets
            - alpha: Link twists

    Raises:
        FileNotFoundError: If the specified file does not exist.
        configparser.Error: If there's an error parsing the configuration file.
        KeyError: If the required sections or keys are missing in the file.
        ValueError: If there's an error evaluating the string representations of lists.

    Notes:
        - The function uses configparser with strict=False to handle potential format issues.
        - The DH parameters are expected to be in string representation of Python lists.
    """
    config = configparser.ConfigParser(strict=False)
    config.read(file_path)

    try:
        # Retrieve data from the [DH] section
        a = np.array(ast.literal_eval(config.get('DH', 'a')))
        d = np.array(ast.literal_eval(config.get('DH', 'd')))
        alpha = np.array(ast.literal_eval(config.get('DH', 'alpha')))

        return a, d, alpha
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except configparser.Error as e:
        raise configparser.Error(f"Error parsing the configuration file: {str(e)}")
    except KeyError as e:
        raise KeyError(f"Required section or key not found in {file_path}: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Error evaluating DH parameters in {file_path}: {str(e)}")

def load_mounting_calibration_parameters(file_path: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Reads calibration parameters from a calibration.conf file.

    This function parses the calibration.conf file and extracts the calibration parameters
    (delta_theta, delta_a, delta_d, delta_alpha) from the [mounting] section.

    Parameters:
        file_path (str): Path to the calibration.conf file.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: A tuple containing four numpy arrays:
            - delta_theta: Joint angle corrections.
            - delta_a: Link length corrections.
            - delta_d: Link offset corrections.
            - delta_alpha: Link twist corrections.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        configparser.Error: If there's an error parsing the configuration file.
        KeyError: If the required sections or keys are missing in the file.
        ValueError: If there's an error evaluating the string representations of lists.

    Notes:
        - The function uses configparser with strict=False to handle potential format issues.
        - The calibration parameters are expected to be in string representation of Python lists.
    """
    config = configparser.ConfigParser(strict=False)
    config.read(file_path)

    try:
        # Retrieve data from the [mounting] section
        delta_a = np.array(ast.literal_eval(config.get('mounting', 'delta_a')))
        delta_d = np.array(ast.literal_eval(config.get('mounting', 'delta_d')))
        delta_theta = np.array(ast.literal_eval(config.get('mounting', 'delta_theta')))
        delta_alpha = np.array(ast.literal_eval(config.get('mounting', 'delta_alpha')))

        return delta_theta, delta_a, delta_d, delta_alpha
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except configparser.Error as e:
        raise configparser.Error(f"Error parsing the configuration file: {str(e)}")
    except KeyError as e:
        raise KeyError(f"Required section or key not found in {file_path}: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Error evaluating calibration parameters in {file_path}: {str(e)}")


# Ukázka použití:

urcontrol_file = 'urcontrol.conf'
calibration_file = 'calibration.conf'

# Načtení a zpracování souboru urcontrol.conf
a, d, alpha = load_dh_parameters_from_urcontrol(urcontrol_file)
print("DH Parameters from urcontrol.conf:")
print(f"a = {a}")
print(f"d = {d}")
print(f"alpha = {alpha}")

# Načtení a zpracování souboru calibration.conf
delta_theta, delta_a, delta_d, delta_alpha = load_mounting_calibration_parameters(calibration_file)
print("\nDH Parameters from calibration.conf:")
print(f"delta_a = {delta_a}")
print(f"delta_d = {delta_d}")
print(f"delta_theta = {delta_theta}")
print(f"delta_alpha = {delta_alpha}")
