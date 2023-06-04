import cv2
import math


def calculate_distance(object_width, focal_length, object_pixel_width):
    # Calculate distance using the formula: distance = (object_width * focal_length) / object_pixel_width
    distance = (object_width * focal_length) / object_pixel_width
    return distance


def main():
    # Set the known object width in centimeters
    object_width = 20

    # Set the focal length of your webcam (you need to calibrate this value)
    focal_length = 1000

    # Initialize the video capture
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow("Frame", frame)

        # Convert the frame to grayscale for better object detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform object detection or tracking here to get the pixel width of the object

        # Calculate the distance using the known object width and pixel width
        object_pixel_width = (
            100  # Replace with the actual pixel width of the detected/tracked object
        )
        distance = calculate_distance(object_width, focal_length, object_pixel_width)
        print("Distance to object:", distance, "cm")

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
