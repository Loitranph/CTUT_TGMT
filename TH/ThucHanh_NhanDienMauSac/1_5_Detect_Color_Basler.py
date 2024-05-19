from pypylon import pylon
import cv2
import numpy as np
import imutils as im

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

while True:
    grabResult = camera.RetrieveResult(800, pylon.TimeoutHandling_ThrowException)
    if grabResult.GrabSucceeded():

        image = converter.Convert(grabResult)
        frame = image.GetArray()
        frame = im.resize(frame, width=800, height=400)
        ###############################################
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        red_lower = np.array([0, 65, 200], np.uint8)
        red_upper = np.array([180, 255, 255], np.uint8)
        red_mask = cv2.inRange(hsv, red_lower, red_upper)
        red_cnt, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c_red in red_cnt:
            #print(cv2.contourArea(c_red))
            area1 = cv2.contourArea(c_red)
            if area1 > 50000:
                cv2.putText(frame, 'RED', (20, 40), 1, 3, (0, 0, 255), 2)

        green_lower = np.array([40, 70, 80], np.uint8)
        green_upper = np.array([70, 255, 255], np.uint8)
        green_mask = cv2.inRange(hsv, green_lower, green_upper)
        green_cnt, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c_green in green_cnt:
            #print(cv2.contourArea(c_green))
            area2 = cv2.contourArea(c_green)
            if area2 > 50000:
                cv2.putText(frame, 'GREEN', (20, 80), 1, 3, (0, 255, 0), 2)

        blue_lower = np.array([90, 60, 0], np.uint8)
        blue_upper = np.array([120, 255, 255], np.uint8)
        blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
        blue_cnt, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c_blue in blue_cnt:
            #print(cv2.contourArea(c_blue))
            area3 = cv2.contourArea(c_blue)
            if area3 > 50000:
                cv2.putText(frame, 'BLUE', (20, 120), 1, 3, (255, 0, 0), 2)

        ###############################################
        cv2.imshow('Window', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break
        camera.close()
cv2.destroyAllWindows()
