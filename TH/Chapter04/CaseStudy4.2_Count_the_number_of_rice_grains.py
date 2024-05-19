# Created by Tran Phuoc Loi 2101076
import cv2
import cv2 as cv

img = cv.imread('Rice.png', 0)

th = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, -3)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

openn = cv.morphologyEx(th, cv.MORPH_OPEN, kernel)

canny = cv.Canny(openn, 200, 250)

countours, _ = cv.findContours(canny, cv.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv.drawContours(img,countours,-1,(0,255,0),2)

sohatgao = len(countours)

cv.putText(img,"So Hat Gao: "+ str(sohatgao),(10,30),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
cv.putText(th,"So Hat Gao: "+ str(sohatgao),(10,30),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
cv.putText(openn,"So Hat Gao: "+ str(sohatgao),(10,30),cv.FONT_ITALIC,1,(0,255,0),3)

cv.imshow('2101076', img)
cv.imshow('Thresh', th)
cv.imshow('OPEN', openn)

cv.waitKey(0)
cv.destroyAllWindows()