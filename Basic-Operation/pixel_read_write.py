import cv2 as cv
import numpy as np
path = "Basic-Operation/"
img = cv.imread(path + "yoda.jpg") # Okuma yapar.
cv.namedWindow('Yoda',cv.WINDOW_AUTOSIZE)

h = img.shape[0]
w = img.shape[1]
ch = img.shape[2]

print("h ,w, ch", h, w, ch)

for row in range(h):
    for col in range(w):
        b, g, r = img[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row, col] = [b, g, r]

cv.imshow("Yoda", img)
cv.waitKey(1000)
cv.destroyAllWindows