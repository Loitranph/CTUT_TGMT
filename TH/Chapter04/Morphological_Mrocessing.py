#Created by Tran Phuoc Loi 2101076

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Chuj.png', 0)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

plt.figure()
plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(dilation), plt.title('Dilation')
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(opening), plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(closing), plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(gradient), plt.title('Gradient')
plt.xticks([]), plt.yticks([])
plt.show()