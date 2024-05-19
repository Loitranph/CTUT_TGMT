#Created by Tran Phuoc Loi 2101076

import cv2 as cv
img1 = cv.imread('Lighthouse1.jpg')
img2=cv.cvtColor(img1,cv.COLOR_RGB2GRAY)
cv.imshow('Image1', img1)
cv.imshow('Image2', img2)
k = cv.waitKey()
if k == 27:
    cv.destroyAllWindows()