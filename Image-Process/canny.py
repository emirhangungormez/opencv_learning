# Goruntulerin piksellerinin renk farklilasmasindan
# yararlanarak programatik olarak kenar tespiti yapistir

import cv2 as cv
import numpy as np

src = cv.imread("Image-Process\homelander2.jpg")
cv.imshow("homelander", src)
cv.waitKey(0)

edge = cv.Canny(src, 50, 150)
cv.imshow("homelander", edge)
cv.waitKey(0)