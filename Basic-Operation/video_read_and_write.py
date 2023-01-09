import cv2 as cv
import numpy as np

capture = cv.VideoCapture("Basic-Operation/Patric_Bateman.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

out = cv.VideoWriter("Basic-Operation/New_Patric_Bateman.avi", cv.VideoWriter_fourcc('D','I','V','X'), 15, (np.int_(width), np.int_(height)), True)

while True:
    # Kamredan goruntu al
    ret, frame = capture.read()

    # Goruntu basarili alindi mi kontrol
    if ret is True:
        # Okunan goruntuyu ekranda goster
        cv.imshow("Video-input", frame)
        out.write(frame)

        c = cv.waitKey(50)
        if c == 27: # ESC
            break
        else:
            break
capture.release()
out.release()

