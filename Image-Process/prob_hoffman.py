# Goruntulerde binary goruntuye cevirme islemi yapılarak goruntudeki
# birbirinden farklı uzunluk ve acilardaki cizgilerin tespiti
# olasiliksal yaklaşim ile gerçeklestirilmistir

import cv2 as cv
import numpy as np

def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image, t, t*2)
    cv.imshow("canny_output", canny_output)
    return canny_output

src = cv.imread("Image-Process\yoda.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)

binary = canny_demo(src)
cv.imshow("binary", binary)
cv.waitKey(0)

linesP = cv.HoughLinesP(binary, 1, np.pi / 180, 150, None, 0, 0)
cv.HoughLinesP
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(src, (l,[0], l[1], (l[2], l[3]), (255,0,0), 1, cv.LINE_AA))

cv.imshow("hough line demo", src)
cv.waitKey(0)