# Goruntulerin piksellerinin esik degerine gore siyah ya da
# beyaz olarak guncellenmesi islemi yapilmistir

import cv2 as cv
import numpy as np

src = cv.imread("Image-Process\homelander1.jpg")
cv.namedWindow("homelander", cv.WINDOW_AUTOSIZE)
cv.imshow("homelander", src)
cv.waitKey(0)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

h, w = src.shape[:2]
cv.imshow("binary", binary)
cv.waitKey(0)
