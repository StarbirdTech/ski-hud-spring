import cv2
import numpy as np


def wrap_equirectangular_video(input_file, output_file):
    cap = cv2.VideoCapture(input_file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        wrapped_frame = wrap_equirectangular_frame(frame)

        out.write(wrapped_frame)

        cv2.imshow("Wrapped Equirectangular Video", wrapped_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def wrap_equirectangular_frame(frame):
    height, width = frame.shape[:2]

    # Calculate output dimensions for the wrapped video
    output_width = width * 2
    output_height = height

    # Create a blank output frame
    output_frame = np.zeros((output_height, output_width, 3), dtype=np.uint8)

    # Wrap each pixel from the input frame to the output frame
    for x in range(output_width):
        for y in range(output_height):
            theta = (x / output_width) * 2 * np.pi
            phi = (y / output_height) * np.pi

            source_x = int(width * (theta / (2 * np.pi)))
            source_y = int(height * (phi / np.pi))

            output_frame[y, x] = frame[source_y, source_x]

    return output_frame


# Example usage
input_video_file = "/Users/arisinert/Git/ski-hud-spring/src/360vid2.mp4"
output_video_file = "wrapped_video.mp4"
wrap_equirectangular_video(input_video_file, output_video_file)
