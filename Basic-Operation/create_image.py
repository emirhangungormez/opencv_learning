import cv2 as cv
import numpy as np
path = "Basic-Operation/"
img = cv.imread(path + "yoda.jpg") # Okuma yapar.
cv.namedWindow('Yoda',cv.WINDOW_AUTOSIZE)

m1 = np.copy(img)
m2 = img

# Resmi tamamen siyah yapar.
m3 = np.zeros(img.shape, img.dtype)
cv.imshow("Siyah", m3)
cv.waitKey(10000)

# Resmi tamamen gri yapar. (512 x 152 boyutunda)
m4 = np.zeros([512,512], np.uint8)
m4[:,:]=127
cv.imshow("Gri", m4)
cv.waitKey(10000)
cv.destroyAllWindows