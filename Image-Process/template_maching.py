# Template matching yöntemiyle sablon goruntusu ile eslesen ana kaynak
# goruntusundeki nokta bulunmus ve yakalinmistir.

import cv2 as cv
import numpy as np

def template_demo():
    src = cv.imread("Image-Process\test1.jpg")
    tpl = cv.imread("Image-Process\test2.jpg")

    cv.imshow("input", src)
    cv.imshow("tpl", tpl)

    th, tw = tpl.shape[:2]

    result = cv.matchTemplate(src, method=cv.TM_CCOEFF_NORMED) # karsilastirma
    cv.imshow("result", result)

    # cv.imwrite(path + "/result.png, np.uint8(result*255)")
    t = 0.98 # benzerlik yuzdesi
    loc = np.where(result > t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255,0,0), 1, 8, 0) # kare cizimi
    
    cv.imshow("ilk_demo", src)
    cv.waitKey(0)
