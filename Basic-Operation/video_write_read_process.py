import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0) # '0' Dahili kamera, '1' Harici kamera
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

def process(image, opt=1):
    dst = None
    if opt == 0:
        dst = cv.bitwise_not(image) # Tersine cevirme
    if opt == 1:
        dst = cv.GaussianBlur(image, (0,0), 15) # Bulaniklastirma
    if opt == 2:
        dst = cv.Canny(image, 100, 200) # Cizgisel-Kenar Efekt
    return dst

index = 1 # Efekt belirlemesi
while True:
    # Kamredan goruntu al
    ret, frame = capture.read()

    # Goruntu basarili alindi mi kontrol
    if ret is True:
        # Okunan goruntuyu ekranda goster
        cv.imshow("Video-input", frame)
        c = cv.waitKey(50)
        if c >= 49:
            index = c - 49
        result = process(frame, index)
        cv.imshow("Result", result)
        # print(c)
        if c == 27: # ESC
            break
        else:
            break
cv.waitKey(1)