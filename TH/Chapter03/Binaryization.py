#Created by Tran Phuoc Loi 2101076

import cv2 as cv

img = cv.imread('Lena.png',0) # tham so la 0 de chuyen sang anh xam
ret,th1 = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 11, 2)

cv.imshow('Image', img)
cv.imshow('BasicThreshold', th1)
cv.imshow('MeanThreshold', th2)
cv.imshow('GausstianThreshold', th3)
cv.waitKey()
cv.destroyAllWindows()