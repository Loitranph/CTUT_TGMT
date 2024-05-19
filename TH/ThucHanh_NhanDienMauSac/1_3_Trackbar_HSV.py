import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")

cv2.resizeWindow("Tracking", 500, 400)

cv2.createTrackbar("Low_H", "Tracking", 0, 180, nothing)
cv2.createTrackbar("Low_S", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Low_V", "Tracking", 0, 255, nothing)

cv2.createTrackbar("High_H", "Tracking", 180, 180, nothing)
cv2.createTrackbar("High_S", "Tracking", 255, 255, nothing)
cv2.createTrackbar("High_V", "Tracking", 255, 255, nothing)

while True:
    ret, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Low_H", "Tracking")
    l_s = cv2.getTrackbarPos("Low_S", "Tracking")
    l_v = cv2.getTrackbarPos("Low_V", "Tracking")

    h_h = cv2.getTrackbarPos("High_H", "Tracking")
    h_s = cv2.getTrackbarPos("High_S", "Tracking")
    h_v = cv2.getTrackbarPos("High_V", "Tracking")

    l_hsv = np.array([l_h, l_s, l_v])
    h_hsv = np.array([h_h, h_s, h_v])

    mask = cv2.inRange(hsv, l_hsv, h_hsv)

    res = cv2.bitwise_and(img, img, mask=mask)

    #cv2.imshow("frame", img)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
