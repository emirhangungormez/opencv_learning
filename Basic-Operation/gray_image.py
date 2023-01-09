import cv2 as cv
path = "Basic-Operation/"
img = cv.imread(path + "yoda.jpg") # Okuma yapar.
cv.namedWindow('Yoda',cv.WINDOW_AUTOSIZE)
cv.waitKey(10000)

# cvtColor
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray_Yoda', img)
cv.waitKey(10000)

# imWrite
cv.imwrite(path + "gray_yoda.jpg", gray)
cv.destroyAllWindows