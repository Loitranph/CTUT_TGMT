#Created by Tran Phuoc Loi 2101076

import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("Lena.png")
b, g, r = cv.split(img)
cv.imshow("img", img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)
plt.hist(b.ravel(), 256, [0, 255])
plt.hist(g.ravel(), 256, [0, 255])
plt.hist(r.ravel(), 256, [0, 255])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()