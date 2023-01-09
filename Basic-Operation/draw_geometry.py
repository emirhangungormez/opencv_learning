import cv2 as cv
import numpy as np

image = np.zeros((512,512,3), dtype=np.uint8)

cv.rectangle(image, (100,100), (300,300), (255,0,0), 2, cv.LINE_8, 0) # Dikdortgen
cv.circle(image, (256,256), 50, (0,0,2550), 2, cv.LINE_8, 0) # Daire
cv.ellipse(image, (256,256), (150,50), 360, 0, 360, (0,255,0), 2, cv.LINE_8, 0) # Elips
cv.imshow("Image", image)
cv.waitKey(0)
