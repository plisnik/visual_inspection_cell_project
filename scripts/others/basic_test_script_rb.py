import numpy as np
import time
import rtde_control
import rtde_receive
from pypylon import pylon
import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities, robot_interface
from ur_robot_calib_params import read_calib_data

# === CONFIGURATION VARIABLES ===
ip_address = "192.168.209.135"  # IP address of the robot
light_output_id = 0             # Digital Output ID
light_test = True               # Turn on the light?
camera_matrix = None            # Camera matrix
dist_coeffs = None              # Distortion coeficients
X_matrix = np.eye(4)            # Hand-eye X matrix
calib_config_test = 0           # 0 = Eye-in-Hand, 1 = Eye-to-Hand

selected_test = "test_1_in"  # Select a test (e.g.. "test_1_in", "test_2_to", ...)
# ====================================================================================================


# === DEFINITION OF TEST FUNCTIONS ===

def test_1_in(
    robot: robot_interface.RobotInterface,
    image: np.ndarray,
    X_matrix: np.ndarray,
    camera_matrix: np.ndarray,
    dist_coeffs: np.ndarray,
    first_TCP_tf: np.ndarray,
    first_robot_tf: np.ndarray
) -> None:
    """
    Performs calibration test 1 (Eye-in-Hand configuration):
    The robot picks cubes with ArUco markers and places them on corresponding markers on a board.

    Args:
        ip_address (str): IP address of the robot.
        image (np.ndarray): Input image containing ArUco markers.
        X_matrix (np.ndarray): Hand-eye transformation matrix (4x4).
        camera_matrix (np.ndarray): Camera intrinsic matrix.
        dist_coeffs (np.ndarray): Distortion coefficients.
        first_TCP_tf (np.ndarray): Initial TCP pose as a 4x4 transformation matrix.
        first_robot_tf (np.ndarray): Initial robot pose as a 4x4 transformation matrix.

    Returns:
        None

    Raises:
        RuntimeError: If no markers are detected in the image.
    """

    print("Launching TEST 1 – Eye-in-Hand")

    # === Detect markers from input image ===
    ids, corners, tvecs, rvecs, transf_matrices = utilities.EstimateMarkerPositionFromImage(
        image,
        camera_matrix,
        dist_coeffs,
        marker_length=0.022,
        dictionary_name=cv2.aruco.DICT_4X4_250
    )

    if ids is None or len(ids) == 0:
        print("❌ No markers were detected.")
        return

    # === Create dictionary of detected marker IDs and transformation matrices ===
    marker_dict = {int(id_): tf for id_, tf in zip(ids.flatten(), transf_matrices)}
    print(f"🔎 Detected markers: {len(marker_dict)}")

    # === Prepare gripper ===
    robot.gripper_activate()
    robot.gripper_set_speed(50)
    robot.gripper_open()

    for i in range(5):
        pick_id = i
        place_id = i + 10

        robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)

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
            robot.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
            robot.moveL(best_pick, speed=0.1, acceleration=0.15)
            robot.gripper_close()
            robot.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

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
            robot.moveL(place_pose_above, speed=0.1, acceleration=0.15)
            robot.moveL(best_place, speed=0.1, acceleration=0.15)
            robot.gripper_open()
            robot.moveL(place_pose_above, speed=0.2, acceleration=0.3)

        else:
            print(f"⚠️ Marker {pick_id} or {place_id} not detected - skipped.")

    robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    print("✅ TEST 1 finished.")

def test_1_to(robot: robot_interface.RobotInterface, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    print("Spouštím TEST 1 – Eye-to-Hand")

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

    # === Prepare gripper ===
    robot.gripper_activate()
    robot.gripper_set_speed(50)
    robot.gripper_open()

    for i in range(5):
        pick_id = i
        place_id = i + 10

        robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)

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
            robot.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
            robot.moveL(best_pick, speed=0.1, acceleration=0.15)
            robot.gripper_close()
            robot.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

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
            robot.moveL(place_pose_above, speed=0.1, acceleration=0.15)
            robot.moveL(best_place, speed=0.1, acceleration=0.15)
            robot.gripper_open()
            robot.moveL(place_pose_above, speed=0.2, acceleration=0.3)

        else:
            print(f"⚠️ Marker {pick_id} nebo {place_id} nebyl detekován – přeskočeno.")

    robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    print("✅ TEST 1 dokončen.")

def test_2_in(robot: robot_interface.RobotInterface, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    """markery nalepené na kostičkách + forma, kam je uložit"""
    print("Spouštím TEST 2 – Eye-in-Hand (forma)")

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

    # === Prepare gripper ===
    robot.gripper_activate()
    robot.gripper_set_speed(50)
    robot.gripper_open()

    for i in range(4):
        pick_id = i
        place_id = 10  # forma s markerem ID 10

        robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)

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
        robot.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
        robot.moveL(best_pick, speed=0.1, acceleration=0.15)
        robot.gripper_close()
        robot.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

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
        robot.moveL(place_pose_above, speed=0.1, acceleration=0.15)
        robot.moveL(best_place, speed=0.1, acceleration=0.15)
        robot.gripper_open()
        robot.moveL(place_pose_above, speed=0.2, acceleration=0.3)

    robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    print("✅ TEST 2 dokončen.")

