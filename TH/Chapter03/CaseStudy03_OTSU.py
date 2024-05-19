#Created by Tran Phuoc Loi 2101076

import cv2 as cv

img = cv.imread('number.jpg')

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5,5), 0)

T = 0

_, th = cv.threshold(blur, T, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

cv.imshow('2101076', th)

k= cv.waitKey(0)

if k == 27:

    cv2.destroyWindow()