#Created by Tran Phuoc Loi 2101076

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Rose_SaltAndPepper.jpg')
median = cv.medianBlur(img, 5)
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
median_rgb = cv.cvtColor(median,cv.COLOR_BGR2RGB)

plt.subplot(211),plt.imshow(img_rgb),plt.title('Rose_SaltAndPepper')
plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(median_rgb),plt.title('Rose_SaltAndPepper-Blurred')
plt.xticks([]), plt.yticks([])
plt.show()