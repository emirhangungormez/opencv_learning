# ROI (Region of Interest)

import cv2 as cv

path = "Image-Process/"
src = cv.imread(path + "yoda.jpg")

h, w = src.shape[:2]
print(h, w)

img = src.copy()

roi = img[1:300,1:400,:]
roi = src.shape[:2]

cv.imshow('ROI',roi)
cv.waitKey(0)

img[0:345, 0:630, :] = roi # Resmin uzerine ekleme
cv.imshow('img', img)
cv.waitKey(0)