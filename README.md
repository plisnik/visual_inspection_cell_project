# Automated Hand-Eye Calibration for Robotic Workstations

This repository contains the implementation of an automated hand-eye calibration system for robotic workstations using machine vision techniques. The project was developed as part of a Master's thesis at Brno University of Technology, Faculty of Mechanical Engineering, in collaboration with INTEMAC.

## Project Overview

The application provides a comprehensive solution for calibrating robot-camera systems, allowing for accurate spatial coordination between a robot and a vision system. It features:

- Support for both **eye-in-hand** (camera mounted on robot) and **eye-to-hand** (stationary camera) configurations
- Automated calibration sequence with minimal manual intervention
- User-friendly graphical interface
- Implementation of multiple hand-eye calibration methods
- Testing capabilities for validating calibration accuracy
- Support for collaborative robots (specifically tested with Universal Robots UR10e)

## System Requirements

### Hardware Requirements
- Universal Robots collaborative robot (tested with UR10e)
- Industrial camera with GigE Vision interface (tested with Basler ace 2 R a2A2448-23gcPRO)
- ChArUco calibration board
- Lighting system (optional but recommended)
- PC with network connection to robot and camera

### Software Requirements
- Python 3.8+
- PySide6 (Qt for Python)
- OpenCV 4.7+
- NumPy
- SciPy
- pypylon (Basler camera SDK)
- ur_rtde (Universal Robots RTDE interface)
- opcua (alternative control)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/plisnik/visual_inspection_cell_project.git
   ```

2. Install required packages and additional dependencies:
   - Basler pylon Camera Software Suite (for camera support)
   - Universal Robots RTDE package

## Project Structure

The repository is organized as follows:

```
├── scripts/                   # Main application code
│   ├── GUI/                   # Graphical user interface components
│   │   ├── UI/                # PySide6 UI definition files
│   │   ├── global_data.py     # Singleton class for application state
│   │   ├── camera_thread.py   # Thread for camera operations
│   │   ├── camera_check.py    # Dialog for camera verification
│   │   └── ...                # Other GUI components
│   ├── utils/                 # Utility functions
│   │   ├── utilities.py       # General utility functions
│   │   ├── robot_interface.py # Robot communication interface
│   │   └── ...                # Other utility modules
│   ├── others/                # Utility functions
│   │   ├── error_calc.py      # Validation
│   │   └── ...                # Other scripts for use without app
│   ├── ur_robot_calib_params/ # Robot calibration parameters
│   │   ├── UR_calibration/    # Configuration files
│   │   └── ...                # Parameter handling modules
│   └── main.py                # Application entry point
├── data_sets/                 # Directory for calibration data
│   └── temporary_data_set/    # Working directory for calibration process
├── logs/                      # Application logs
├── models/                    # CAD models
├── LICENSE.md                 # License information
└── README.md                  # This file
```

## Usage

1. Start the application:
```bash
python scripts/main.py
```

2. In the Settings tab, enter the robot's IP address and check the connection.

3. In the Calibration tab:
   - Select the calibration configuration (eye-in-hand or eye-to-hand)
   - Configure the ChArUco board parameters
   - Select the calibration method
   - Click "Initial Adjustment" to position the robot/camera
   - Click "Start Calibration" to begin the automated process

4. The application will:
   - Move the robot to predefined positions
   - Capture images of the calibration pattern
   - Calculate the calibration matrix
   - Display the results on the Home tab

5. Save the calibration results for future use or test the calibration using the provided testing scenarios.

## Calibration Methods

The application implements several hand-eye calibration methods:

- Tsai and Lenz
- Park and Martin
- Horaud et al.
- Andreff et al.
- Daniilidis
- Li et al. (Robot-World/Hand-Eye)
- Shah (Robot-World/Hand-Eye)

## Testing

The system includes three testing scenarios:

1. **Basic Pick and Place**: Tests precision by picking up and placing objects marked with ArUco markers
2. **Form Manipulation**: Tests manipulation with a form that has predefined positions
3. **Precision Pointing**: Tests absolute positioning accuracy using a calibration needle

## Contributing

This project was developed as part of a Master's thesis and is primarily intended for academic purposes. However, contributions are welcome through pull requests.

## Author

Petr Lisník

## License
[MIT](https://choosealicense.com/licenses/mit/)
