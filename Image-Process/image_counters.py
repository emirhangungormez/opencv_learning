# Goruntuun sahip oldugu tum noktalari birlestiren kapali bir
# egri olusturarak kontur olusturması

import cv2 as cv
import numpy as np

def thresholding_demo(image):
    dst = cv.GaussianBlur(image, (3,3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    cv.imshow("binary", binary)
    return binary

def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image, t, t*2)
    cv.imshow("canny_output", canny_output)
    return canny_output

src = cv.imread("Image-Process\homelander1.jpg")
cv.namedWindow("homelander", cv.WINDOW_AUTOSIZE)
cv.imshow("homelander", src)
cv.waitKey(0)

binary = thresholding_demo(src)
canny = canny_demo(src)

contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    cv.drawContours(src, contours, c,(0,0,255), 2, 8)

cv.imshow("cizim", src)
cv.waitKey(0)