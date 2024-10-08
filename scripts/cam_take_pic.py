import sys
import pyrealsense2 as rs
import numpy as np
import cv2
import os
import glob
import rtde_receive
import utilities as utilities


# IP adresa robota
ip_address = '192.168.0.11'

# Inicializace RTDE receive interface
rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)

# Hledání všech existujících složek začínajících na "data_set_"
existing_data_folders = glob.glob("data_set_*")

# Pokud nějaké složky existují, zjistíme nejvyšší číslo
if existing_data_folders:
    highest_data_number = max([int(folder.split('_')[-1]) for folder in existing_data_folders])
    new_data_folder_number = highest_data_number + 1
else:
    new_data_folder_number = 0

# Sestavení názvu nové složky pro dataset
data_folder_name = f"data_set_{new_data_folder_number:02d}"
os.makedirs(data_folder_name)

# Složky pro uložení snímků, kloubů a TCP pozic uvnitř dataset složky
pictures_folder = os.path.join(data_folder_name, f"cam_pictures_set_{new_data_folder_number:02d}")
os.makedirs(pictures_folder)

joints_folder = os.path.join(data_folder_name, f"joints_pose_set_{new_data_folder_number:02d}")
os.makedirs(joints_folder)

tcp_folder = os.path.join(data_folder_name, f"robot_pose_set_{new_data_folder_number:02d}")
os.makedirs(tcp_folder)

print(f"Nová složka byla vytvořena: {data_folder_name}, a pod-složky: {pictures_folder}, {joints_folder}, {tcp_folder}")

# Inicializace pipeliny kamery
pipeline = rs.pipeline()
config = rs.config()

# Povolení snímání barevného obrazu
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

# Spuštění streamu
pipeline.start(config)

count = 0

try:
    while True:
        # Zachycení snímku z kamery
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        if not color_frame:
            continue

        # Převod snímku na numpy pole
        color_image = np.asanyarray(color_frame.get_data())

        # Zobrazení snímku v okně
        cv2.imshow('RealSense', color_image)

        # Reakce na stisk klávesy
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Uložení snímku
            image_name = os.path.join(pictures_folder, f"image{count:02d}.png")
            cv2.imwrite(image_name, color_image)
            print(f"Snímek uložen jako {image_name}")

            # Načtení aktuálních úhlů kloubů a polohy TCP
            joint_angles = rtde_r.getActualQ()  # Kloubové úhly
            tcp_pose = rtde_r.getActualTCPPose()  # TCP pozice

            # Uložení kloubových úhlů do souborů (.txt a .npy)
            joints_txt = os.path.join(joints_folder, f"joints{count:02d}.txt")
            joints_npy = os.path.join(joints_folder, f"joints{count:02d}.npy")
            with open(joints_txt, 'w') as f:
                # Uložení pole ve formátu [a, b, c] s přesností na 8 desetinných míst
                f.write(f"[{', '.join(f'{x:.8f}' for x in joint_angles)}]")
            np.save(joints_npy, joint_angles)
            print(f"Kloubové úhly uloženy do {joints_txt} a {joints_npy}")

            # Uložení polohy TCP do souborů (.txt a .npy)
            pose_txt = os.path.join(tcp_folder, f"pose{count:02d}.txt")
            pose_npy = os.path.join(tcp_folder, f"pose{count:02d}.npy")
            with open(pose_txt, 'w') as f:
                # Uložení pole ve formátu [a, b, c] s přesností na 8 desetinných míst
                f.write(f"[{', '.join(f'{x:.8f}' for x in tcp_pose)}]")
            np.save(pose_npy, tcp_pose)
            print(f"TCP pozice uložena do {pose_txt} a {pose_npy}")

            count += 1

        elif key == ord('q'):
            # Ukončení programu po stisku klávesy 'q'
            print("Ukončuji program.")
            break

finally:
    # Ukončení streamu a uzavření oken
    pipeline.stop()
    cv2.destroyAllWindows()


# Vstupní a výstupní složky - DODĚLAT
input_folder = tcp_folder
output_folder = os.path.join(data_folder_name, f"robot_pose_tf_set_{new_data_folder_number:02d}")

# Vytvoření složky pro transformační matice
os.makedirs(output_folder, exist_ok=True)

# Zpracování souborů
utilities.batch_convert_poses_to_matrices(input_folder, output_folder)

