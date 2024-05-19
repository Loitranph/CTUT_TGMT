#Created by Tran Phuoc Loi 2101076

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('Monkey.png',0)
equ = cv.equalizeHist(img)

cv.imshow('Image',img)
cv.waitKey(0)
plt.hist(img.ravel(),256,[0,255])
plt.show()

cv.imshow('Image',equ)
cv.waitKey(0)
plt.hist(equ.ravel(),256,[0,255])
plt.show()

cv.imwrite('MonkeyOut.png',equ)