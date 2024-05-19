# Created by Tran Phuoc Loi 2101076

import cv2 as cv

img = cv.imread('ViThuoc.png', 0)

blur = cv.medianBlur(img, 5)

_, th = cv.threshold(blur, 200, 255, cv.THRESH_BINARY)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (19, 19))

clo = cv.morphologyEx(th, cv.MORPH_CLOSE, kernel)

cv.imshow('Binary', th)
cv.imshow('CLOSE', clo)

cv.waitKey(0)
cv.destroyAllWindows()