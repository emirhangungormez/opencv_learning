# Goruntuler normalize edilerek histogramları
# karsilastirilmis ve benzerlikler tespit edilmistir.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src1 = cv.imread("Image-Process\homelander1.jpg")
src2 = cv.imread("Image-Process\homelander2.jpg")
src3 = cv.imread("Image-Process\homelander3.jpg")

# cvtColor
hsv1 = cv.cvtColor(src1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3, cv.COLOR_BGR2HSV)

# calcHist
hist1 = cv.calcHist([hsv1], [0,1], None, [60,64], [0,180,0,256]) # kanal, taslak, boyut
hist2 = cv.calcHist([hsv2], [0,1], None, [60,64], [0,180,0,256])
hist3 = cv.calcHist([hsv3], [0,1], None, [60,64], [0,180,0,256])

# normalize
cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

# compareHist
cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)
cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL)