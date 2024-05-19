#Created by Tran Phuoc Loi 2101076

import cv2
img = cv2.imread('Lena.png',0) 

ret,th1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('Image', img)
cv2.imshow('BasicThreshold', th1)
cv2.waitKey()
cv2.destroyAllWindows()