# Goruntulerde binary goruntuye cevirme islemi yapılarak goruntudeki
# daireler hoffman yontemi ile saptanmistir

import cv2 as cv
import numpy as np

def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image, t, t*2)
    cv.imshow("canny_output", canny_output)
    return canny_output

src = cv.imread("Image-Process\tokens.jpg")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (9,9) , 2, 2)

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp=1, minDist=10, param1=100, param2=50, minRadius=20, maxRadius=100)

for c in circles[0,:]:
    print(c)
    cx, cy, r = c
    cv.circle(src, (cx, cy), 2, (0,255,0), 2, 8, 0)
    cv.circle(src, (cx, cy), r, (0,0,255), 2, 8, 0)

cv.imshow("hough line demo", src)
cv.waitKey(0)