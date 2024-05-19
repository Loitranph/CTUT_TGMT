from pypylon import pylon
import cv2

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

while True:
    grabResult = camera.RetrieveResult(100, pylon.TimeoutHandling_ThrowException)
    if grabResult.GrabSucceeded():

        image = converter.Convert(grabResult)
        frame = image.GetArray()
        #img = im.resize(fra_cam, width=800, height=400)
        ###############################################
        #code here
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        height, width, ret = frame.shape
        cx = int(width / 2)
        cy = int(height / 2)

        # Chon gia tri diem anh
        pixel_center = hsv_frame[cx, cy]
        cv2.circle(frame, (cx, cy), 100, (255, 0, 0), 3)
        #print(pixel_center)
        hue_value = pixel_center[0]
        color = "Undefined"

        if hue_value < 9:
            color = "RED"

        elif hue_value > 45 and hue_value < 78:
            color = "GREEN"

        elif hue_value > 95 and hue_value < 131:
            color = "BLUE"

        cv2.putText(frame, color, (30, 30), 0, 1, (0, 0, 255), 3)
        ###############################################
        cv2.imshow('img', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
        camera.close()
cv2.destroyAllWindows()
