#Created by Tran Phuoc Loi 2101076

import cv2 as cv
img = cv.imread('ChimCanhCut.jpg')
num_width, num_height = img.shape[:2]
print(img.shape[:2])
print(num_width)
print(num_height)
rotation_matrix = cv.getRotationMatrix2D((num_width/2, num_height/2), 45, 1)
img_rotation = cv.warpAffine(img, rotation_matrix, (num_width, num_height))

cv.imshow('Rotation', img)
cv.waitKey()
cv.imshow('Rotation', img_rotation)
cv.waitKey()