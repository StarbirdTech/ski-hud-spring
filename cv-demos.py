import cv2

video = cv2.VideoCapture()

image = cv2.imread("test1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(nfeatures=2000)
kp, des = orb.detectAndCompute(gray_image, None)
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 255, 0), flags=0)

cv2.imshow("ORB", kp_image)
cv2.waitKey()
