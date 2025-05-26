import cv2
import os
import numpy as np

# Not needed – I’ll generate it online where it can be saved as SVG/PDF and has exact dimensions:
# https://calib.io/pages/camera-calibration-pattern-generator
# https://chev.me/arucogen/

# Otherwise, I’d have to create it in pixels

def generate_aruco_markers(
    start_id: int, 
    num_markers: int, 
    marker_size: int, 
    output_dir: str, 
    dictionary_name: int = cv2.aruco.DICT_6X6_250
    ) -> None:
    """
    Generates and saves ArUco markers to specified directory.
    
    This function creates a series of ArUco markers with sequential IDs, adds white borders
    around them for better detection, and saves them as PNG images. The markers are generated
    using OpenCV's ArUco module with a specified dictionary type.
    
    Parameters:
        start_id (int): Starting marker ID for the sequence (e.g., 0, 10, 100)
        num_markers (int): Number of markers to generate sequentially
        marker_size (int): Size of the marker in pixels (square format)
        output_dir (str): Directory path where marker images will be saved
        dictionary_name (int): Type of ArUco dictionary to use (default: DICT_6X6_250)
    
    Returns:
        None
    
    Notes:
        - Each marker is saved as "aruco_marker_{ID}.png" in the output directory
        - A 20-pixel white border is added around each marker for better detection
        - The function uses OpenCV's ArUco module for marker generation
        - Output directory must exist before calling this function
    """
    
    # Initialize ArUco dictionary for marker generation
    aruco_dict = cv2.aruco.getPredefinedDictionary(dictionary_name)
    
    # Generate markers sequentially from start_id to start_id + num_markers
    for marker_id in range(start_id, start_id + num_markers):
        # Create black marker image canvas
        marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)
        
        # Generate ArUco marker pattern on the canvas
        marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size, marker_image)
        
        # Add white border around marker for better detection and printing
        border_size = 20
        marker_with_border = cv2.copyMakeBorder(
            marker_image,
            border_size,  # top border
            border_size,  # bottom border
            border_size,  # left border
            border_size,  # right border
            cv2.BORDER_CONSTANT,
            value=[255, 255, 255]  # white color
        )
        
        # Save marker image to output directory
        filename = output_dir / f"aruco_marker_{marker_id}.png"
        cv2.imwrite(str(filename), marker_with_border)
        print(f"Marker {marker_id} was saved to: {filename}")


if __name__ == "__main__":

    # Create directory for saving markers
    output_dir = ''
    generate_aruco_markers(
        start_id=0,         # Start from ID 0
        num_markers=1,      # Generate 1 marker
        marker_size=100,    # Marker size in pixels
        output_dir=output_dir,
        dictionary_name=cv2.aruco.DICT_6X6_250  # Use 6x6 dictionary
    )

    # Create ChArUco board
    dir_mark = 'charuco_boards'
    path_mark = os.path.join(dir_mark, 'charuco_board_X.jpg')

    dict_aruco = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dict_aruco, parameters)

    squareLength = 40   
    markerLength = 30   
    board = cv2.aruco.CharucoBoard((5, 7), squareLength, markerLength, dict_aruco)
    board_img = board.generateImage((600, 800))
    cv2.imshow("board", board_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    ret = cv2.imwrite(path_mark, board_img)
