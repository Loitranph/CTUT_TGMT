#Created by Tran Phuoc Loi 2101076

import cv2 as cv
img = cv.imread('ChimCanhCut.jpg')
print(img.shape)
print(img)
cv.imshow('Image', img)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    img1 = cv.imwrite('ChimCanhCut.png', img)
cv.destroyAllWindows()