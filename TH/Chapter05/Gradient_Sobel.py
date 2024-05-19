Created by Tran Phuoc Loi

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("Sudoku.jpg", 0)
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
titles = ['image', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, sobelX, sobelY, sobelCombined]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
