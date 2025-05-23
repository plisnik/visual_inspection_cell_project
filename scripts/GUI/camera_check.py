from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
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
from UI.camera_check_ui import Ui_Camera_check
from camera_thread_class import CameraThread

class CameraCheck(QDialog, Ui_Camera_check):
    """
    Dialog window for camera preview and checking functionality.
    Handles camera thread management and image display.
    """
    def __init__(self, global_data: GlobalData):
        super(CameraCheck, self).__init__()
        self.setupUi(self)
        self.global_data = global_data
        self.logger = self.global_data.logger

        self.camera_thread = None  # Camera thread instance
        self.start_camera()

    def start_camera(self):
        """Starts the camera thread for image acquisition."""
        if self.camera_thread is None or not self.camera_thread.isRunning():
            self.camera_thread = CameraThread(self.global_data)  # Pass global_data instance
            self.camera_thread.frame_ready.connect(self.update_image)
            self.camera_thread.error_signal.connect(self.show_error)
            self.camera_thread.start()

    def stop_camera(self):
        """Stops the camera thread and releases resources."""
        if self.camera_thread and self.camera_thread.isRunning():
            self.camera_thread.stop()
            self.camera_thread = None
            self.logger.info("Camera thread stopped.")

    def update_image(self):
        """Updates the QLabel with the latest camera frame."""
        if self.global_data.image_global is not None:
            frame = self.global_data.image_global.copy()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = channel * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Scale image to fit the QLabel while maintaining aspect ratio
            scaled_pixmap = QPixmap.fromImage(q_img).scaled(
                self.label_image.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            self.label_image.setMinimumSize(300, 300)
            self.label_image.setPixmap(scaled_pixmap)

    def show_error(self, message: str):
        """Displays an error message in a critical QMessageBox."""
        self.logger.error(f"Camera error: {message}")
        QMessageBox.critical(self, "Camera Error", message)

    def closeEvent(self, event):
        """Stops the camera thread when the dialog is closed."""
        self.stop_camera()
        event.accept()



