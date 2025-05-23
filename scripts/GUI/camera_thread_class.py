from PySide6.QtCore import QThread, Signal
from pypylon import pylon
import cv2
import numpy as np
from global_data import GlobalData

class CameraThread(QThread):
    """Thread for continuous camera image acquisition."""
    
    frame_ready = Signal()  # Signal to update the image
    error_signal = Signal(str)  # Signal for error messages

    def __init__(self, global_data: GlobalData):
        super(CameraThread, self).__init__()
        self.global_data = global_data
        self.logger = self.global_data.logger
        self.camera = None
        self.is_running = False

    def run(self):
        """Main loop for image acquisition."""
        try:
            # Initialize camera
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.camera.Open()

            # Load user-defined camera settings (configured via Pylon Viewer)
            self.camera.UserSetSelector.SetValue("UserSet1")
            self.camera.UserSetLoad.Execute()
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            self.is_running = True
            self.logger.info("Camera connected and acquisition started.")

            fail_counter = 0  # Number of consecutive unsuccessful attempts
            # Image acquisition loop
            while self.camera.IsGrabbing() and self.is_running:
                grab_result = self.camera.RetrieveResult(500, pylon.TimeoutHandling_Return)
                
                if grab_result.GrabSucceeded():
                    img = grab_result.GetArray()  # Get image array
                    frame = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)  # Convert to BGR
                    self.global_data.image_global = frame  # Store in shared data
                    self.frame_ready.emit()  # Emit signal for GUI update
                    fail_counter = 0  # Reset při úspěchu

                else:
                    fail_counter += 1
                    if fail_counter >= 5:
                        error_msg = "Error capturing image from camera (5 consecutive failures)."
                        self.logger.error(error_msg)
                        self.error_signal.emit(error_msg)
                        fail_counter = 0  # Reset even after an error is reported, so that it is not emitted every iteration

        except Exception as e:
            error_msg = f"Camera error: {str(e)}"
            if self.logger:
                self.logger.critical(error_msg, exc_info=True)
            self.error_signal.emit(error_msg)

        finally:
            self.cleanup()

    def stop(self):
        """Stops the thread and releases the camera."""
        self.is_running = False
        self.wait()  # Waits for the thread to exit safely

    def cleanup(self):
        """Releases the camera on exit."""
        if self.camera:
            self.camera.Close()
            del self.camera  # Release object
            self.camera = None

        self.logger.info("Camera disconnected.")
