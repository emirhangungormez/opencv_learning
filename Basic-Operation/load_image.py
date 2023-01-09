# Konsola "pip install opencv-python" yazarak gerekli kutuphane yuklenmeli.

import cv2 as cv
path = "Basic-Operation/"
img = cv.imread(path + "yoda.jpg") # Okuma yapar.
type(img)

# namedWindow (Pencere ayarlaması)
cv.namedWindow('Yoda',cv.WINDOW_AUTOSIZE)

# imshow (Ekranda gosterme)
cv.imshow('Yoda', img)
cv.waitKey(10000)
cv.destroyAllWindows