#Created by Tran Phuoc Loi 2101076

import cv2 as cv
import numpy as np

def onTrackbarChange(x):
    pass

image = cv.imread('ChimCanhCut.jpg')

hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

cv.namedWindow('HSV Range Selector')

cv.createTrackbar('Low H', 'HSV Range Selector', 0, 255, onTrackbarChange)
cv.createTrackbar('Low S', 'HSV Range Selector', 0, 255, onTrackbarChange)
cv.createTrackbar('Low V', 'HSV Range Selector', 0, 255, onTrackbarChange)

cv.createTrackbar('High H', 'HSV Range Selector', 255, 255, onTrackbarChange)
cv.createTrackbar('High S', 'HSV Range Selector', 255, 255, onTrackbarChange)
cv.createTrackbar('High V', 'HSV Range Selector', 255, 255, onTrackbarChange)

while True:

    low_h = cv.getTrackbarPos('Low H', 'HSV Range Selector')
    high_h = cv.getTrackbarPos('High H', 'HSV Range Selector')
    low_s = cv.getTrackbarPos('Low S', 'HSV Range Selector')
    high_s = cv.getTrackbarPos('High S', 'HSV Range Selector')
    low_v = cv.getTrackbarPos('Low V', 'HSV Range Selector')
    high_v = cv.getTrackbarPos('High V', 'HSV Range Selector')

    lower_bound = np.array([low_h, low_s, low_v])
    upper_bound = np.array([high_h, high_s, high_v])
    mask = cv.inRange(hsv_image, lower_bound, upper_bound)

    result = cv.bitwise_and(image, image, mask=mask)

    cv.imshow('Original Image', image)
    cv.imshow('Mask', mask)
    cv.imshow('Result', result)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()