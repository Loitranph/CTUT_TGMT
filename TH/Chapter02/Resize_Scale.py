#Created by Tran Phuoc Loi 2101076

import cv2 as cv

img = cv.imread('ChimCanhCut.jpg')
print(img.shape)

new_width = 800
new_height = 400

img_resized1 = cv.resize(src=img, dsize=(new_width, new_height))
cv.imwrite('OutputResize.jpg', img_resized1)
print(img_resized1.shape)

fx = 0.5
fy = 1.0

img_resized2 = cv.resize(src=img, dsize=None, fx=fx, fy=fy)
cv.imwrite('OutputResize2.jpg', img_resized2)
print(img_resized2.shape)

cv.imshow('Image',img_resized2)
cv.waitKey(0)
cv.imshow('Image',img_resized1)
cv.waitKey(0)