# Goruntulerde sigma_s ve sigma_r argumanlari kullanilarak
# ana hatlari koruyarak filtreleme islemi gerceklestirilmistir.

import cv2 as cv
import numpy as np

src = cv.imread("Image-Process\homelander1.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(1)

h, w = src.shape[:2]
dst = cv.edgePreservingFilter(src, sigma_s=10, sigma_r=0.4, flags=cv.RECURS_FILTER)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = dst

result = cv.resize(result, (w,h //2))
cv.imshow("result", result)
cv.waitKey(1)