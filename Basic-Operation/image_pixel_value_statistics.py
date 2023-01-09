# For Pixel Value

import cv2 as cv
import numpy as np
path = "Basic-Operation/"
src = cv.imread(path + "merve.jpg", cv.IMREAD_GRAYSCALE)

# minMaxLoc
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(src)
print("min_value: %.2f, max_value: %.2f" % (min_val, max_val))
print("min_loc: ", min_loc, " max_loc: ", max_loc)

# meanStdDev (Ortalama ve Standart Sapma Bilgileri)
means, stddev = cv.meanStdDev(src)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

src[np.where(src < means)] = 0 # Siyah
src[np.where(src > means)] = 255 # Beyaz

cv.imshow("Binary", src)
cv.waitKey(10000)
cv.destroyAllWindows