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
from UI.initial_adjustment_ui import Ui_Initial_adjustment
from camera_thread_class import CameraThread
from utils import utilities, utilities_camera

class InitialAdjustment(QDialog, Ui_Initial_adjustment):
    """Dialog window for initial camera adjustment before calibration."""
    
    setup_pressed = Signal()  # Signal emitted when setup is confirmed

    def __init__(self, global_data: GlobalData):
        """Initialize the initial adjustment dialog."""
        super(InitialAdjustment, self).__init__()
        self.setupUi(self)
        self.global_data = global_data
        self.logger = self.global_data.logger
        self.logger.info("Initial adjustment dialog opened")

        self.camera_thread = None  # Camera thread instance
        self.start_camera()
        self.b_setup.setEnabled(False)
        self.lineEdit_distance.textChanged.connect(self.update_setup_button)
        self.scale_factor: float = 0.3
        self.Slider_rectangle.valueChanged.connect(self.update_scale_factor)

        # Connect buttons
        self.b_setup.clicked.connect(self.emit_setup_signal)
        self.b_close.clicked.connect(self.close)
        self.b_freedrive_on.clicked.connect(self.enable_freedrive)
        self.b_freedrive_off.clicked.connect(self.disable_freedrive)
        self.b_light_on_init.clicked.connect(self.turn_on_light)
        self.b_light_off_init.clicked.connect(self.turn_off_light)

        # Set validators for input fields
        self.lineEdit_distance.setValidator(QIntValidator(0, 9999))

    # FUNCTIONS  -------------------------------------------------------------------------------

    def update_scale_factor(self, value):
        """Updates the scale_factor according to the slider value."""
        self.scale_factor = value / 100 

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
    
    def update_setup_button(self):
        """Enable the setup button only if an image is available and distance is entered."""
        has_image = self.global_data.image_global is not None
        has_distance = bool(self.lineEdit_distance.text().strip())

        self.b_setup.setEnabled(has_image and has_distance)

    def emit_setup_signal(self):
        """Emit a signal to the main window indicating the setup button was pressed."""
        self.global_data.distance = float(self.lineEdit_distance.text()) / 1000
        self.global_data.x_rect = self.x_rect
        self.global_data.y_rect = self.y_rect
        self.global_data.rect_width = self.rect_width
        self.global_data.rect_height = self.rect_height
        self.global_data.image_shape = self.image_shape
        self.logger.info(f"Setup confirmed with distance: {self.global_data.distance} meters")
        self.setup_pressed.emit()
        self.close()

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

    def update_image(self):
        """Update QLabel with the latest image from the camera."""
        if self.global_data.image_global is not None:
            frame = self.global_data.image_global.copy()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_final, self.x_rect, self.y_rect, self.rect_width, self.rect_height = utilities_camera.draw_scalable_rectangle(frame,self.scale_factor)
            height, width, channel = frame_final.shape
            self.image_shape = (width, height)
            bytes_per_line = channel * width
            q_img = QImage(frame_final.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Scale image to fit the label
            scaled_pixmap = QPixmap.fromImage(q_img).scaled(
                self.label_image.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            self.label_image.setMinimumSize(300, 300)
            self.label_image.setPixmap(scaled_pixmap)

        # Ensure setup button is updated
        self.update_setup_button()

    def show_error(self, message):
        """Display an error message."""
        self.logger.error(f"Camera error: {message}")
        QMessageBox.critical(self, "Camera Error", message)

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

        self.logger.info("Initial adjustment dialog closed")
        event.accept()

    def keyPressEvent(self, event):
        """Ignore Enter key press to close window."""
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            return  # Do nothing (ignore Enter key)
        super().keyPressEvent(event)  # Process other keys normally

