import cv2
import time


def estimate_remaining_time(current_frame, total_frames, start_time):
    elapsed_time = time.time() - start_time
    frames_remaining = total_frames - current_frame
    seconds_per_frame = elapsed_time / current_frame
    remaining_time = frames_remaining * seconds_per_frame
    return remaining_time


video_path = "cache/NoOverlay.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
out = cv2.VideoWriter(
    "cache/SkiHUD-winter1-cv.mp4",
    cv2.VideoWriter_fourcc(*"avc1"),
    fps,
    (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))),
)
start_time = time.time()
print(f"Total frames: {frame_count}")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create(nfeatures=2000)
    kp, des = orb.detectAndCompute(gray_image, None)
    kp_image = cv2.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)
    out.write(kp_image)

    current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    remaining_time = estimate_remaining_time(current_frame, frame_count, start_time)
    print(
        f"Frame {current_frame+1}/{frame_count} | Remaining time: {remaining_time:.2f} seconds",
        end="\r",
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
