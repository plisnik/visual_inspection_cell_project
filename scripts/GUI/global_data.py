import threading
from queue import Queue
import numpy as np
import cv2
from pypylon import pylon
from typing import List, Tuple, Optional, Union, Any, Callable
from numpy.typing import NDArray
from datetime import datetime
import logging
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import utilities

class GlobalData:
    """
    Singleton class for managing global application state and resources.
    Handles camera operations, calibration parameters, and various application settings.
    """
    _instance: Optional['GlobalData'] = None

    def __new__(cls) -> 'GlobalData':
        if cls._instance is None:
            cls._instance = super(GlobalData, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self) -> None:
        """Initialize all variables. Called only once during first instance creation."""
        # Robot interface
        self.ip_address: str = "192.168.209.132"
        self.camera_output_id: int = 1
        self.light_output_id: int = 0

        # Setup logger
        self.logger: logging.Logger = self.setup_logger()

        # Camera 
        self.camera: pylon.InstantCamera = pylon.InstantCamera()
        self.camera_thread: Optional[threading.Thread] = None
        self.stop_camera_thread: bool = False
        self.camera_lock: threading.Lock = threading.Lock()
        self.image_global: Optional[NDArray[np.uint8]] = None
        self.image_queue: Queue[NDArray[np.uint8]] = Queue(maxsize=1)
        self.image_shape: Tuple[int, int] = (2472, 2064)

        # Active image processing functions
        self.active_functions: List[Callable[..., Any]] = []

        # ChArUco calibration parameters
        self.square_length: float = 0.03
        self.marker_length: float = 0.022
        self.board_rows: int = 6
        self.board_cols: int = 8
        self.board_size: Tuple[int, int] = (self.board_cols, self.board_rows)
        self.board_width: float = self.board_cols * self.square_length
        self.board_height: float = self.board_rows * self.square_length
        self.aruco_dict: cv2.aruco.Dictionary = cv2.aruco.getPredefinedDictionary(
            cv2.aruco.DICT_4X4_250
        )
        self.charuco_board: cv2.aruco.CharucoBoard = cv2.aruco.CharucoBoard(
            self.board_size,
            self.square_length,
            self.marker_length,
            self.aruco_dict
        )
        self.charuco_board.setLegacyPattern(True)
        self.charuco_detector: cv2.aruco.CharucoDetector = cv2.aruco.CharucoDetector(
            self.charuco_board
        )
        self.charuco_params: cv2.aruco.CharucoParameters = cv2.aruco.CharucoParameters()
        self.detec_params: cv2.aruco.DetectorParameters = cv2.aruco.DetectorParameters()

        # Data paths configuration
        self.temporary_data_set: str = "data_sets/temporary_data_set"
        self.sub_dirs: List[str] = ["cam_pictures", "robot_pose_tf", "obj_pose_tf", "tcp_pose_tf", "joints_pose"]
        self.image_folder: str = os.path.join(self.temporary_data_set, 'cam_pictures')
        self.robot_pose_folder: str = os.path.join(self.temporary_data_set, 'robot_pose_tf')
        self.joints_pose_folder: str = os.path.join(self.temporary_data_set, 'joints_pose')
        self.TCP_pose_folder: str = os.path.join(self.temporary_data_set, 'tcp_pose_tf')
        self.obj_pose_folder: str = os.path.join(self.temporary_data_set, 'obj_pose_tf')

        # Camera calibration parameters
        self.camera_matrix: NDArray[np.float64] = np.zeros((3, 3), dtype=np.float64)
        self.dist_coeffs: NDArray[np.float64] = np.zeros((1, 5), dtype=np.float64)

        # Calibration results
        self.X_matrix: NDArray[np.float64] = np.zeros((4, 4), dtype=np.float64)
        self.position_vector: NDArray[np.float64] = np.zeros((1, 6), dtype=np.float64)

        # Calibration data storage
        self.obj_pose_tf_list: List[NDArray[np.float64]] = []
        self.rob_pose_tf_list: List[NDArray[np.float64]] = []

        # Hand-Eye Calibration parameters
        self.distance: float = 0
        self.x_rect: int = 0
        self.y_rect: int = 0
        self.rect_width: int = 0
        self.rect_height: int = 0
        self.calib_config: int = 0      # 0 = Eye-in-Hand, 1 = Eye-to-Hand
        self.calib_method: str = ""
        self.light: int = 0             # 0 without light, 1 with light

        # Mapping method names to cv2 constants
        self.method_map = {
            'TSAI': cv2.CALIB_HAND_EYE_TSAI,
            'PARK': cv2.CALIB_HAND_EYE_PARK,
            'HORAUD': cv2.CALIB_HAND_EYE_HORAUD,
            'ANDREFF': cv2.CALIB_HAND_EYE_ANDREFF,
            'DANIILIDIS': cv2.CALIB_HAND_EYE_DANIILIDIS,
            'LI (world)': cv2.CALIB_ROBOT_WORLD_HAND_EYE_LI,
            'SHAH (world)': cv2.CALIB_ROBOT_WORLD_HAND_EYE_SHAH,
        }

        # Used calibration calculation
        self.final_calib_config: int = 0    # 0 = Eye-in-Hand, 1 = Eye-to-Hand
        self.final_calib_method: str = ""

        # Testing configuration
        self.calib_config_test: int = 0     # 0 = Eye-in-Hand, 1 = Eye-to-Hand
        self.light_test: int = 0            # 0 without light, 1 with light

    @classmethod
    def get_instance(cls) -> 'GlobalData':
        """
        Ensures singleton pattern by always returning the same instance.
        
        Returns:
            GlobalData: The singleton instance of GlobalData
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def update_charuco_board(self):
        """Recomputes dependent parameters when board settings are changed."""
        self.board_size = (self.board_cols, self.board_rows)
        self.board_width = self.board_cols * self.square_length
        self.board_height = self.board_rows * self.square_length

        self.charuco_board = cv2.aruco.CharucoBoard(
            self.board_size,
            self.square_length,
            self.marker_length,
            self.aruco_dict
        )
        self.charuco_board.setLegacyPattern(True)

        self.charuco_detector = cv2.aruco.CharucoDetector(self.charuco_board)

    def reset_calibration_data(self) -> None:
        """Resets all calibration-related data to initial values."""
        self.obj_pose_tf_list = []
        self.rob_pose_tf_list = []
        self.camera_matrix = np.zeros(3,3)
        self.dist_coeffs = np.zeros(1,5)
        self.X_matrix = np.zeros(4,4)
        self.position_vector = np.zeros(1,6)

    def ensure_directories(self) -> None:
        """Creates all necessary directories if they don't exist."""
        for dir_path in [self.image_folder, self.robot_pose_folder, self.obj_pose_folder]:
            os.makedirs(dir_path, exist_ok=True)

    def get_camera(self):
        """Create a new camera instance"""
        self.camera = utilities.connect_to_camera(self.camera)
        return self.camera

    def setup_logger(self, name: str = "GlobalLogger") -> logging.Logger:
        """
        Create and configure a global logger.

        Args:
            name (str): The name of the logger.

        Returns:
            logging.Logger: Configured logger instance.
        """
        logs_dir = "logs"
        os.makedirs(logs_dir, exist_ok=True)  # Ensure the logs directory exists

        # Generate log file name based on the current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        log_filename = os.path.join(logs_dir, f"camera_app_{current_date}.log")

        logger = logging.getLogger(name)

        # Avoid adding handlers multiple times if the logger already exists
        if logger.hasHandlers():
            return logger

        logger.setLevel(logging.DEBUG)

        # File handler (logs to a file)
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setLevel(logging.INFO)

        # Console handler (logs to the terminal)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Log message format
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Attach handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
