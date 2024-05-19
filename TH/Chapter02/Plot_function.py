#Created by Tran Phuoc Loi 2101076

import cv2 as cv
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img = cv.line(img,(0,0),(511,511),(0,255,0),5)
img = cv.rectangle(img,(10,10),(300,300),(255,0,0),3)
img = cv.circle(img,(300,300), 100, (0,0,255), -1)
#ve chu OpenCV
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,300), font,4,(0,255,255),5,cv.LINE_AA)
cv.imshow('Plot', img)
cv.imwrite('Lighthouse2.jpg', img)
cv.waitKey()