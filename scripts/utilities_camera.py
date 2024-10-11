import cv2
import numpy as np

def find_corners(image: np.ndarray, pattern_size: tuple) -> tuple:
    """
    Finds the corners of a chessboard pattern in the given image.

    This function checks if the image is colored and converts it to grayscale if it is.
    Then, it uses the OpenCV function to find the chessboard corners and refines their positions.

    Parameters:
        image (np.ndarray): The input image in which to find the chessboard corners.
        pattern_size (tuple): The number of inner corners per a chessboard row and column,
            defined as (number_of_inner_corners_x, number_of_inner_corners_y).

    Returns:
        tuple: A tuple containing:
            - found (bool): True if the corners were found, False otherwise.
            - corners (np.ndarray): An array of corner points if found, otherwise None.

    Notes:
        - The function uses OpenCV's findChessboardCorners and cornerSubPix methods.
        - It applies corner refinement to enhance the accuracy of the detected corner positions.
    """
    # Convert to grayscale if the image is colored (has 3 channels)
    if len(image.shape) > 2 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners in the image
    found, corners = cv2.findChessboardCorners(image, pattern_size)

    # Define termination criteria for corner refinement
    term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)

    # If corners are found, refine their positions
    if found:
        cv2.cornerSubPix(image, corners, (5, 5), (-1, -1), term)

    return found, corners

def draw_corners(image: np.ndarray, corners: np.ndarray, pattern_size: tuple) -> np.ndarray:
    """
    Draws the corners of a chessboard pattern on the given image.

    This function converts the input image to color (if it is in grayscale)
    and then uses OpenCV's drawChessboardCorners function to overlay the detected corners.

    Parameters:
        image (np.ndarray): The input image on which to draw the chessboard corners.
        corners (np.ndarray): An array of corner points detected in the image.
        pattern_size (tuple): The number of inner corners per a chessboard row and column,
            defined as (number_of_inner_corners_x, number_of_inner_corners_y).

    Returns:
        np.ndarray: The color image with the chessboard corners drawn on it.

    Notes:
        - The function assumes the input image is in grayscale or has been converted to grayscale.
        - The corners are drawn as green dots on the image.
    """
    # Convert the image to color if it is grayscale
    color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Draw the chessboard corners on the image
    cv2.drawChessboardCorners(color_image, pattern_size, corners, True)

    return color_image

def get_object_pose(object_points: np.ndarray, image_points: np.ndarray, 
                    camera_matrix: np.ndarray, dist_coeffs: np.ndarray) -> tuple:
    """
    Computes the pose of an object in 3D space given its corresponding 2D image points.

    This function uses the solvePnP algorithm from OpenCV to estimate the rotation and translation
    vectors that relate the 3D object points to the 2D image points based on the camera calibration data.

    Parameters:
        object_points (np.ndarray): A set of 3D points in the object coordinate space (Nx3).
        image_points (np.ndarray): A set of 2D points in the image plane corresponding to the object points (Nx2).
        camera_matrix (np.ndarray): The camera intrinsic matrix (3x3).
        dist_coeffs (np.ndarray): The distortion coefficients of the camera.

    Returns:
        tuple: A tuple containing:
            - rvec (np.ndarray): The rotation vector (3x1) representing the object's orientation.
            - tvec (np.ndarray): The translation vector (3x1) representing the object's position.

    Notes:
        - The rotation vector can be converted to a rotation matrix using cv2.Rodrigues.
        - The function returns flattened vectors for easier manipulation.
    """
    # Solve for the rotation and translation vectors
    ret, rvec, tvec = cv2.solvePnP(object_points, image_points, camera_matrix, dist_coeffs)

    return rvec.flatten(), tvec.flatten()

def calibrate_lens(image_list: list, pattern_points: np.ndarray, pattern_size: tuple) -> tuple:
    """
    Calibrates the camera lens using a list of images containing a chessboard pattern.

    This function finds corners in the provided images and computes the camera matrix and distortion coefficients
    using the cv2.calibrateCamera function from OpenCV.

    Parameters:
        image_list (list): A list of images (as numpy arrays) containing a chessboard pattern for calibration.
        pattern_points (np.ndarray): An array of object points corresponding to the chessboard corners.

    Returns:
        tuple: A tuple containing:
            - camera_matrix (np.ndarray): The intrinsic camera matrix (3x3).
            - dist_coeffs (np.ndarray): The distortion coefficients (5x1).

    Raises:
        Exception: If corners cannot be found in any of the images.

    Notes:
        - The function assumes a pre-defined set of object points corresponding to the chessboard corners.
        - It is essential that the chessboard pattern is consistent across the images for accurate calibration.
    """
    img_points, obj_points = [], []
    h, w = 0, 0

    # Loop through each image in the provided list
    for img in image_list:
        h, w = img.shape[:2]
        
        # Find corners in the chessboard pattern
        found, corners = find_corners(img,pattern_size)
        if not found:
            raise Exception("Chessboard calibration failed: Unable to find corners in the image.")

        img_points.append(corners.reshape(-1, 2))  # Reshape corners to 2D points
        obj_points.append(pattern_points)  # Add the corresponding object points

    # Initialize camera matrix and distortion coefficients
    camera_matrix = np.zeros((3, 3))
    dist_coeffs = np.zeros(5)

    # Calibrate the camera using the found image points and object points
    rms, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (w, h), None, None)

    return camera_matrix, dist_coeffs




