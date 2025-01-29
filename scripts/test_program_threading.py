import numpy as np
import rtde_receive
import rtde_control
import rtde_io
import time
from pypylon import pylon
from pypylon import genicam
import cv2
import os
import threading
from typing import List, Callable, Tuple, Any

'''
Předpoklad nastavení parametrů kamery dopředu (zjistit nastavení přes pypylon? asi jen dočasné?)
U realsense to šlo nastavovat ze skriptu

Postup - manuální (teď testovací)
Inicializace - nastavení ip adresy apod.
1. Připojení k robotu - zjistit zda funguje (např.vyčtení polohy)
2. Připojení ke kameře - zjistit zda funguje (zobrazit co vidí)
3. Přesun robota tak, aby viděl kalibrační podložku - vždy manuální, kolmo nad podložku, v zobrazení přidat obdélník, kde má podložka být v obraze
4. Snímání a ukládání jednotlivých fotek + ukládání polohy robota (přímo TCP nebo klouby+výpočet s kalib hodnotami) - manuální posun robota a potvrzování snímků
5. Výpočet kalibračních parametrů kamery
6. Zjištění pozice kalibrační podložky na jednotlivých snímcích
7. Výpočet Hand-eye kalibrace

Automatický pohyb
---
4. Automatický pohyb: snímání a ukládání jednotlivých fotek + ukládání polohy robota (vhodná trajektorie/jednotlivé body - od nastavené pozice, POZOR na překážky)
(pevně daný počet bodů nebo trajektorie s postupným výpočtem matice kamery i matice X (5. 6. 7. zároveň) a nastavení ukončení, pokud bude jen malá změna?) 
---

S uživatelkým rozhraním
Inicializace - nastavení ip adresy apod.
1. Připojení k robotu - zjistit zda funguje (funkce IsConnected - rtde_r?)
2. Připojení ke kameře - zjistit zda funguje (zobrazit co vidí)
3. Přesun robota tak, aby viděl kalibrační podložku - vždy manuální, kolmo nad podložku, v zobrazení přidat obdélník, kde má podložka být v obraze
4. Snímání a ukládání jednotlivých fotek + ukládání polohy robota - manuálně / automaticky
5. Výběr vyhovujících snímků / Odstranění nevyhovujících snímků
--- atd 

'''

# Global variable for controlling the camera display thread
stop_camera_thread = False

# List of active functions: Each function is stored as a tuple (function, priority)
active_functions: List[Tuple[Callable[..., Any], int]] = []

# Global variable for camera instance
camera = None
camera_thread = None
camera_lock = threading.Lock()  # Global lock for synchronization between threads

# Function for processing the image using active functions
def process_image(image: np.ndarray) -> np.ndarray:
    """
    Processes the image using active functions, applied in the order of their priority.

    Args:
        image (np.ndarray): The input image, typically from the camera.

    Returns:
        np.ndarray: The output image after applying all active functions.
    """
    # Sort active functions by priority (from lowest to highest value)
    sorted_functions = sorted(active_functions, key=lambda x: x[1])
    
    # Iterate over sorted functions and apply them to the image
    for func, _ in sorted_functions:
        image = func(image)
    return image


def camera_thread_function(camera: pylon.InstantCamera) -> None:
   """
   Runs the camera thread which continuously captures, processes and displays images.
   The thread runs until stopped via the global stop_camera_thread flag or user input.

   Args:
       camera (pylon.InstantCamera): The initialized Basler camera object.

   Returns:
       None
   """
   global stop_camera_thread
   
   # Start image acquisition with latest-image-only strategy
   camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
   
   while camera.IsGrabbing() and not stop_camera_thread:
       # Try to retrieve an image with 500ms timeout
       grab = camera.RetrieveResult(500, pylon.TimeoutHandling_Return)
       
       if grab.GrabSucceeded():
           # Convert grab result to numpy array
           image = grab.GetArray()
           
           # Process the captured image using active functions
           processed_image = process_image(image)
           
           # Display the processed image
           cv2.imshow("Camera", processed_image)
           
           # Check for ESC or 'q' key press to stop
           if cv2.waitKey(1) & 0xFF in (27, ord("q")):
               stop_camera_thread = True
               
       grab.Release()
   
   # Cleanup
   camera.StopGrabbing()
   cv2.destroyAllWindows()
   print("Camera stopped.")

