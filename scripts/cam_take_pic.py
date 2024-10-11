import sys
import pyrealsense2 as rs
import numpy as np
import cv2
import os
import glob
import rtde_receive
import utilities as utilities

def main():
    # Robot's IP address
    ip_address = '192.168.0.11'

    # Initialize RTDE receive interface
    rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)

    # Find all existing folders starting with "data_set_"
    existing_data_folders = glob.glob("data_set_*")

    # Determine the highest folder number if any exist, otherwise start with 0
    if existing_data_folders:
        highest_data_number = max([int(folder.split('_')[-1]) for folder in existing_data_folders])
        new_data_folder_number = highest_data_number + 1
    else:
        new_data_folder_number = 0

    # Construct the name for the new dataset folder
    data_folder_name = f"data_set_{new_data_folder_number:02d}"
    os.makedirs(data_folder_name)

    # Create folders for storing images, joint positions, and TCP poses inside the dataset folder
    pictures_folder = os.path.join(data_folder_name, f"cam_pictures_set_{new_data_folder_number:02d}")
    os.makedirs(pictures_folder)

    joints_folder = os.path.join(data_folder_name, f"joints_pose_set_{new_data_folder_number:02d}")
    os.makedirs(joints_folder)

    tcp_folder = os.path.join(data_folder_name, f"robot_pose_set_{new_data_folder_number:02d}")
    os.makedirs(tcp_folder)

    print(f"New folder created: {data_folder_name}, with sub-folders: {pictures_folder}, {joints_folder}, {tcp_folder}")

    # Initialize the camera pipeline
    pipeline = rs.pipeline()
    config = rs.config()

    # Enable color image streaming
    config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

    # Start the streaming
    pipeline.start(config)

    count = 0

    try:
        while True:
            # Capture a frame from the camera
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()

            if not color_frame:
                continue

            # Convert the frame to a numpy array
            color_image = np.asanyarray(color_frame.get_data())

            # Display the image in a window
            cv2.imshow('RealSense', color_image)

            # Respond to key presses
            key = cv2.waitKey(1) & 0xFF

            if key == ord('s'):
                # Save the captured image
                image_name = os.path.join(pictures_folder, f"image{count:02d}.png")
                cv2.imwrite(image_name, color_image)
                print(f"Image saved as {image_name}")

                # Retrieve the current joint angles and TCP pose
                joint_angles = rtde_r.getActualQ()  # Joint angles
                tcp_pose = rtde_r.getActualTCPPose()  # TCP position

                # Save joint angles to files (.txt and .npy)
                joints_txt = os.path.join(joints_folder, f"joints{count:02d}.txt")
                joints_npy = os.path.join(joints_folder, f"joints{count:02d}.npy")
                with open(joints_txt, 'w') as f:
                    # Save the array in the format [a, b, c] with 8 decimal precision
                    f.write(f"[{', '.join(f'{x:.8f}' for x in joint_angles)}]")
                np.save(joints_npy, joint_angles)
                print(f"Joint angles saved to {joints_txt} and {joints_npy}")

                # Save TCP position to files (.txt and .npy)
                pose_txt = os.path.join(tcp_folder, f"pose{count:02d}.txt")
                pose_npy = os.path.join(tcp_folder, f"pose{count:02d}.npy")
                with open(pose_txt, 'w') as f:
                    # Save the array in the format [a, b, c] with 8 decimal precision
                    f.write(f"[{', '.join(f'{x:.8f}' for x in tcp_pose)}]")
                np.save(pose_npy, tcp_pose)
                print(f"TCP position saved to {pose_txt} and {pose_npy}")

                count += 1

            elif key == ord('q'):
                # Exit the program when 'q' is pressed
                print("Exiting program.")
                break

    finally:
        # Stop the streaming and close all windows
        pipeline.stop()
        cv2.destroyAllWindows()

    # Create a folder for storing transformation matrices
    tf_matrix_folder = os.path.join(data_folder_name, f"robot_pose_tf")
    os.makedirs(tf_matrix_folder, exist_ok=True)

    # Convert TCP poses to transformation matrices and store them
    utilities.batch_convert_poses_to_matrices(tcp_folder, tf_matrix_folder)


if __name__ == '__main__':
    sys.exit(main())