def test_2_to(robot: robot_interface.RobotInterface, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    print("Spouštím TEST 2 – Eye-to-Hand (forma)")

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

    # === Prepare gripper ===
    robot.gripper_activate()
    robot.gripper_set_speed(50)
    robot.gripper_open()

    for i in range(4):
        pick_id = i
        place_id = 10  # forma s markerem ID 10

        robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)

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
        robot.moveL(pick_pose_above, speed=0.1, acceleration=0.15)
        robot.moveL(best_pick, speed=0.1, acceleration=0.15)
        robot.gripper_close()
        robot.moveL(pick_pose_above, speed=0.2, acceleration=0.3)

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
        robot.moveL(place_pose_above, speed=0.1, acceleration=0.15)
        robot.moveL(best_place, speed=0.1, acceleration=0.15)
        robot.gripper_open()
        robot.moveL(place_pose_above, speed=0.2, acceleration=0.3)

    robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    print("✅ TEST 2 dokončen.")

def test_3_in(robot: robot_interface.RobotInterface, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    """kalibrační podložka a hrot"""
    print("Spouštím TEST 3 – Eye-in-Hand (kalibrační hrot)")

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
    robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    robot.moveL(best_pose, speed=0.1, acceleration=0.15)

    print("✅ Robot namířen na levý horní roh ChArUco desky.")
    time.sleep(2)

    # Návrat do výchozí pozice
    robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    print("✅ TEST 3 dokončen.")


def test_3_to(robot: robot_interface.RobotInterface, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf):
    print("Spouštím TEST 3 – Eye-to-Hand")

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
    robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    robot.moveL(best_pose, speed=0.05, acceleration=0.1)

    print("✅ Robot namířen na levý horní roh ChArUco desky.")
    time.sleep(3)

    # Návrat do výchozí pozice
    robot.moveL(utilities.tf_matrix_to_pose_vector(first_TCP_tf), speed=0.1, acceleration=0.15)
    print("✅ TEST 3 dokončen.")

# ===========================================================================================================

if __name__ == "__main__":
    try:
        robot = robot_interface.RobotInterface(ip_address, mode="rtde")
        # Load calibration data using the updated function
        file_path = 'calibration_results/basic_calib_in_02_05.yaml'
        success, result, message = utilities.load_calibration_results_yaml(file_path)

        if success:
            # Unpack the returned tuple
            camera_matrix, dist_coeffs, X_matrix, position_vector, calib_config, calib_method = result

        # Initialize robot parameters
        urcontrol_file = 'scripts/ur_robot_calib_params/UR_calibration/urcontrol.conf'
        calibration_file = 'scripts/ur_robot_calib_params/UR_calibration/calibration.conf'
        a, d, alpha = read_calib_data.load_dh_parameters_from_urcontrol(urcontrol_file)
        delta_theta, delta_a, delta_d, delta_alpha = read_calib_data.load_mounting_calibration_parameters(calibration_file)

        if light_test:
            if not utilities.enable_digital_output_rb(robot, light_output_id):
                raise RuntimeError("Failed to turn on light.")
            
        # utilities.enable_digital_output(ip_address,1)

        # Initialize camera
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        camera.Open()

        # Load user-defined camera settings (configured via Pylon Viewer)
        camera.UserSetSelector.SetValue("UserSet1")
        camera.UserSetLoad.Execute()
        
        # Try to enable freedrive mode
        success, message = utilities.enable_freedrive_mode_rb(robot)
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
        success, message = utilities.disable_freedrive_mode_rb(robot)
        if success:
            print("Freedrive mode disabled")
        else:
            raise RuntimeError(f"Failed to disable freedrive mode: {message}")
        time.sleep(1)

        first_TCP = robot.get_actual_tcp_pose()
        first_TCP_tf = utilities.pose_vector_to_tf_matrix(first_TCP)
        first_joints = np.array(robot.get_actual_joints())
        first_robot_tf = utilities.fk_with_corrections(first_joints, a, d, alpha, delta_theta, delta_a, delta_d, delta_alpha)

        # Výběr testu podle nastavení
        test_func = globals().get(selected_test)
        if test_func:
            test_func(robot, image, X_matrix, camera_matrix, dist_coeffs, first_TCP_tf, first_robot_tf)
        else:
            print(f"Neplatný název testu: {selected_test}")

        if light_test:
            utilities.disable_digital_output_rb(robot, light_output_id)

        print("✅ Test byl úspěšně dokončen.")

    except Exception as e:
        print(f"❌ Chyba během testu: {e}")
