import cv2

video_path = "src/SkiHUD-demo-video.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
out = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*"H264"),
    fps,
    (cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create(nfeatures=2000)
    kp, des = orb.detectAndCompute(gray_image, None)
    kp_image = cv2.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)
    out.write(kp_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
