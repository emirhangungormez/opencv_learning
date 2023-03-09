# Hog yontemiyle goruntu icindeki insanlar tespit edilmis ve isaretlenmistir.

import cv2 as cv
import numpy as np

src = cv.imread("Image-Process\yayalar.jpg")

hog = cv.HOGDescriptor()

hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

rects, weights = hog.detectMultiScale(src, winStride=(4,4), padding=(8,8), scale=1.25)

for(x,y,w,h) in rects:
    cv.rectangle(src, (x,y), (x + w, y +h), (0, 255, 0), 2)

cv.imshow('result', src)
cv.waitKey(0)