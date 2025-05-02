from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar, QPushButton
from PySide6.QtCore import Signal, Qt
from global_data import GlobalData

class CalibrationProgressDialog(QDialog):
    """Dialog window displaying calibration progress with a stop option."""

    stop_signal = Signal()  # Signal to stop the calibration process

    def __init__(self, global_data: GlobalData):
        """Initialize the progress dialog."""
        super(CalibrationProgressDialog, self).__init__()
        self.setWindowTitle("Calibration in Progress")
        self.setModal(True)  # Prevent interaction with the main window
        # nelze zavřít okno
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        
        self.global_data = global_data
        self.logger = self.global_data.logger

        layout = QVBoxLayout()

        self.label = QLabel("Calibration is in progress, please wait...")
        layout.addWidget(self.label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        layout.addWidget(self.progress_bar)

        self.stop_button = QPushButton("STOP")
        self.stop_button.clicked.connect(self.stop_calibration)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)
        self.logger.info("Calibration progress dialog initialized")

    def update_progress(self, step, message):
        """Update the progress bar and status label."""
        self.progress_bar.setValue(step)
        self.label.setText(message)

    def stop_calibration(self):
        """Emit a signal to stop the calibration process."""
        self.logger.warning("Calibration process stop requested")
        self.stop_signal.emit()
