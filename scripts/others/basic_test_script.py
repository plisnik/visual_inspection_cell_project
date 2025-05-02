import numpy as np
import time
import rtde_control
import rtde_receive
from pypylon import pylon
import cv2
import os
import sys

# Cesty k utilitám
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities, utilities_camera
from utils.robotiq_gripper_control import RobotiqGripper
from ur_robot_calib_params import read_calib_data


# === KONFIGURAČNÍ PROMĚNNÉ ===
ip_address = "192.168.209.135"  # IP adresa robota
light_output_id = 0             # ID digitálního výstupu
light_test = True               # Zapnout světlo?
camera_matrix = None            # Kamerová matice
dist_coeffs = None              # Distortion koeficienty
X_matrix = np.eye(4)            # Hand-eye matice
calib_config_test = 1           # 0 = Eye-in-Hand, 1 = Eye-to-Hand

selected_test = "test_3_to"  # Vyber test (např. "test_1_in", "test_2_to", ...)
# ====================================================================================================


# === DEFINICE TESTOVACÍCH FUNKCÍ ===

def test_1_in(ip_address, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    """
    markery nalepené na kostičkách, markery na podložce
    robot uchopí kostičky a položí na markery na podložce
    """
    print("Spouštím TEST 1 – Eye-in-Hand")

    # === Inicializace RTDE + Gripper ===
    rtde_c = rtde_control.RTDEControlInterface(ip_address)
    gripper = RobotiqGripper(rtde_c)

    # === Detekce markerů ze vstupního snímku ===
    ids, corners, tvecs, rvecs, transf_matrices = utilities.EstimateMarkerPositionFromImage(
        image,
        camera_matrix,
        dist_coeffs,
        marker_length=0.022,
        dictionary_name=cv2.aruco.DICT_4X4_250
    )

    if ids is None or len(ids) == 0:
        print("❌ Žádné markery nebyly detekovány.")
        return

    marker_dict = {int(id_): tf for id_, tf in zip(ids.flatten(), transf_matrices)}
    print(f"🔎 Detekováno markerů: {len(marker_dict)}")

    gripper.activate()
    gripper.set_speed(15)
    gripper.open()

    for i in range(5):
        pick_id = i
        place_id = i + 10

        rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)

        if pick_id in marker_dict and place_id in marker_dict:
            tf_pick_camera = marker_dict[pick_id]
            tf_place_camera = marker_dict[place_id]

            # === PICK část ===
            pick_list = utilities.generate_pick_poses_z_down(tf_pick_camera)
            pick_list_global = [first_robot_tf @ X_matrix @ p for p in pick_list]

            best_pick_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pick_list_global)
            best_pick = utilities.tf_matrix_to_pose_vector(best_pick_tf)

            offset_above = np.eye(4)
            offset_above[:3, 3] = np.array([0, 0, -0.05])
            pick_tf_above = best_pick_tf @ offset_above
            pick_pose_above = utilities.tf_matrix_to_pose_vector(pick_tf_above)

            print(f"👉 PICK {pick_id} → {best_pick}")
            rtde_c.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
            rtde_c.moveL(best_pick, speed=0.1, acceleration=0.15)
            gripper.close()
            rtde_c.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

            # === PLACE část ===
            place_list = utilities.generate_pick_poses_z_down(tf_place_camera)
            place_list_global = [first_robot_tf @ X_matrix @ p for p in place_list]

            best_place_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, place_list_global)

            offset_place = np.eye(4)
            offset_place[:3, 3] = np.array([0, 0, -0.033])
            best_place_tf = best_place_tf @ offset_place
            place_tf_above = best_place_tf @ offset_above

            best_place = utilities.tf_matrix_to_pose_vector(best_place_tf)
            place_pose_above = utilities.tf_matrix_to_pose_vector(place_tf_above)

            print(f"👉 PLACE {pick_id} → {place_id} @ {best_place}")
            rtde_c.moveL(place_pose_above, speed=0.1, acceleration=0.15)
            rtde_c.moveL(best_place, speed=0.1, acceleration=0.15)
            gripper.open()
            rtde_c.moveL(place_pose_above, speed=0.2, acceleration=0.3)

        else:
            print(f"⚠️ Marker {pick_id} nebo {place_id} nebyl detekován – přeskočeno.")

    rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    rtde_c.disconnect()
    print("✅ TEST 1 dokončen.")

