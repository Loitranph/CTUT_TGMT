from pypylon import pylon
import cv2
import numpy as np

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
def nothing(x):
    pass


cv2.namedWindow("Tracking")

cv2.resizeWindow("Tracking", 500, 400)

cv2.createTrackbar("Low_H", "Tracking", 0, 180, nothing)
cv2.createTrackbar("Low_S", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Low_V", "Tracking", 0, 255, nothing)

cv2.createTrackbar("High_H", "Tracking", 180, 180, nothing)
cv2.createTrackbar("High_S", "Tracking", 255, 255, nothing)
cv2.createTrackbar("High_V", "Tracking", 255, 255, nothing)
while True:
    grabResult = camera.RetrieveResult(500, pylon.TimeoutHandling_ThrowException)
    if grabResult.GrabSucceeded():

        image = converter.Convert(grabResult)
        fra_cam = image.GetArray()
        #img = im.resize(fra_cam, width=800, height=400)
        ###############################################
        hsv = cv2.cvtColor(fra_cam, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos("Low_H", "Tracking")
        l_s = cv2.getTrackbarPos("Low_S", "Tracking")
        l_v = cv2.getTrackbarPos("Low_V", "Tracking")

        h_h = cv2.getTrackbarPos("High_H", "Tracking")
        h_s = cv2.getTrackbarPos("High_S", "Tracking")
        h_v = cv2.getTrackbarPos("High_V", "Tracking")

        l_hsv = np.array([l_h, l_s, l_v])
        h_hsv = np.array([h_h, h_s, h_v])

        mask = cv2.inRange(hsv, l_hsv, h_hsv)

        res = cv2.bitwise_and(fra_cam, fra_cam, mask=mask)

        ###############################################
        cv2.imshow('Window', mask)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
        camera.close()
cv2.destroyAllWindows()
