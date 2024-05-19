from pypylon import pylon
import cv2
import imutils as im

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

while True:
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
    if grabResult.GrabSucceeded():

        image = converter.Convert(grabResult)
        fra_cam = image.GetArray()
        #print(fra_cam.shape) (2748, 3840, 3)
        frame = im.resize(fra_cam, width=640, height=480)

        ###############################################
        #code here
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        ###############################################
        #cv2.imshow('Frame',frame)
        cv2.imshow('a',img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
        camera.close()
cv2.destroyAllWindows()