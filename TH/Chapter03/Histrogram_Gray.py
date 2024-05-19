#Created by Tran Phuoc Loi 2101076

import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Lena.png',0)
cv.imshow('AnhGoc',img)
plt.hist(img.ravel(),256,[0,255])
plt.show()
cv.waitKey()
cv.destroyAllWindows()