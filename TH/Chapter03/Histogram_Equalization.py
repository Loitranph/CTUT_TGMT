#Created by Tran Phuoc Loi 2101076

import cv2 as cv
import numpy as np
img = cv.imread('Monkey.png',0)
equ = cv.equalizeHist(img)
cv.imwrite('MonkeyOut.png',equ)