#Created by Tran Phuoc Loi 2101076

import cv2 as cv
img = cv.imread('ChimCanhCut.jpg')
print('ChimCanhCut.jpg', img.shape)

x = 100
y = 200
h = 200
w = 400

img_crop = img[y : y+h, x : x+w]
cv.imwrite('OutCrop.jpg', img_crop)

cv.imshow('Image',img_crop)
cv.waitKey(0)
print('OutCrop.jpg', img_crop.shape)