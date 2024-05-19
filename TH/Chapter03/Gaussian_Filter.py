#Created by Tran Phuoc Loi 2101076

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Lena_Noise.jpg')
gauss = cv.GaussianBlur(img, (5, 5), 0)
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gauss_rgb = cv.cvtColor(gauss, cv.COLOR_BGR2RGB)

plt.subplot(211),plt.imshow(img_rgb),plt.title('Lena_Noise')
plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(gauss_rgb),plt.title('Lena_Noise-Gauss')
plt.xticks([]), plt.yticks([])
plt.show()