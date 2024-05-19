#Created by Tran Phuoc Loi 2101076

import cv2 as cv
import numpy as np
img = cv.imread('Color.png')
img_hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

cv.imshow('RGB',img)
cv.imshow('HSV',img_hsv)

min_color = np.array([26, 250, 250])
max_color = np.array([30, 255, 255])
mask = cv.inRange(img_hsv, min_color, max_color)
cv.imshow('Mask', mask)
final = cv.bitwise_and(img, img, mask = mask)

cv.imshow('Final', final)
cv.waitKey()
cv.destroyAllWindows()