def to_grayscale(image: np.ndarray) -> np.ndarray:
   """
   Converts an RGB/BGR image to grayscale.

   Args:
       image (np.ndarray): Input image in RGB/BGR format.

   Returns:
       np.ndarray: Grayscale version of the input image.
   """
   return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def threshold(image: np.ndarray) -> np.ndarray:
   """
   Applies binary thresholding to an image. If the input image is in color,
   it is first converted to grayscale.

   Args:
       image (np.ndarray): Input image, can be either grayscale or RGB/BGR.

   Returns:
       np.ndarray: Binary image after thresholding (values are either 0 or 255).
   """
   # Convert to grayscale if image is in color
   if len(image.shape) == 3:  
       image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       
   # Apply binary thresholding with threshold value of 127
   _, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
   return thresh_image

def enable_digital_output(rtde_IO: rtde_io.RTDEIOInterface, rtde_r: rtde_receive.RTDEReceiveInterface, output_id: int) -> None:
   """
   Enables a digital output on the UR robot and verifies its state.

   Args:
       rtde_IO (rtde_io.RTDEIOInterface): RTDE IO interface for controlling robot outputs.
       rtde_r (rtde_receive.RTDEReceiveInterface): RTDE receive interface for reading robot state.
       output_id (int): ID of the digital output to enable.

   Returns:
       None

   Raises:
       Exception: If there's an error setting or verifying the digital output.
   """
   try:
       # Enable the digital output
       rtde_IO.setStandardDigitalOut(output_id, True)
       print(f"Digital output {output_id} has been enabled.")

       # Wait briefly to ensure the output has been set
       time.sleep(1)

       # Verify the output state
       if rtde_r.getDigitalOutState(output_id):
           print(f"Standard digital out ({output_id}) is HIGH")
       else:
           print(f"Standard digital out ({output_id}) is LOW")

   except Exception as e:
       print(f"Error setting digital output: {e}")


def disable_digital_output(rtde_IO: rtde_io.RTDEIOInterface, rtde_r: rtde_receive.RTDEReceiveInterface, output_id: int) -> None:
   """
   Disables a digital output on the UR robot and verifies its state.

   Args:
       rtde_IO (rtde_io.RTDEIOInterface): RTDE IO interface for controlling robot outputs.
       rtde_r (rtde_receive.RTDEReceiveInterface): RTDE receive interface for reading robot state.
       output_id (int): ID of the digital output to disable.

   Returns:
       None

   Raises:
       Exception: If there's an error setting or verifying the digital output.
   """
   try:
       # Disable the digital output
       rtde_IO.setStandardDigitalOut(output_id, False)
       print(f"Digital output {output_id} has been disabled.")

       # Wait briefly to ensure the output has been set
       time.sleep(1)

       # Verify the output state
       if rtde_r.getDigitalOutState(output_id):
           print(f"Standard digital out ({output_id}) is HIGH")
       else:
           print(f"Standard digital out ({output_id}) is LOW")

   except Exception as e:
       print(f"Error setting digital output: {e}")

def connect_to_camera() -> pylon.InstantCamera | None:
   """
   Connects to the first available Basler camera and loads UserSet1 configuration.

   Returns:
       pylon.InstantCamera | None: Initialized camera object if connection successful,
                                  None if connection fails.

   Raises:
       RuntimeError: If no camera is found.
       Exception: For other camera connection or configuration errors.
   """
   try:
       # Get the transport layer factory
       tl_factory = pylon.TlFactory.GetInstance()
       
       # Look for available devices
       devices = tl_factory.EnumerateDevices()
       if not devices:
           raise RuntimeError("No camera found.")
           
       # Create and open camera object
       camera = pylon.InstantCamera(tl_factory.CreateFirstDevice())
       camera.Open()
       print("Camera connected successfully.")
       
       # Load user-defined camera settings (configured via Pylon Viewer)
       camera.UserSetSelector.SetValue("UserSet1")
       camera.UserSetLoad.Execute()
       
       return camera
       
   except Exception as e:
       print(f"Error connecting to camera: {e}")
       return None

