import cv2 as cv
import numpy as np
path = "Image-Process/"
img = cv.imread(path + "yoda.jpg")

# Shifting (Kaydirma)
rows = img.shape[0]
cols = img.shape[1]

M = np.float32([[1,0,3], [0,1,90]])
shifted = cv.warpAffine(img, M, (cols, rows))

cv.imshow("Shifted", shifted)
cv.waitKey(1000)

# Rotate (Dondurme)
M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow("Rotated", dst)
cv.waitKey(1000)

# Scaling (Boyutlama)
res = cv.resize(img, None, fx=0.4, fy=0.4, interpolation=cv.INTER_CUBIC)
cv.imshow("Img", res)
cv.waitKey(1000)

cv.destroyAllWindows()