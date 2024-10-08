from read_calib_data import download_sftp_file, load_dh_parameters_from_urcontrol, load_mounting_calibration_parameters

# Connection parameters
sftp_host = '192.168.0.11'  # Robot's IP address
sftp_port = 22              # Port for SFTP (typically 22)
sftp_user = 'root'          # Username for SFTP
sftp_pass = 'easybot'       # Password for SFTP
remote_file_path = '/root/.urcontrol/calibration.conf'      # Path to file on server
calibration_file = 'src/UR_calibration/calibration.conf'                       # Path to save file on local PC
remote_file_path_2 = '/root/.urcontrol/urcontrol.conf'      # Path to file on server
urcontrol_file = 'src/UR_calibration/urcontrol.conf'                           # Path to save file on local PC

# Call function to download files
download_sftp_file(sftp_host, sftp_port, sftp_user, sftp_pass, remote_file_path, calibration_file)
download_sftp_file(sftp_host, sftp_port, sftp_user, sftp_pass, remote_file_path_2, urcontrol_file)

## Reading
# Loading and processing the urcontrol.conf file
a, d, alpha = load_dh_parameters_from_urcontrol(urcontrol_file)
print("DH Parameters from urcontrol.conf:")
print(f"a = {a}")
print(f"d = {d}")
print(f"alpha = {alpha}")

# Loading and processing the calibration.conf file
delta_theta, delta_a, delta_d, delta_alpha = load_mounting_calibration_parameters(calibration_file)
print("\nDH Parameters from calibration.conf:")
print(f"delta_a = {delta_a}")
print(f"delta_d = {delta_d}")
print(f"delta_theta = {delta_theta}")
print(f"delta_alpha = {delta_alpha}")
