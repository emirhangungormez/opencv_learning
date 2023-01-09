import cv2 as cv
path = "Basic-Operation/"
img = cv.imread(path + "yoda.jpg") # Okuma yapar.

# X Flip
dst1 = cv.flip(img, 0)
cv.imshow("Flip-Yoda", dst1)
cv.waitKey(0)

# Y Flip
dst1 = cv.flip(img, 1)
cv.imshow("Flip-Yoda", dst1)
cv.waitKey(0)

# XY Flip
dst1 = cv.flip(img, -1)
cv.imshow("Flip-Yoda", dst1)
cv.waitKey(0)

cv.destroyAllWindows