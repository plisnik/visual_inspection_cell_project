from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QIntValidator)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QToolButton,
    QWidget, QFileDialog, QDialog, QMessageBox)
import time
import os
import sys
import numpy as np
from utils import utilities_camera, utilities
from GUI.global_data import GlobalData
from GUI.UI.main_window_ui import Ui_MainWindow
from GUI.camera_check import CameraCheck
from GUI.initial_adjustment import InitialAdjustment
from GUI.calibration_thread import CalibrationThread
from GUI.test_1 import Test_Thread_1
from GUI.test_2 import Test_Thread_2
from GUI.test_3 import Test_Thread_3
from GUI.progress_dialog import CalibrationProgressDialog
from GUI.progress_dialog_test import TestProgressDialog
from GUI.test_init import TestInit

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.global_data = GlobalData.get_instance()
        
        # Setup logger
        self.logger = self.global_data.logger
        self.logger.info("Application started")

        # Initialize UI state
        self.stackedWidget.setCurrentWidget(self.page_home)
        self.update_calibration_labels()

        # MENU  -----------------------------------------------------------------
        # Connect menu buttons to change pages
        self.b_home_menu.clicked.connect(lambda: self.change_page(self.page_home))
        self.b_calib_menu.clicked.connect(lambda: self.change_page(self.page_calib))
        self.b_test_menu.clicked.connect(lambda: self.change_page(self.page_test))
        self.b_settings_menu.clicked.connect(lambda: self.change_page(self.page_settings))

        # HOME  ---------------------------------------------------------------------
        # Connect buttons to actions
        self.b_new_calib.clicked.connect(lambda: self.b_calib_menu.click())
        self.b_test.clicked.connect(lambda: self.b_test_menu.click())
        self.b_upload_calib.clicked.connect(self.load_calibration)
        self.b_save_results.clicked.connect(self.save_calibration)
        self.b_save_data.clicked.connect(self.save_data)
        self.b_upload_data.clicked.connect(self.load_dataset)
        self.b_calculate.clicked.connect(self.calculate)

        # Disable for now
        self.b_upload_data.setEnabled(False)
        self.b_calculate.setEnabled(False)
        
        # CALIBRATION  ------------------------------------------------------------------
        # Disable before setup
        self.b_start_calib.setEnabled(False)
        self.b_initial_adjustment.setEnabled(False)

        # Calibration setup
        self.b_start_calib.clicked.connect(self.start_calibration)
        self.b_set_board_params.clicked.connect(self.set_board_params)
        self.b_set_IP.clicked.connect(self.set_ip_address)
        self.slider_light.valueChanged.connect(self.update_slider_light)
        self.slider_config.valueChanged.connect(self.update_slider_config)
        self.comboBox_methods.insertItem(0, "--- Vyber metodu ---")
        self.comboBox_methods.setCurrentIndex(0)
        self.comboBox_methods.currentIndexChanged.connect(self.update_calib_method)
        self.b_initial_adjustment.clicked.connect(self.camera_init_adjust)
        
        # Input validation
        self.lineEdit_rows.setValidator(QIntValidator(0, 999))
        self.lineEdit_columns.setValidator(QIntValidator(0, 999))
        self.lineEdit_size_square.setValidator(QIntValidator(0, 999))
        self.lineEdit_size_marker.setValidator(QIntValidator(0, 999))

        # TEST  ------------------------------------------------------------------------
        # Slidery - konfigurace a osvětlení
        self.slider_light_test.valueChanged.connect(self.update_slider_light_test)
        self.slider_config_test.valueChanged.connect(self.update_slider_config_test)
        self.b_test_1.setEnabled(False)
        self.b_test_2.setEnabled(False)
        self.b_test_1.clicked.connect(self.start_test_1)
        self.b_test_2.clicked.connect(self.start_test_2)

        # SETTINGS  ---------------------------------------------------------------------
        # Connect buttons to actions
        self.b_check_robot.clicked.connect(self.check_robot_status)
        self.b_camera_on.clicked.connect(self.turn_on_camera)
        self.b_camera_off.clicked.connect(self.turn_off_camera)
        self.b_light_on.clicked.connect(self.turn_on_light)
        self.b_light_off.clicked.connect(self.turn_off_light)
        self.b_camera_check.clicked.connect(self.camera_check_open)

        # RESPONSIVE  -----------------------------------------------------------------
        # Icons
        for tool_button in [self.b_new_calib, self.b_save_data, self.b_upload_calib, self.b_upload_data, self.b_test, self.b_save_results, self.b_calculate]:
            tool_button.resizeEvent = lambda event, tb=tool_button: self.resizeToolButton(tb, event)
        
    
    # FUNCTIONS  ------------------------------------------------------------------------

    def start_test_1(self):
        """Open the test init window."""
        self.logger.debug("Opening test initial window")

        # Initialize the adjustment window
        self.widget = TestInit(self.global_data)
        
        # Connect setup completion signal to enable the calibration button
        self.widget.start_signal.connect(lambda: QTimer.singleShot(0, self.test_1))
        
        # Show the adjustment window
        self.logger.info("Otevírání test initial window")
        self.widget.exec()
        self.logger.debug("Okno test initial zavřeno")

    def test_1(self):
        # Initialize progress dialog and test thread
        self.progress_dialog_test = TestProgressDialog(self.global_data)
        self.test_thread = Test_Thread_1(self.global_data)
        
        # Connect signals
        self.test_thread.finished_signal.connect(self.test_finished)  # Vlastní slot po dokončení testu
        self.test_thread.stop_signal.connect(self.test_stopped)
        self.progress_dialog_test.stop_signal.connect(self.test_thread.stop)  # Uživatel chce přerušit test

        # Start the test
        self.logger.debug("Launching test thread")
        self.test_thread.start()
        self.progress_dialog_test.exec()
    
    def test_finished(self):
        self.logger.info("Test process finished")

        # Změna textu a deaktivace tlačítka STOP
        self.progress_dialog_test.label.setText("Test completed successfully.")
        self.progress_dialog_test.stop_button.setEnabled(False)

        # Zavření okna po 2 sekundách
        QTimer.singleShot(2000, self.progress_dialog_test.close)

    def test_stopped(self):
        self.logger.info("Test stopped")
        self.progress_dialog_test.label.setText("Test stopped.")
        self.progress_dialog_test.stop_button.setEnabled(False)
        QTimer.singleShot(2000, self.progress_dialog_test.close)

    def start_test_2(self):
        """Open the test init window."""
        self.logger.debug("Opening test initial window")

        # Initialize the adjustment window
        self.widget = TestInit(self.global_data)
        
        # Connect setup completion signal to enable the calibration button
        self.widget.start_signal.connect(lambda: QTimer.singleShot(0, self.test_2))
        
        # Show the adjustment window
        self.logger.info("Otevírání test initial window")
        self.widget.exec()
        self.logger.debug("Okno test initial zavřeno")

    def test_2(self):
        pass
        # Initialize progress dialog and test thread
        self.progress_dialog_test = TestProgressDialog(self.global_data)
        self.test_thread = Test_Thread_2(self.global_data)
        
        # Connect signals
        self.test_thread.finished_signal.connect(self.test_finished)  # Vlastní slot po dokončení testu
        self.test_thread.stop_signal.connect(self.test_stopped)
        self.progress_dialog_test.stop_signal.connect(self.test_thread.stop)  # Uživatel chce přerušit test

        # Start the test
        self.logger.debug("Launching test thread")
        self.test_thread.start()
        self.progress_dialog_test.exec()

    def start_test_3(self):
        """Open the test init window."""
        self.logger.debug("Opening test initial window")

        # Initialize the adjustment window
        self.widget = TestInit(self.global_data)
        
        # Connect setup completion signal to enable the calibration button
        self.widget.start_signal.connect(lambda: QTimer.singleShot(0, self.test_3))
        
        # Show the adjustment window
        self.logger.info("Otevírání test initial window")
        self.widget.exec()
        self.logger.debug("Okno test initial zavřeno")

    def test_3(self):
        pass
        # Initialize progress dialog and test thread
        self.progress_dialog_test = TestProgressDialog(self.global_data)
        self.test_thread = Test_Thread_3(self.global_data)
        
        # Connect signals
        self.test_thread.finished_signal.connect(self.test_finished)  # Vlastní slot po dokončení testu
        self.test_thread.stop_signal.connect(self.test_stopped)
        self.progress_dialog_test.stop_signal.connect(self.test_thread.stop)  # Uživatel chce přerušit test

        # Start the test
        self.logger.debug("Launching test thread")
        self.test_thread.start()
        self.progress_dialog_test.exec()

    def start_calibration(self):
        """Start the calibration process and display a progress dialog."""
        self.logger.info("Starting calibration process")

        # Vymazat temrporary data
        try:
            utilities.delete_folder(self.global_data.temporary_data_set)
        except Exception as e:
            self.logger.error(e)
        
        # Vytvoření nové temporary_data_set
        os.makedirs(self.global_data.temporary_data_set)

        # Vytvoření podsložek, pokud neexistují
        for sub_dir in self.global_data.sub_dirs:
            os.makedirs(os.path.join(self.global_data.temporary_data_set, sub_dir), exist_ok=True)

        # Initialize progress dialog and calibration thread
        self.progress_dialog = CalibrationProgressDialog(self.global_data)
        self.calibration_thread = CalibrationThread(self.global_data)

        # Connect signals
        self.calibration_thread.progress_signal.connect(self.progress_dialog.update_progress)
        self.calibration_thread.finished_signal.connect(self.calibration_finished)
        self.calibration_thread.stop_signal.connect(self.calibration_stopped)
        self.progress_dialog.stop_signal.connect(self.calibration_thread.stop)  # Allow stopping the process

        # Start calibration
        self.logger.debug("Launching calibration thread")
        self.calibration_thread.start()
        self.progress_dialog.exec()
        self.logger.info("Calibration process initiated")

    def calibration_finished(self):
        """Handle the completion of the calibration process."""
        self.logger.info("Calibration completed successfully")
        self.update_calibration_labels()
        self.b_test_1.setEnabled(True)
        self.b_test_2.setEnabled(True)
        QTimer.singleShot(2000, self.progress_dialog.close)
        self.change_page(self.page_home)
    
    def calibration_stopped(self):
        """Handle the completion of the calibration process."""
        self.logger.info("Calibration stopped")
        self.progress_dialog.update_progress(0, "Calibration stopped")
        QTimer.singleShot(2000, self.progress_dialog.close)
        self.change_page(self.page_home)

    def update_initial_adjustment_button(self):
        """Enable the 'Initial Adjustment' button only if a method is selected and all required parameters are set."""
        has_method = self.comboBox_methods.currentIndex() > 0  # A method must be selected
        has_rows = bool(self.lineEdit_rows.text().strip())
        has_cols = bool(self.lineEdit_columns.text().strip())
        has_square_size = bool(self.lineEdit_size_square.text().strip())
        has_marker_size = bool(self.lineEdit_size_marker.text().strip())

        # Enable the button only if all conditions are met
        is_enabled = has_method and has_rows and has_cols and has_square_size and has_marker_size
        self.b_initial_adjustment.setEnabled(is_enabled)

        # Log status change
        if is_enabled:
            self.logger.debug("Initial adjustment button enabled")
        else:
            self.logger.debug("Initial adjustment button disabled - missing parameters")

    def camera_init_adjust(self):
        """Open the initial camera adjustment window."""
        self.logger.debug("Opening camera initial adjustment window")

        # Initialize the adjustment window
        self.widget = InitialAdjustment(self.global_data)
        
        # Connect setup completion signal to enable the calibration button
        self.widget.setup_pressed.connect(self.enable_target_button)
        
        # Show the adjustment window
        self.logger.info("Displaying camera adjustment dialog")
        self.widget.exec()
        self.logger.debug("Camera adjustment dialog closed")

    def enable_target_button(self):
        """Enable the calibration start button after initial camera adjustment."""
        self.b_start_calib.setEnabled(True)
        self.logger.info("Calibration start button enabled after camera adjustment")

    def calculate(self):
        pass

    def turn_on_camera(self):
        """Turn on the camera power."""
        self.logger.info("Attempting to enable camera power")
        self.statusBar().showMessage("Attempting to enable camera power")
        QApplication.processEvents()

        # Retrieve necessary parameters
        ip = self.global_data.ip_address
        output_id = self.global_data.camera_output_id

        # Try enabling camera power
        if utilities.enable_digital_output(ip, output_id):
            self.logger.info("Camera power successfully enabled")
            self.statusBar().showMessage("Camera power enabled")
        else:
            self.logger.error("Failed to enable camera power")
            self.statusBar().showMessage("Camera power activation failed!")

        # Ensure the button is not stuck in the pressed state
        self.b_camera_on.setChecked(False)

    def turn_off_camera(self):
        """Turn off the camera power."""
        self.logger.info("Attempting to disable camera power")
        self.statusBar().showMessage("Attempting to disable camera power")
        QApplication.processEvents()  # Refresh GUI immediately

        # Retrieve necessary parameters
        ip = self.global_data.ip_address
        output_id = self.global_data.camera_output_id

        # Check the current state of the digital output
        if utilities.disable_digital_output(ip, output_id):  # If the state is still active, the operation failed
            self.logger.error("Failed to disable camera power")
            self.statusBar().showMessage("Camera power disable failed!")
        else:  # If the state is inactive, the operation was successful
            self.logger.info("Camera power successfully disabled")
            self.statusBar().showMessage("Camera power disabled")

        # Ensure the button is not stuck in the pressed state
        self.b_camera_off.setChecked(False)

    def turn_on_light(self):
        """Turn on the light."""
        self.logger.info("Attempting to turn on the light")
        self.statusBar().showMessage("Turning on the light...")
        self.b_light_on.setText("Turning on...")
        QApplication.processEvents()  # Refresh GUI immediately

        # Try to turn on the light
        if utilities.enable_digital_output(self.global_data.ip_address, self.global_data.light_output_id): 
            self.logger.info("Light turned on")
            self.statusBar().showMessage("Light is ON")
        else:  # If the state is inactive, the operation failed
            self.logger.error("Failed to turn on the light")
            self.statusBar().showMessage("Light did not turn on!")

        # Ensure the button is not stuck in the pressed state
        self.b_light_on.setChecked(False)
        self.b_light_on.setText("Turn ON")

    def turn_off_light(self):
        """Turn off the light."""
        self.logger.info("Attempting to turn off the light")
        self.statusBar().showMessage("Turning off the light...")
        self.b_light_off.setText("Turning off...")
        QApplication.processEvents()  # Refresh GUI immediately

        # Try to turn off the light
        if utilities.disable_digital_output(self.global_data.ip_address, self.global_data.light_output_id):  
            self.logger.error("Failed to turn off the light")
            self.statusBar().showMessage("Light did not turn off!")
        else:  # If the state is inactive, the operation was successful
            self.logger.info("Light turned off")
            self.statusBar().showMessage("Light is OFF")

        # Ensure the button is not stuck in the pressed state
        self.b_light_off.setChecked(False)
        self.b_light_off.setText("Turn OFF")

    def load_calibration(self):
        """Open a dialog to select a calibration file, load calibration data, and store it in self.global_data."""
        self.logger.info("Opening file dialog to select a calibration file")
        file_path, _ = QFileDialog.getOpenFileName(self, "Select calibration file", "", "YAML Files (*.yaml);;All Files (*)")

        if file_path:
            self.logger.info(f"Loading calibration data from: {file_path}")

            # Load calibration data using the updated function
            success, result, message = utilities.load_calibration_results_yaml(file_path)

            if success:
                # Unpack the returned tuple
                camera_matrix, dist_coeffs, X_matrix, position_vector, calibration_config, calibration_method = result

                # Store data in self.global_data
                self.global_data.camera_matrix = camera_matrix
                self.global_data.dist_coeffs = dist_coeffs
                self.global_data.X_matrix = X_matrix
                self.global_data.position_vector = position_vector
                self.global_data.calib_config = calibration_config
                self.global_data.calib_method = calibration_method

                # Update UI labels
                self.update_calibration_labels()
                self.b_test_1.setEnabled(True)
                self.b_test_2.setEnabled(True)

                self.logger.info("Calibration data successfully loaded")
                self.statusBar().showMessage(f"Calibration loaded from: {file_path}")
            else:
                self.logger.error(f"Error loading calibration file: {message}", exc_info=True)
                self.statusBar().showMessage(f"{message}")


    def update_calibration_labels(self):
        """Update QLabel values in the UI based on the data stored in self.global_data."""

        self.logger.info("Updating calibration labels in UI")

        # Update labels for `camera_matrix` (3×3)
        for i in range(3):
            for j in range(3):
                label_name = f"cm_{i}_{j}"
                label = getattr(self, label_name, None)
                if label:
                    label.setText(f"{self.global_data.camera_matrix[i, j]:.5g}")

                label_name_t = f"cm_{i}_{j}_t"
                label_t = getattr(self, label_name_t, None)
                if label_t:
                    label_t.setText(f"{self.global_data.camera_matrix[i, j]:.5g}")

        # Update labels for `dist_coeff` (1×5) as a list string "[x,x,x,x,x]"
        if hasattr(self, "dist_coeff"):
            dist_coeff_text = f"{np.round(self.global_data.dist_coeffs.flatten(),5).tolist()}"
            self.dist_coeff.setText(dist_coeff_text)
            self.dist_coeff_t.setText(dist_coeff_text)

        # Update labels for `X_matrix` (4×4)
        for i in range(4):
            for j in range(4):
                label_name = f"tfm_{i}_{j}"
                label = getattr(self, label_name, None)
                if label:
                    label.setText(f"{self.global_data.X_matrix[i, j]:.5g}")

                label_name_t = f"tfm_{i}_{j}_t"
                label_t = getattr(self, label_name_t, None)
                if label_t:
                    label_t.setText(f"{self.global_data.X_matrix[i, j]:.5g}")

        # Update labels for `position_vector` (1×6) formatted as "[tx,ty,tz,rx,ry,rz]"
        if hasattr(self, "pose_vector"):
            pose_vector_text = f"{np.round(self.global_data.position_vector.flatten(),5).tolist()}"
            self.pose_vector.setText(pose_vector_text)
            self.pose_vector_t.setText(pose_vector_text)

        self.logger.info("Calibration labels updated successfully")
 
    def resizeToolButton(self, tool_button, event):
        """Dynamically adjust the tool button icon size based on its dimensions."""
        min_size = 50
        max_size = int(min(tool_button.width(), tool_button.height()) * 0.5)
        icon_size = max(min_size, max_size)
        tool_button.setIconSize(QSize(icon_size, icon_size))

    def save_data(self):
        """Open a QFileDialog to select a folder and save dataset files."""
        self.logger.info("Opening folder selection dialog for saving dataset")

        # Open folder selection dialog
        folder_path = QFileDialog.getExistingDirectory(self, "Select folder for saving data")

        # If the user selected a folder, attempt to save the dataset
        if folder_path:
            self.logger.info(f"Saving dataset to: {folder_path}")
            source_folder = self.global_data.temporary_data_set
            
            # Save dataset using updated function
            success, message = utilities.save_dataset(source_folder, folder_path)

            # Log and display the result
            if success:
                self.logger.info(message)
            else:
                self.logger.error(message)
            
            self.statusBar().showMessage(message)
        else:
            self.logger.warning("No folder selected for saving dataset")
            self.statusBar().showMessage("No folder selected!")

    def camera_check_open(self):
        """Open the camera check window."""
        self.logger.debug("Opening camera check window")
        self.widget = CameraCheck(self.global_data)
        self.widget.exec()
        self.logger.debug("Camera check window closed")

    def load_dataset(self):
        """
        Opens a file dialog to select a ZIP file, extracts its contents into 
        the temporary dataset folder, and logs any errors encountered.
        """
        
        self.logger.info("Attempting to load dataset")
        file_path, _ = QFileDialog.getOpenFileName(self, "Select ZIP file", "", "ZIP Files (*.zip);;All Files (*)")

        if file_path:
            self.logger.debug(f"Selected dataset file: {file_path}")
            success, error_message = utilities.extract_zip_dataset(file_path, self.global_data.temporary_data_set)

            if success:
                self.logger.info(f"Dataset successfully extracted to: {self.global_data.temporary_data_set}")
                self.statusBar().showMessage(f"Dataset loaded from: {file_path}")
            else:
                self.logger.error(f"Failed to extract dataset from: {file_path}. Error: {error_message}")
                self.statusBar().showMessage(f"Error extracting ZIP file: {error_message}")
        else:
            self.logger.warning("No file selected for dataset loading")
            self.statusBar().showMessage("No file selected!")

    def save_calibration(self):
        """Open a file dialog to save calibration data in a YAML file."""
        self.logger.info("Attempting to save calibration data")

        # Open file save dialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save calibration as", "", "YAML Files (*.yaml);;All Files (*)")

        if file_path:
            self.logger.info(f"Saving calibration data to: {file_path}")

            # Save calibration data using the updated function
            success, message = utilities.save_calibration_results_yaml(
                file_path,
                self.global_data.camera_matrix,
                self.global_data.dist_coeffs,
                self.global_data.X_matrix,
                self.global_data.position_vector,
                self.global_data.final_calib_config,
                self.global_data.final_calib_method
            )

            # Log and display the result
            if success:
                self.logger.info(message)
            else:
                self.logger.error(message)

            self.statusBar().showMessage(message)
        else:
            self.logger.warning("No file selected for saving calibration")
            self.statusBar().showMessage("No file selected!")

    def check_robot_status(self):
        """Check the robot connection status based on its IP address."""
        ip = self.global_data.ip_address
        self.logger.info(f"Checking robot connection status for IP: {ip}")

        # Verify connection status
        if utilities.check_robot_connection(ip):
            self.logger.info(f"Robot at IP {ip} is connected")
            self.statusBar().showMessage(f"Robot at IP {ip} is connected!")
        else:
            self.logger.error(f"Robot at IP {ip} is not connected")
            self.statusBar().showMessage(f"Robot at IP {ip} is not connected!")

    def update_calib_method(self, index):
        """Save the selected calibration method only if a valid option is chosen."""
        if index > 0:  # Index 0 is a placeholder
            self.global_data.calib_method = self.comboBox_methods.currentText()
            self.logger.info(f"Selected calibration method: {self.global_data.calib_method}")
            self.statusBar().showMessage(f"Selected calibration method: {self.global_data.calib_method}")
        else:
            self.global_data.calib_method = None
            self.logger.warning("No calibration method selected")
            self.statusBar().showMessage("No calibration method selected!")

        self.update_initial_adjustment_button()
    
    def update_slider_light(self, value):
        """Updates the light value according to the slider value."""
        self.global_data.light = value
        message = f"Light use {'enabled' if value else 'disabled'}"
        self.logger.info(message)
        self.statusBar().showMessage(message)

    def update_slider_light_test(self, value):
        """Updates the light value according to the slider value."""
        self.global_data.light_test = value
        message = f"Test: Light use {'enabled' if value else 'disabled'}"
        self.logger.info(message)
        self.statusBar().showMessage(message)

    def update_slider_config(self, value):
        """Updates according to the slider value."""
        self.global_data.calib_config = value
        message = f"Eye-in-hand configuration set" if value == 0 else "Eye-to-hand configuration set"
        self.logger.info(message)
        self.statusBar().showMessage(message)

    def update_slider_config_test(self, value):
        """Updates according to the slider value."""
        self.global_data.calib_config_test = value
        message = f"Test: Eye-in-hand configuration set" if value == 0 else "Test: Eye-to-hand configuration set"
        self.logger.info(message)
        self.statusBar().showMessage(message)

    def set_ip_address(self):
        """Retrieve the IP address from the input field and store it in self.global_data."""
        ip = self.lineEdit_IP.text().strip()

        # Store the value in the global variable
        self.global_data.ip_address = ip

        self.logger.info(f"Robot IP address set to: {self.global_data.ip_address}")
        self.statusBar().showMessage(f"Robot IP address set to: {self.global_data.ip_address}")

    def set_board_params(self):
        """Retrieve calibration board parameters from input fields and store them in self.global_data."""
        try:
            self.global_data.board_rows = int(self.lineEdit_rows.text())
            self.global_data.board_cols = int(self.lineEdit_columns.text())
            self.global_data.square_length = float(self.lineEdit_size_square.text()) / 1000
            self.global_data.marker_length = float(self.lineEdit_size_marker.text()) / 1000
            self.global_data.update_charuco_board()

            self.logger.info("Calibration board parameters updated")
            self.statusBar().showMessage("Calibration board parameters set")
            
            self.update_initial_adjustment_button()

        except ValueError as e:
            self.logger.error(f"Invalid input for board parameters: {e}")
            self.statusBar().showMessage("Error: Invalid board parameters")

    def change_page(self, page):
        """Switch to the specified page in the stacked widget."""
        self.logger.info(f"Changing to page: {page.objectName()}")
        self.stackedWidget.setCurrentWidget(page)

        # Temporarily disable the start calibration button
        self.b_start_calib.setEnabled(False)
    
    def closeEvent(self, event):
        """Intercepts the window close event to confirm with the user."""
        reply = QMessageBox.question(
            self,
            "Exit Application",
            "Are you sure you want to exit the application? Have you saved all your data?",
            QMessageBox.StandardButton.Close | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        )

        if reply == QMessageBox.StandardButton.Close:
            event.accept()  # Close the window
        else:
            event.ignore()  # Cancel closing


if __name__ == "__main__":
    app = QApplication(sys.argv)
    global_data = GlobalData.get_instance()
    
    # Setup root logger
    logger = global_data.logger
    logger.info("Application starting")
    
    try:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        logger.critical(f"Application crashed: {str(e)}", exc_info=True)
        raise
