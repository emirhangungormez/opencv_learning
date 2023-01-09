# For Pixel Value

import cv2 as cv
import numpy as np
path = "Basic-Operation/"
m = cv.imread(path + "merve.jpg")

print(m.shape)

cv.imshow("Merve", m)
g = cv.cvtColor(m, cv.COLOR_BGR2GRAY) # Resmi tek boyuta indiriyoruz.
gray = np.float32(g) # Matematiksel islemlerde kolaylik saglamasi icin

# Norm_MinMax
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_val, max_val))
means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

# 0 - 1 arasina cevirme
dst = np.zeros(gray.shape, dtype = np.float32)
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
cv.imshow("NormMax", np.uint8(dst*255))
cv.waitKey(10000)

# Yeniden Norm_MinMax
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(dst)
print("min_value: %.2f, max_value: %.2f" % (min_val, max_val))
means, stddev = cv.meanStdDev(dst)
print("mean: %.2f, stddev: %.2f" % (means, stddev))