def test_1_to(ip_address, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    print("Spouštím TEST 1 – Eye-to-Hand")

    # === Inicializace RTDE + Gripper ===
    rtde_c = rtde_control.RTDEControlInterface(ip_address)
    gripper = RobotiqGripper(rtde_c)

    # === Detekce markerů ze vstupního snímku ===
    ids, corners, tvecs, rvecs, transf_matrices = utilities.EstimateMarkerPositionFromImage(
        image,
        camera_matrix,
        dist_coeffs,
        marker_length=0.022,
        dictionary_name=cv2.aruco.DICT_4X4_250
    )

    if ids is None or len(ids) == 0:
        print("❌ Žádné markery nebyly detekovány.")
        return

    marker_dict = {int(id_): tf for id_, tf in zip(ids.flatten(), transf_matrices)}
    print(f"🔎 Detekováno markerů: {len(marker_dict)}")

    gripper.activate()
    gripper.set_speed(15)
    gripper.open()

    for i in range(5):
        pick_id = i
        place_id = i + 10

        rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)

        if pick_id in marker_dict and place_id in marker_dict:
            tf_pick_camera = marker_dict[pick_id]
            tf_place_camera = marker_dict[place_id]

            # === PICK část ===
            pick_list = utilities.generate_pick_poses_z_down(tf_pick_camera)
            pick_list_global = [X_matrix @ p for p in pick_list]

            best_pick_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pick_list_global)
            best_pick = utilities.tf_matrix_to_pose_vector(best_pick_tf)

            offset_above = np.eye(4)
            offset_above[:3, 3] = np.array([0, 0, -0.05])
            pick_tf_above = best_pick_tf @ offset_above
            pick_pose_above = utilities.tf_matrix_to_pose_vector(pick_tf_above)

            print(f"👉 PICK {pick_id} → {best_pick}")
            rtde_c.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
            rtde_c.moveL(best_pick, speed=0.1, acceleration=0.15)
            gripper.close()
            rtde_c.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

            # === PLACE část ===
            place_list = utilities.generate_pick_poses_z_down(tf_place_camera)
            place_list_global = [X_matrix @ p for p in place_list]

            best_place_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, place_list_global)

            offset_place = np.eye(4)
            offset_place[:3, 3] = np.array([0, 0, -0.033])
            best_place_tf = best_place_tf @ offset_place
            place_tf_above = best_place_tf @ offset_above

            best_place = utilities.tf_matrix_to_pose_vector(best_place_tf)
            place_pose_above = utilities.tf_matrix_to_pose_vector(place_tf_above)

            print(f"👉 PLACE {pick_id} → {place_id} @ {best_place}")
            rtde_c.moveL(place_pose_above, speed=0.1, acceleration=0.15)
            rtde_c.moveL(best_place, speed=0.1, acceleration=0.15)
            gripper.open()
            rtde_c.moveL(place_pose_above, speed=0.2, acceleration=0.3)

        else:
            print(f"⚠️ Marker {pick_id} nebo {place_id} nebyl detekován – přeskočeno.")

    rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    rtde_c.disconnect()
    print("✅ TEST 1 dokončen.")

