import cv2 as cv
import numpy as np
path = "Basic-Operation/"
img1 = cv.imread(path + "merve1.jpg")
img2 = cv.imread(path + "merve.jpg")

horizontal = np.hstack((img1, img2)) # Resimleri birlestirir.
cv.imshow("Yoda ve Merve", horizontal)
cv.waitKey(10000)
cv.destroyAllWindows