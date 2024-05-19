#Created by Tran Phuoc Loi 2101076

import cv2 as cv
img = cv.imread('circles.png')
print('Gia tri RGB')
print(img)
#chuyen sang khong gian mau HSV
img_hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
print('Gia tri HSV')
print(img_hsv)
cv.imshow('Color RGB',img) #hien thi img
cv.imshow('Color HSV',img_hsv) #hien thi img hsv
cv.waitKey(0)
cv.destroyAllWindows()