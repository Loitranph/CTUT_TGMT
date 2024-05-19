#Created by Tran Phuoc Loi 2101076

import cv2 as cv
import numpy as np

img = cv.imread('GauTruc.png')
alpha = 1
beta = 40
Img_new = cv.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

cv.imwrite('img_new.jpg', Img_new)
cv.imshow('Image',img)
cv.waitKey(0)
cv.imshow('Image',Img_new)
cv.waitKey(0)