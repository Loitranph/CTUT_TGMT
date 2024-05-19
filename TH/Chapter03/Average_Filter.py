#Created by Tran Phuoc Loi 2101076

import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Lena_Noise.jpg')
average = cv.blur(img, (5,5))
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
average_rgb = cv.cvtColor(average, cv.COLOR_BGR2RGB)
plt.subplot(121),plt.imshow(img_rgb),plt.title('Lena_Noise')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(average_rgb),plt.title('Lena_Noise-Blurred')
plt.xticks([]), plt.yticks([])
plt.show()