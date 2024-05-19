#Created by Tran Phuoc Loi 2101076

import numpy as np
import cv2 as cv
rectangle = np.zeros((300, 300), dtype = "uint8")
cv.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
circle = np.zeros((300, 300), dtype = "uint8")
cv.circle(circle, (150, 150), 150, 255, -1)
bitwiseAnd = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwiseAnd)
cv.waitKey(0)
bitwiseOr = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitwiseOr)
cv.waitKey(0)
bitwiseXor = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", bitwiseXor)
cv.waitKey(0)
bitwiseNot = cv.bitwise_not(circle)
cv.imshow("NOT", bitwiseNot)
cv.waitKey(0)