def test_2_in(ip_address, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    """markery nalepené na kostičkách + forma, kam je uložit"""
    print("Spouštím TEST 2 – Eye-in-Hand (forma)")

    # === Inicializace RTDE + Gripper ===
    rtde_c = rtde_control.RTDEControlInterface(ip_address)
    gripper = RobotiqGripper(rtde_c)

    # === Detekce markerů ze vstupního snímku ===
    ids, corners, tvecs, rvecs, transf_matrices = utilities.EstimateMarkerPositionFromImage(
        image,
        camera_matrix,
        dist_coeffs,
        marker_length=0.022,
        dictionary_name=cv2.aruco.DICT_4X4_250
    )

    if ids is None or len(ids) == 0:
        print("❌ Žádné markery nebyly detekovány.")
        return

    marker_dict = {int(id_): tf for id_, tf in zip(ids.flatten(), transf_matrices)}
    print(f"🔎 Detekováno markerů: {list(marker_dict.keys())}")

    # === Definice offsetů do formy (110 x 110 mm) vůči markeru ID 10 ===
    form_offsets = [
        np.array([-0.055,  0.055, -0.033]),  # levý horní roh
        np.array([ 0.055,  0.055, -0.033]),  # pravý horní roh
        np.array([-0.055, -0.055, -0.033]),  # levý dolní roh
        np.array([ 0.055, -0.055, -0.033]),  # pravý dolní roh
    ]

    # === Aktivace gripperu ===
    gripper.activate()
    gripper.open()

    for i in range(4):
        pick_id = i
        place_id = 10  # forma s markerem ID 10

        rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)

        if pick_id not in marker_dict or place_id not in marker_dict:
            print(f"⚠️ Marker {pick_id} nebo {place_id} nebyl detekován – přeskočeno.")
            continue

        tf_pick_camera = marker_dict[pick_id]
        tf_place_camera = marker_dict[place_id]

        # === PICK část ===
        pick_list = utilities.generate_pick_poses_z_down(tf_pick_camera)
        pick_list_global = [first_robot_tf @ X_matrix @ p for p in pick_list]

        best_pick_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pick_list_global)
        best_pick = utilities.tf_matrix_to_pose_vector(best_pick_tf)

        offset_above = np.eye(4)
        offset_above[:3, 3] = np.array([0, 0, -0.05])  # nad objekt

        pick_tf_above = best_pick_tf @ offset_above
        pick_pose_above = utilities.tf_matrix_to_pose_vector(pick_tf_above)

        print(f"👉 PICK marker {pick_id} @ {best_pick}")
        rtde_c.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
        rtde_c.moveL(best_pick, speed=0.1, acceleration=0.15)
        gripper.close()
        rtde_c.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

        # === PLACE část ===
        place_list = utilities.generate_pick_poses_z_down(tf_place_camera)
        place_list_global = [first_robot_tf @ X_matrix @ p for p in place_list]

        best_place_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, place_list_global)

        # Přičti offset podle pozice ve formě
        offset_position = np.eye(4)
        offset_position[:3, 3] = form_offsets[i]
        best_place_tf = best_place_tf @ offset_position
        place_tf_above = best_place_tf @ offset_above

        best_place = utilities.tf_matrix_to_pose_vector(best_place_tf)
        place_pose_above = utilities.tf_matrix_to_pose_vector(place_tf_above)

        print(f"👉 PLACE marker {pick_id} → pozice {i} na formě: {best_place}")
        rtde_c.moveL(place_pose_above, speed=0.1, acceleration=0.15)
        rtde_c.moveL(best_place, speed=0.1, acceleration=0.15)
        gripper.open()
        rtde_c.moveL(place_pose_above, speed=0.2, acceleration=0.3)

    rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    rtde_c.disconnect()
    print("✅ TEST 2 dokončen.")

