#Created by Tran Phuoc Loi 2101076

import cv2
from matplotlib import pyplot as plt
img = cv2.imread('Lena_Noise.jpg')
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
bilateral_rgb = cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB)
plt.subplot(211),plt.imshow(img_rgb),plt.title('Lena_Noise')
plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(bilateral_rgb),plt.title('Lena_Noise-Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()