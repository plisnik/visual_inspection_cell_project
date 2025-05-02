from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Signal, Qt
from global_data import GlobalData

class TestProgressDialog(QDialog):
    """Dialog window showing test progress with STOP option."""

    stop_signal = Signal()  # Signal to stop the test process

    def __init__(self, global_data: GlobalData):
        super(TestProgressDialog, self).__init__()
        self.setWindowTitle("Test in Progress")
        self.setModal(True)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # Disable close button

        self.global_data = global_data
        self.logger = self.global_data.logger

        layout = QVBoxLayout()

        self.label = QLabel("Test is currently running...\nPlease wait or press STOP to cancel.")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.stop_button = QPushButton("STOP")
        self.stop_button.clicked.connect(self.stop_test)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)
        self.logger.info("Test progress dialog initialized")

    def stop_test(self):
        """Emit a signal to stop the test process."""
        self.logger.warning("Test process stop requested")
        self.stop_signal.emit()
