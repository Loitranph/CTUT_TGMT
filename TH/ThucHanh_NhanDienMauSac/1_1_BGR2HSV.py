import cv2
import numpy as np

img = np.uint8([[[255, 242, 0]]])
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img_hsv)