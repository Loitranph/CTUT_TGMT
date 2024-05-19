#Created by Tran Phuoc Loi 2101076

import cv2 as cv
import numpy as np

img = cv.imread('Color.png')

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

T = np.mean(gray[0:10,0:10])-20

print(T)

_, th = cv.threshold(gray, T, 255, cv.THRESH_BINARY_INV)

cv.imshow('2101076', th)

k= cv.waitKey(0)

if k == 27:

    cv2.destroyWindow()