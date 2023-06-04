import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Provide the camera's focal length in millimeters
focal_length_mm = (
    3.04  # Example value, please replace with the actual focal length of your camera
)

# Provide the camera sensor width in millimeters
sensor_width_mm = (
    4  # Example value, please replace with the actual sensor width of your camera
)


# model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
# model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
model_type = (
    "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)
)


midas = torch.hub.load("intel-isl/MiDaS", model_type)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
midas.to(device)
midas.eval()

midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
transform = (
    midas_transforms.dpt_transform
    if model_type in ["DPT_Large", "DPT_Hybrid"]
    else midas_transforms.small_transform
)

cap = cv2.VideoCapture(0)  # Open the default camera (index 0)

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    # Preprocess the frame
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    input_batch = transform(frame_rgb).to(device)

    with torch.no_grad():
        prediction = midas(input_batch)

        depth_map = (
            torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=frame.shape[:2],
                mode="bicubic",
                align_corners=False,
            )
            .squeeze()
            .cpu()
            .numpy()
        )

    # Normalize the depth map for visualization
    normalized_depth_map = cv2.normalize(
        depth_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U
    )

    # Calculate the average depth at the center of the screen
    center_y, center_x = frame.shape[:2]
    center_y //= 2
    center_x //= 2
    average_depth = np.mean(
        depth_map[center_y - 10 : center_y + 10, center_x - 10 : center_x + 10]
    )

    # Calculate the distance in inches
    distance_in_inches = (focal_length_mm * 25.4) / (average_depth * sensor_width_mm)

    # Display the depth map and distance
    cv2.imshow("Depth Map", normalized_depth_map)
    # Draw a circle at the center of the screen
    cv2.circle(frame, (center_x, center_y), 10, (0, 0, 255), -1)
    cv2.putText(
        frame,
        f"Distance: {distance_in_inches:.2f} inches",
        (30, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )
    cv2.imshow("Frame", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()  # Release the capture
cv2.destroyAllWindows()
