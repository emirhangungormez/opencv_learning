# Shi-tomas yontemiyle goruntu icindeki yer alan kenarlar yakalamis ve bu koseler isaretlenmistir.

import cv2 as cv
import numpy as np

src = cv.imread("Image-Process\legolar.jpg")

def process(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray, maxCorners=35, qualityLevel=0.05, minDistance=10)
    # cv.goodFeaturesToTrack() = goruntudeki en keskin yerleri bulur
    for pt in corners:
        print(pt)
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][0])
        cv.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)
    
    return image

result = process(src)
cv.imshow('result', result)
cv.waitKey(0)