def test_2_to(ip_address, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    print("Spouštím TEST 2 – Eye-to-Hand (forma)")

    # === Inicializace RTDE + Gripper ===
    rtde_c = rtde_control.RTDEControlInterface(ip_address)
    gripper = RobotiqGripper(rtde_c)

    # === Detekce markerů ze vstupního snímku ===
    ids, corners, tvecs, rvecs, transf_matrices = utilities.EstimateMarkerPositionFromImage(
        image,
        camera_matrix,
        dist_coeffs,
        marker_length=0.022,
        dictionary_name=cv2.aruco.DICT_4X4_250
    )

    if ids is None or len(ids) == 0:
        print("❌ Žádné markery nebyly detekovány.")
        return

    marker_dict = {int(id_): tf for id_, tf in zip(ids.flatten(), transf_matrices)}
    print(f"🔎 Detekováno markerů: {list(marker_dict.keys())}")

    # === Definice offsetů do formy (110 x 110 mm) vůči markeru ID 10 ===
    form_offsets = [
        np.array([-0.055,  0.055, -0.033]),  # levý horní roh
        np.array([ 0.055,  0.055, -0.033]),  # pravý horní roh
        np.array([-0.055, -0.055, -0.033]),  # levý dolní roh
        np.array([ 0.055, -0.055, -0.033]),  # pravý dolní roh
    ]

    # === Aktivace gripperu ===
    gripper.activate()
    gripper.open()

    for i in range(4):
        pick_id = i
        place_id = 10  # forma s markerem ID 10

        rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)

        if pick_id not in marker_dict or place_id not in marker_dict:
            print(f"⚠️ Marker {pick_id} nebo {place_id} nebyl detekován – přeskočeno.")
            continue

        tf_pick_camera = marker_dict[pick_id]
        tf_place_camera = marker_dict[place_id]

        # === PICK část ===
        pick_list = utilities.generate_pick_poses_z_down(tf_pick_camera)
        pick_list_global = [X_matrix @ p for p in pick_list]

        best_pick_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pick_list_global)
        best_pick = utilities.tf_matrix_to_pose_vector(best_pick_tf)

        offset_above = np.eye(4)
        offset_above[:3, 3] = np.array([0, 0, -0.05])  # nad objekt

        pick_tf_above = best_pick_tf @ offset_above
        pick_pose_above = utilities.tf_matrix_to_pose_vector(pick_tf_above)

        print(f"👉 PICK marker {pick_id} @ {best_pick}")
        rtde_c.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
        rtde_c.moveL(best_pick, speed=0.1, acceleration=0.15)
        gripper.close()
        rtde_c.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

        # === PLACE část ===
        place_list = utilities.generate_pick_poses_z_down(tf_place_camera)
        place_list_global = [X_matrix @ p for p in place_list]

        best_place_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, place_list_global)

        # Přičti offset podle pozice ve formě
        offset_position = np.eye(4)
        offset_position[:3, 3] = form_offsets[i]
        best_place_tf = best_place_tf @ offset_position
        place_tf_above = best_place_tf @ offset_above

        best_place = utilities.tf_matrix_to_pose_vector(best_place_tf)
        place_pose_above = utilities.tf_matrix_to_pose_vector(place_tf_above)

        print(f"👉 PLACE marker {pick_id} → pozice {i} na formě: {best_place}")
        rtde_c.moveL(place_pose_above, speed=0.1, acceleration=0.15)
        rtde_c.moveL(best_place, speed=0.1, acceleration=0.15)
        gripper.open()
        rtde_c.moveL(place_pose_above, speed=0.2, acceleration=0.3)

    rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    rtde_c.disconnect()
    print("✅ TEST 2 dokončen.")

