from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, Signal,
    QSize, QTime, QUrl, Qt, QTimer, QMutex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QIntValidator)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QToolButton,
    QWidget, QFileDialog, QDialog, QMessageBox)
import cv2
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from global_data import GlobalData
from UI.test_init_ui import Ui_test_1
from camera_thread_class import CameraThread
from utils import utilities, utilities_camera
from ur_robot_calib_params import read_calib_data

class TestInit(QDialog,Ui_test_1):
    """Dialog window before starting test."""

    start_signal = Signal()

    def __init__(self, global_data: GlobalData):
        """Initialize the initial adjustment dialog."""
        super(TestInit, self).__init__()
        self.setupUi(self)
        self.global_data = global_data
        self.logger = self.global_data.logger
        self.logger.info("Test Initial dialog opened")

        self.camera_thread = None  # Camera thread instance
        self.start_camera()

        # Connect buttons
        self.b_start_test.clicked.connect(self.emit_start_signal)
        self.b_close.clicked.connect(self.close)
        self.b_freedrive_on.clicked.connect(self.enable_freedrive)
        self.b_freedrive_off.clicked.connect(self.disable_freedrive)
        self.b_light_on_init.clicked.connect(self.turn_on_light)
        self.b_light_off_init.clicked.connect(self.turn_off_light)


    # FUNCTIONS  -----------------------------------------------------------------


    def start_camera(self):
        """Start the camera thread."""
        if self.camera_thread is None or not self.camera_thread.isRunning():
            self.logger.info("Starting camera thread")
            self.camera_thread = CameraThread(self.global_data)
            self.camera_thread.frame_ready.connect(self.update_image)
            self.camera_thread.error_signal.connect(self.show_error)
            self.camera_thread.start()
        else:
            self.logger.warning("Camera thread is already running")

    def stop_camera(self):
        """Stop the camera thread."""
        if self.camera_thread and self.camera_thread.isRunning():
            self.logger.info("Stopping camera thread")
            self.camera_thread.stop()
            self.camera_thread = None

    def show_error(self, message):
        """Display an error message."""
        self.logger.error(f"Camera error: {message}")
        QMessageBox.critical(self, "Camera Error", message)

    def turn_on_light(self):
        """Turn on the light."""
        self.logger.info("Attempting to turn on the light")
        self.b_light_on_init.setText("Turning on...")
        QApplication.processEvents()  # Refresh GUI immediately

        # Try to turn on the light
        state = utilities.enable_digital_output(self.global_data.ip_address, self.global_data.light_output_id)

        if state:  # If the state is active, the light has been turned on successfully
            self.logger.info("Light turned on")
        else:  # If the state is inactive, the operation failed
            self.logger.error("Failed to turn on the light")

        # Ensure the button is not stuck in the pressed state
        self.b_light_on_init.setChecked(False)
        self.b_light_on_init.setText("Light ON")

    def turn_off_light(self):
        """Turn off the light."""
        self.logger.info("Attempting to turn off the light")
        self.b_light_off_init.setText("Turning off...")
        QApplication.processEvents()  # Refresh GUI immediately

        # Try to turn off the light
        state = utilities.disable_digital_output(self.global_data.ip_address, self.global_data.light_output_id)

        if state:  # If the state is still active, the operation failed
            self.logger.error("Failed to turn off the light")
        else:  # If the state is inactive, the operation was successful
            self.logger.info("Light turned off")

        # Ensure the button is not stuck in the pressed state
        self.b_light_off_init.setChecked(False)
        self.b_light_off_init.setText("Light OFF")

    def enable_freedrive(self):
        """Enable freedrive mode for manual movement of the robot."""
        self.logger.info("Attempting to enable freedrive mode")
        self.b_freedrive_on.setText("Enabling...")
        QApplication.processEvents()  # Refresh GUI immediately

        # Try to enable freedrive mode
        success, message = utilities.enable_freedrive_mode(self.global_data.ip_address)

        if success:
            self.logger.info("Freedrive mode enabled")
        else:
            self.logger.error(f"Failed to enable freedrive mode: {message}")

        # Ensure the button is not stuck in the pressed state
        self.b_freedrive_on.setChecked(False)
        self.b_freedrive_on.setText("Freedrive ON")

    def disable_freedrive(self):
        """Disable freedrive mode and return to normal control mode."""
        self.logger.info("Attempting to disable freedrive mode")
        self.b_freedrive_off.setText("Disabling...")
        QApplication.processEvents()  # Refresh GUI immediately

        # Try to disable freedrive mode
        success, message = utilities.disable_freedrive_mode(self.global_data.ip_address)

        if success:
            self.logger.info("Freedrive mode disabled")
        else:
            self.logger.error(f"Failed to disable freedrive mode: {message}")

        # Ensure the button is not stuck in the pressed state
        self.b_freedrive_off.setChecked(False)
        self.b_freedrive_off.setText("Freedrive OFF")

    def update_image(self):
        """Update QLabel with the latest image from the camera."""
        if self.global_data.image_global is not None:
            frame = self.global_data.image_global.copy()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            self.image_shape = (width, height)
            bytes_per_line = channel * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Scale image to fit the label
            scaled_pixmap = QPixmap.fromImage(q_img).scaled(
                self.image_label.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            self.image_label.setMinimumSize(400, 400)
            self.image_label.setPixmap(scaled_pixmap)

    def emit_start_signal(self):
        """..."""
        self.global_data.image_shape = self.image_shape
        self.logger.info(f"...")
        self.start_signal.emit()
        self.close()

    def closeEvent(self, event):
        """Ensure the camera thread is stopped when the window is closed."""
        self.stop_camera()

        success, message = utilities.disable_freedrive_mode(self.global_data.ip_address)
        if success:
            self.logger.info("Freedrive mode disabled")
        else:
            self.logger.error(f"Failed to disable freedrive mode: {message}")

        state = utilities.disable_digital_output(self.global_data.ip_address, self.global_data.light_output_id)

        if state:  # If the state is still active, the operation failed
            self.logger.error("Failed to turn off the light")
        else:  # If the state is inactive, the operation was successful
            self.logger.info("Light turned off")

        self.logger.info("Test Initial dialog closed")
        event.accept()
