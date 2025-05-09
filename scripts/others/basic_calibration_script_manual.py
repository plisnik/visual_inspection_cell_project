import numpy as np
import time
import rtde_control
import rtde_receive
from pypylon import pylon
import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities, utilities_camera
from ur_robot_calib_params import read_calib_data

# ==== PARAMETRY – uprav si podle potřeby ====
ip_address = "192.168.209.135"  # IP adresa robota
light_output_id = 0             # ID digitálního výstupu
light_on = True                 # Zapnout světlo?

calib_config = 0                # 0 = Eye-in-Hand, 1 = Eye-to-Hand

calib_method = "TSAI"
# Mapping method names to cv2 constants
method_map = {
    'TSAI': cv2.CALIB_HAND_EYE_TSAI,
    'PARK': cv2.CALIB_HAND_EYE_PARK,
    'HORAUD': cv2.CALIB_HAND_EYE_HORAUD,
    'ANDREFF': cv2.CALIB_HAND_EYE_ANDREFF,
    'DANIILIDIS': cv2.CALIB_HAND_EYE_DANIILIDIS,
    'LI (world)': cv2.CALIB_ROBOT_WORLD_HAND_EYE_LI,
    'SHAH (world)': cv2.CALIB_ROBOT_WORLD_HAND_EYE_SHAH,
}

data_set = "data_sets/manual_data_set_to_05_09"

image_folder = "cam_pictures"
tcp_pose_folder = "tcp_pose_tf"
joints_pose_folder = "joints_pose"
robot_pose_folder = "robot_pose_tf"
obj_pose_folder = "obj_pose_tf"

# === Parametry ChArUco desky ===
square_length = 0.016
marker_length = 0.012
board_rows = 8
board_cols = 10
# square_length = 0.03
# marker_length = 0.022
# board_rows = 6
# board_cols = 8
board_size = (board_cols, board_rows)
board_width = board_cols * square_length
board_height = board_rows * square_length
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
charuco_board = cv2.aruco.CharucoBoard(board_size, square_length, marker_length, aruco_dict)
charuco_board.setLegacyPattern(True)
charuco_detector = cv2.aruco.CharucoDetector(charuco_board)

# ============================================

def main():
    print("Spouštím manuální kalibraci...")

    # Zapnutí světla
    if light_on:
        if not utilities.enable_digital_output(ip_address, light_output_id):
            raise RuntimeError("Nepodařilo se zapnout světlo")
        
    # Initialize camera
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    camera.Open()

    # Load user-defined camera settings (configured via Pylon Viewer)
    camera.UserSetSelector.SetValue("UserSet1")
    camera.UserSetLoad.Execute()

    # Kalibrační soubory
    urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
    calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'
    a, d, alpha = read_calib_data.load_dh_parameters_from_urcontrol(urcontrol_file)
    delta_theta, delta_a, delta_d, delta_alpha = read_calib_data.load_mounting_calibration_parameters(calibration_file)

    # Kontrola, zda složka už existuje
    if os.path.exists(data_set):
        print(f"Složka '{data_set}' už existuje. Zvol jiný název nebo ji nejdřív smaž.")
        sys.exit(1)  # Ukončí program s chybovým kódem

    # Vytvoření nové složky
    os.makedirs(data_set)

    # Vytvoření podsložek a aktualizace proměnných na jejich plné cesty
    image_path = os.path.join(data_set, image_folder)
    tcp_path = os.path.join(data_set, tcp_pose_folder)
    joints_path = os.path.join(data_set, joints_pose_folder)
    robot_path = os.path.join(data_set, robot_pose_folder)
    obj_path = os.path.join(data_set, obj_pose_folder)
    for folder in [image_path, tcp_path, joints_path, robot_path, obj_path]:
        os.makedirs(folder)

    # Try to enable freedrive mode
    success, message = utilities.enable_freedrive_mode(ip_address)
    if success:
        print("Freedrive mode enabled")
    else:
        raise RuntimeError(f"Failed to enable freedrive mode: {message}")
    time.sleep(1)

    # Start image acquisition
    camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
    manual = True
    while manual:
        if not utilities.enable_freedrive_mode(ip_address)[0]:
            raise RuntimeError("❌ Failed to enable freedrive mode")
    
        while camera.IsGrabbing():
            grab_result = camera.RetrieveResult(500, pylon.TimeoutHandling_Return)
            if grab_result.GrabSucceeded():
                frame = grab_result.Array
                frame_final = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
                # Zmenšení pro zobrazení
                window_image = cv2.resize(frame_final, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)

                # Zobrazení obrazu
                cv2.imshow("Camera", window_image)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('s'):
                    if not utilities.disable_freedrive_mode(ip_address)[0]:
                        raise RuntimeError("❌ Failed to disable freedrive mode")

                    image = frame_final.copy()
                    path = utilities_camera.save_current_frame(image_path, image)
                    print(f"✅ Saved image: {path}")
                    time.sleep(1)
                    rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)
                    tcp_pose = rtde_r.getActualTCPPose()
                    joints = np.array(rtde_r.getActualQ())
                    rtde_r.disconnect()
                    tf = utilities.pose_vector_to_tf_matrix(tcp_pose)
                    robot_fk = utilities.fk_with_corrections(joints, a, d, alpha, delta_theta, delta_a, delta_d, delta_alpha)

                    utilities.save_pose_data(tcp_path, tf)
                    utilities.save_pose_data(robot_path, robot_fk)
                    utilities.save_joints_data(joints_path, joints)

                    break

                elif key == ord('q'):
                    utilities.disable_freedrive_mode(ip_address)
                    grab_result.Release()
                    camera.StopGrabbing()
                    camera.Close()
                    cv2.destroyAllWindows()

                    print("\n✅ Manual capture completed.")
                    manual = False
                    break  

    # Vypnutí světla
    if light_on:
        utilities.disable_digital_output(ip_address, light_output_id)

    print("\nSpouštím výpočet kalibrace...")
    camera_matrix, dist_coeffs, obj_pose_tf_list, rob_pose_tf_list = utilities.calibrate_camera_with_charuco(
        image_path, charuco_detector, charuco_board, robot_path, obj_path
    )

    if calib_config == 0:
        X_matrix, pose_vector = utilities.eye_in_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, calib_method, method_map)
    else:
        X_matrix, pose_vector = utilities.eye_to_hand_calibration(rob_pose_tf_list, obj_pose_tf_list, calib_method, method_map)

    print("\nKalibrace dokončena.")
    print(f"Kamera: {camera_matrix}")
    print(f"koeficienty: {dist_coeffs}")
    print(f"X_matrix:\n{X_matrix}")
    print(f"Pose vector: {pose_vector}")

    file_path = "calibration_results/manual_calib_05_09_to_hand.yaml"
    # Save calibration data using the updated function
    success, message = utilities.save_calibration_results_yaml(
        file_path,
        camera_matrix,
        dist_coeffs,
        X_matrix,
        pose_vector,
        calib_config,
        calib_method
    )

if __name__ == "__main__":
    main()