# Function to change exposure time
def change_exposure_time(new_exposure_time: float):
    """
    Function to change the exposure time of the camera.
    Stops the camera, changes the exposure time, and restarts the camera.

    Args:
        new_exposure_time (float): The new exposure time to set in seconds.
    """
    global camera, camera_lock, stop_camera_thread, camera_thread
    with camera_lock:  # Acquire the lock to ensure no other thread is modifying the camera
        # Stop camera (simulation)
        print("Stopping camera for exposure time adjustment.")
        stop_camera_thread = True
        if camera_thread is not None:
            camera_thread.join()  # Wait for the camera thread to stop
        
        # Change the exposure time here (camera-specific code)
        print(f"Changing exposure time to {new_exposure_time} seconds.")
        camera.ExposureTime.SetValue(new_exposure_time)
        
        # Restart the camera with the new exposure time
        stop_camera_thread = False
        camera_thread = threading.Thread(target=camera_thread_function, args=(camera,))
        camera_thread.start()
        print("Camera restarted with new exposure time.")

# Main control program
def main():
    global stop_camera_thread, active_functions, camera, camera_lock, camera_thread

    # IP address of the robot
    ip_address = "192.168.209.124"

    # Creating RTDE instances
    rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)
    rtde_c = rtde_control.RTDEControlInterface(ip_address)
    rtde_IO = rtde_io.RTDEIOInterface(ip_address)
    
    # Check connection status
    connect = rtde_r.isConnected()
    print(connect)

    while True:
        print("\n--- Menu ---")
        print("1: Connect to the camera")
        print("2: Start camera - thread + image")
        print("3: Add grayscale processing")
        print("4: Add thresholding")
        print("5: Remove grayscale processing")
        print("6: Remove thresholding")
        print("7: Read robot position")
        print("8: Turn on camera power")
        print("9: Turn on light")
        print("10: Turn off light")
        print("11: Turn off camera power")
        print("12: Set exposure time")
        print("X: Exit")

        choice = input("Choose an action: ")
        
        match choice:
            case "1":
                # Connect to the camera
                camera = connect_to_camera()
            case "2":
                # Start camera if not already running or connected
                if camera is None:
                    print("Camera is not connected.")
                elif camera_thread is not None and camera_thread.is_alive():
                    print("Camera is already running.")
                else:
                    stop_camera_thread = False
                    camera_thread = threading.Thread(target=camera_thread_function, args=(camera,))
                    camera_thread.start()
                    print("Camera started.")
            case "3":
                # Add grayscale processing to the active functions list
                if to_grayscale not in active_functions:
                    active_functions.append((to_grayscale, 1))
                    print("Grayscale processing added.")
                else:
                    print("Grayscale processing is already active.")
            case "4":
                # Add thresholding to the active functions list
                if threshold not in active_functions:
                    active_functions.append((threshold, 2))
                    print("Thresholding added.")
                else:
                    print("Thresholding is already active.")
            case "5":
                # Remove grayscale processing
                if to_grayscale in active_functions:
                    active_functions.remove((to_grayscale, 1))
                    print("Grayscale processing removed.")
                else:
                    print("Grayscale processing was not active.")
            case "6":
                # Remove thresholding
                if threshold in active_functions:
                    active_functions.remove((threshold, 2))
                    print("Thresholding removed.")
                else:
                    print("Thresholding was not active.")
            case "7":
                # Read robot position
                actual_q = rtde_r.getActualQ()
                print(actual_q)
                actual_TCP = rtde_r.getActualTCPPose()
                print(actual_TCP)
            case "8":
                # Turn on camera power
                enable_digital_output(rtde_IO, rtde_r, output_id=1)
            case "9":
                # Turn on light
                enable_digital_output(rtde_IO, rtde_r, output_id=0)
            case "10":
                # Turn off light
                disable_digital_output(rtde_IO, rtde_r, output_id=0)
            case "11":
                # Turn off camera power
                disable_digital_output(rtde_IO, rtde_r, output_id=1)
            case "12":
                # Set exposure time
                if camera is not None:
                    exposure_time = float(input("Enter the new exposure time (in seconds): "))
                    change_exposure_time(exposure_time)
                else:
                    print("Camera is not connected.")
            case "X":
                # Exit the program
                print("Exiting program.")
                stop_camera_thread = True
                if camera_thread is not None:
                    camera_thread.join()
                break
            case _:
                # Handle invalid choice
                print("Invalid choice, please try again.")
    
    if camera:
        # Close the camera connection if it was opened
        camera.Close()


if __name__ == "__main__":
    main()
