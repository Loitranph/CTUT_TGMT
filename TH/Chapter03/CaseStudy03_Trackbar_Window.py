#Created by Tran Phuoc Loi 2101076

import cv2 as cv

def on_trackbar(val):
    pass

cv.namedWindow('TPLOI')
cv.namedWindow('2101076')

cv.createTrackbar('T', 'TPLOI', 0, 255, on_trackbar)

while True:
    img = cv.imread('number.jpg')

    if img is None:
        print("Không thể đọc ảnh.")
        break

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    T = cv.getTrackbarPos('T', 'TPLOI')

    _, th = cv.threshold(gray, T, 255, cv.THRESH_BINARY_INV)

    cv.imshow('TPLOI', img)
    cv.imshow('2101076', th)

    k = cv.waitKey(1)

    if k == 27:
        cv.destroyAllWindows()
        break