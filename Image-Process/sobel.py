# Goruntulerde sobel filtre kullanilarak turev
# hesaplanmistir ve kenal algilamasi saglanmiştir

import cv2 as cv
import numpy as np

src = cv.imread("Image-Process\yoda.jpg")

h, w = src.shape[:2]
x_grad = cv.Sobel(src, cv.CV_32F, 1 ,0) # CV_32F (turev alma islemi)
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)

x_grad = cv.convertScaleAbs(x_grad)
y_grad = cv.convertScaleAbs(y_grad)

cv.imshow("x_grad" , x_grad)
cv.waitKey(1000)

cv.imshow("y_grad" , y_grad)
cv.waitKey(1000)

dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)
cv.imshow("dst" , dst)
cv.waitKey(0)