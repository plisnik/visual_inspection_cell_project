import cv2
import os
import numpy as np

# Not needed – I’ll generate it online where it can be saved as SVG/PDF and has exact dimensions:
# https://calib.io/pages/camera-calibration-pattern-generator
# https://chev.me/arucogen/

# Otherwise, I’d have to create it in pixels

def generate_aruco_markers(start_id, num_markers, marker_size, output_dir, dictionary_name=cv2.aruco.DICT_6X6_250):
    """
    Generates and saves ArUco markers.
    
    Args:
        start_id (int): Starting marker ID
        num_markers (int): Number of markers to generate
        marker_size (int): Marker size in pixels
        dictionary_name (int): Type of ArUco dictionary
    """
    
    # Initialize ArUco dictionary
    aruco_dict = cv2.aruco.getPredefinedDictionary(dictionary_name)
    
    # Generate markers
    for marker_id in range(start_id, start_id + num_markers):
        # Create marker image
        marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)
        marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size, marker_image)
        
        # Add white border
        border_size = 20
        marker_with_border = cv2.copyMakeBorder(
            marker_image,
            border_size,
            border_size,
            border_size,
            border_size,
            cv2.BORDER_CONSTANT,
            value=[255, 255, 255]
        )
        
        # Save marker image
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

    squareLength = 40   # Here, our measurement unit is "centimeter"
    markerLength = 30   # Here, our measurement unit is "centimeter"
    board = cv2.aruco.CharucoBoard((5, 7), squareLength, markerLength, dict_aruco)
    board_img = board.generateImage((600, 800))
    cv2.imshow("board", board_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    ret = cv2.imwrite(path_mark, board_img)
