# Kotu resimler uzerinde histogram esitleme islemi
# yapilarak gorsellerin iyilestirilmesi saglanmistir.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def custom_hist(gray):

    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1

    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align='center', color='r', alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

src = cv.imread("Image-Process\yoda.jpg")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("Cikti", gray)
cv.waitKey(0)

custom_hist(gray)

dst = cv.equalizeHist(gray)
cv.imshow("Cikti_2", dst)
cv.waitKey(0)

custom_hist(dst)