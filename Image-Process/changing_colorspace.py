import cv2 as cv

# HSV
path = "Image-Process/"
img = cv.imread(path + "yoda.jpg")
cv.namedWindow("RGB", cv.WINDOW_AUTOSIZE)
cv.imshow("RGB", img)
cv.waitKey(1000)

# RGB to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
cv.waitKey(1000)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)
cv.waitKey(1000)