# Videolarda on plandaki goruntu goz ardi edilerek arka plana odaklanilmistir

import cv2 as cv
import numpy as np

cap = cv.VideoCapture("Image-Process\Patric_Bateman.mp4")

fgbg = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=500)

while True:
    ret, frame = cap.read() # video bilgileri
    fgmask = fgbg.apply(frame) # siyah arkaplan
    background = fgbg.getBackgroundImage()
    cv.imshow("input", frame)
    cv.imshow("mask", fgmask)
    cv.imshow("background", background)
    k = cv.waitKey(10)&0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()