def test_3_in(ip_address, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    """kalibrační podložka a hrot"""
    print("Spouštím TEST 3 – Eye-in-Hand (kalibrační hrot)")

    # === Inicializace RTDE ===
    rtde_c = rtde_control.RTDEControlInterface(ip_address)

    # === Parametry ChArUco desky ===
    square_length = 0.03
    marker_length = 0.022
    board_rows = 6
    board_cols = 8
    board_size = (board_cols, board_rows)

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
    charuco_board = cv2.aruco.CharucoBoard(board_size, square_length, marker_length, aruco_dict)
    charuco_board.setLegacyPattern(True)
    charuco_detector = cv2.aruco.CharucoDetector(charuco_board)

    # === Detekce ChArUco desky ===
    charuco_corners, charuco_ids, _, _ = charuco_detector.detectBoard(image)

    if charuco_ids is None or len(charuco_ids) == 0:
        print("❌ Žádná ChArUco deska nebyla detekována.")
        return

    # Odhad pozice desky vůči kameře
    rvec = np.zeros((3, 1))
    tvec = np.zeros((3, 1))

    retval, rvec, tvec = cv2.aruco.estimatePoseCharucoBoard(
        charuco_corners,
        charuco_ids,
        charuco_board,
        camera_matrix,
        dist_coeffs,
        rvec,
        tvec,
        useExtrinsicGuess=False
    )

    if not retval:
        print("❌ Nepodařilo se spočítat pozici ChArUco desky.")
        return

    # Vytvoření transformační matice z pozice (levý horní roh)
    pose_vector = np.hstack((tvec.flatten(), rvec.flatten()))
    pose_tf = utilities.pose_vector_to_tf_matrix(pose_vector)

    # === Generování cílových pozic na základě detekce ===
    tf_matrix_list = utilities.generate_pick_poses(pose_tf)
    pose_list_global = [first_robot_tf @ X_matrix @ p for p in tf_matrix_list]

    best_pose_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pose_list_global)

    # Offset o 1 cm ve směru Z
    offset_above = np.eye(4)
    offset_above[:3, 3] = np.array([0, 0, -0.01])
    best_pose_tf = best_pose_tf @ offset_above

    best_pose = utilities.tf_matrix_to_pose_vector(best_pose_tf)

    # Pohyb k cíli
    rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    rtde_c.moveL(best_pose, speed=0.1, acceleration=0.15)

    print("✅ Robot namířen na levý horní roh ChArUco desky.")
    time.sleep(2)

    # Návrat do výchozí pozice
    rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    rtde_c.disconnect()
    print("✅ TEST 3 dokončen.")


