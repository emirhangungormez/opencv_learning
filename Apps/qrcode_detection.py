# Opencv icindeki QR kod detection metodu kullanilarak bir QR kodunu yakalama
# ve bu QR kod icindeki mesaji okuma islemi anlatilmistir.

import cv2 as cv
import numpy as np

src = cv.imread("Apps\qrcode.jpg")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

qrcoder = cv.QRCodeDetector()

codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(gray)

result = np.copy(src)

cv.drawContours(result, [np.int32(points)], 0, (0,0,255), 2) # QR kod etrafina kirmizi cizgi cizimi

print("qrcode information is: \n%s" % codeinfo)

cv.imshow("QR", result)
cv.waitKey(0)