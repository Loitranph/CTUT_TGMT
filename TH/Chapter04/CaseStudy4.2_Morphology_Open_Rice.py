# Created by Tran Phuoc Loi 2101076

import cv2 as cv

img = cv.imread('Rice.png', 0)

th = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, -3)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

openn = cv.morphologyEx(th, cv.MORPH_OPEN, kernel)

cv.imshow('2101076', img)
cv.imshow('Thresh', th)
cv.imshow('OPEN', openn)

cv.waitKey(0)
cv.destroyAllWindows()