def test_3_to(ip_address, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    print("Spouštím TEST 3 – Eye-to-Hand")
    
    # === Inicializace RTDE ===
    rtde_c = rtde_control.RTDEControlInterface(ip_address)

    # === Parametry ChArUco desky ===
    square_length = 0.03
    marker_length = 0.022
    board_rows = 6
    board_cols = 8
    board_size = (board_cols, board_rows)

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
    charuco_board = cv2.aruco.CharucoBoard(board_size, square_length, marker_length, aruco_dict)
    charuco_board.setLegacyPattern(True)
    charuco_detector = cv2.aruco.CharucoDetector(charuco_board)

    # === Detekce ChArUco desky ===
    charuco_corners, charuco_ids, _, _ = charuco_detector.detectBoard(image)
    print("deska ok")

    if charuco_ids is None or len(charuco_ids) == 0:
        print("❌ Žádná ChArUco deska nebyla detekována.")
        return

    # Odhad pozice desky vůči kameře
    rvec = np.zeros((3, 1))
    tvec = np.zeros((3, 1))

    retval, rvec, tvec = cv2.aruco.estimatePoseCharucoBoard(
        charuco_corners,
        charuco_ids,
        charuco_board,
        camera_matrix,
        dist_coeffs,
        rvec,
        tvec,
        useExtrinsicGuess=False
    )

    if not retval:
        print("❌ Nepodařilo se spočítat pozici ChArUco desky.")
        return

    # Vytvoření transformační matice z pozice (levý horní roh)
    pose_vector = np.hstack((tvec.flatten(), rvec.flatten()))
    pose_tf = utilities.pose_vector_to_tf_matrix(pose_vector)

    # === Generování cílových pozic na základě detekce ===
    tf_matrix_list = utilities.generate_pick_poses(pose_tf)
    pose_list_global = [X_matrix @ p for p in tf_matrix_list]
    
    best_pose_tf = utilities.find_closest_rotation_matrix(first_TCP_tf, pose_list_global)
    
    # Offset o x cm ve směru Z
    offset_above = np.eye(4)
    offset_above[:3, 3] = np.array([0, 0, -0.01])
    best_pose_tf = best_pose_tf @ offset_above

    best_pose = utilities.tf_matrix_to_pose_vector(best_pose_tf)
    
    # Pohyb k cíli
    rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    rtde_c.moveL(best_pose, speed=0.05, acceleration=0.1)

    print("✅ Robot namířen na levý horní roh ChArUco desky.")
    time.sleep(3)

    # Návrat do výchozí pozice
    rtde_c.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    rtde_c.disconnect()
    print("✅ TEST 3 dokončen.")

# ===========================================================================================================

if __name__ == "__main__":
    try:
        # Načtení kalibračních parametrů
        # Load calibration data using the updated function
        file_path = 'calibration_results/basic_calib_1_to_22_4.yaml'
        success, result, message = utilities.load_calibration_results_yaml(file_path)

        if success:
            # Unpack the returned tuple
            camera_matrix, dist_coeffs, X_matrix, position_vector, calib_config, calib_method = result

        # Inicializace robot, kamera, kalibrace atd.
        urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
        calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'
        a, d, alpha = read_calib_data.load_dh_parameters_from_urcontrol(urcontrol_file)
        delta_theta, delta_a, delta_d, delta_alpha = read_calib_data.load_mounting_calibration_parameters(calibration_file)

        if light_test:
            if not utilities.enable_digital_output(ip_address, light_output_id):
                raise RuntimeError("Failed to turn on light.")
            
        utilities.enable_digital_output(ip_address,1)

        # Initialize camera
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        camera.Open()

        # Load user-defined camera settings (configured via Pylon Viewer)
        camera.UserSetSelector.SetValue("UserSet1")
        camera.UserSetLoad.Execute()
        
        # Try to enable freedrive mode
        success, message = utilities.enable_freedrive_mode(ip_address)
        if success:
            print("Freedrive mode enabled")
        else:
            raise RuntimeError(f"Failed to enable freedrive mode: {message}")
        time.sleep(1)
        
        # Start image acquisition
        camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 

        while camera.IsGrabbing():
            grab_result = camera.RetrieveResult(500, pylon.TimeoutHandling_Return)
            if grab_result.GrabSucceeded():
                frame = grab_result.Array
                frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
                live_frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4, interpolation=cv2.INTER_AREA)
                cv2.imshow("Live Camera", live_frame)

                key = cv2.waitKey(1)
                if key != -1:
                    image = frame.copy()
                    break

        # Cleanup
        grab_result.Release()
        camera.StopGrabbing()
        cv2.destroyAllWindows()

        if image is None:
            raise RuntimeError("Nepodařilo se uložit snímek z kamery.")
        else:
            print("Snímek úspěšně zachycen.")

        # Try to disable freedrive mode
        success, message = utilities.disable_freedrive_mode(ip_address)
        if success:
            print("Freedrive mode disabled")
        else:
            raise RuntimeError(f"Failed to disable freedrive mode: {message}")
        time.sleep(1)

        rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)
        first_TCP = rtde_r.getActualTCPPose()
        first_TCP_tf = utilities.pose_vector_to_tf_matrix(first_TCP)
        first_joints = np.array(rtde_r.getActualQ())
        first_robot_tf = utilities.fk_with_corrections(first_joints, a, d, alpha, delta_theta, delta_a, delta_d, delta_alpha)
        rtde_r.disconnect()

        # Výběr testu podle nastavení
        test_func = globals().get(selected_test)
        if test_func:
            test_func(ip_address, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf)
        else:
            print(f"Neplatný název testu: {selected_test}")

        if light_test:
            utilities.disable_digital_output(ip_address, light_output_id)

        print("✅ Test byl úspěšně dokončen.")

    except Exception as e:
        print(f"❌ Chyba během testu: {e}")
