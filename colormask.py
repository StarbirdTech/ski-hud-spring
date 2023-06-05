import cv2
import numpy as np

# Load the video
video = cv2.VideoCapture(
    "/Users/arisinert/Git/ski-hud-spring/src/SkiHUD-NoOverlay-BoundingBoxes.mp4"
)

# Define the RGB values for #FF573D
rgb_color = (255, 87, 61)

# Define the range around the RGB color
color_range = 50

# Convert the RGB color to HSV
hsv_color = cv2.cvtColor(np.uint8([[rgb_color]]), cv2.COLOR_BGR2HSV)[0][0]

# Define the range of the color in HSV
lower_color = np.array(
    [hsv_color[0] - color_range, hsv_color[1] - 50, hsv_color[2] - 50]
)
upper_color = np.array(
    [hsv_color[0] + color_range, hsv_color[1] + 50, hsv_color[2] + 50]
)

# Process each frame of the video
while True:
    ret, frame = video.read()

    if not ret:
        break

    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the color range
    color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    # Bitwise-AND the original frame with the mask to obtain the color regions
    color_frame = cv2.bitwise_and(frame, frame, mask=color_mask)

    # Display the resulting frame
    cv2.imshow("Color Filtered Video", color_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close all windows
video.release()
cv2.destroyAllWindows()
