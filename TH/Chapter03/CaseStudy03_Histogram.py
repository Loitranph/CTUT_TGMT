#Created by Tran Phuoc Loi 2101076

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('number.jpg',0)
equ = cv.equalizeHist(img)

cv.imshow('Image',img)
cv.waitKey(0)

T = 200

plt.hist(img.ravel(),256,[T,T])
plt.show()

cv.imshow('Image',equ)
cv.waitKey(0)

plt.hist(equ.ravel(),256,[T,T])
plt.show()

cv.imwrite('NumbeOut.png',equ)