# Yuzun, gozun ve diger ozelliklerin ogrenme yoluyla cikarildigi bir
# yapinin nihai hali, ogrenilmis bir modelin ozelliklerini kullanarak gerceklestirilmistir.

import cv2 as cv
import numpy as np

model_bin = "Apps\Model\MobileNetSSD_deploy.caffemodel"
config_text = "Apps\Model\MobileNetSSD_deploy.prototxt"

objName = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "wolf", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

net = cv.dnn.readNetFromCaffe(config_text, model_bin)

cap = cv.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    h, w = frame.shape[:2]
    blobImage = cv.dnn.blobFromImage(frame, 0.007843, (300, 300), (127.5, 127.5, 127.5), True, False)
    net.setInput(blobImage)
    cvOut = net.forward()
    for detection in cvOut[0,0,:,:]:
        score = float(detection[2])
        objIndex = int(detection[1])
        if score > 0.5: # ilgili sinifa ait olma olasiligi
            left = detection[3] * w
            top = detection[4] * h
            right = detection[5] * w
            bottom = detection[6] * h
            cv.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (255,0,0), thickness=2)
            cv.putText(frame, "score:%.2f,%s" % (score, objName[objIndex]),(int(left) - 10, int(top) -5 ), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2,8)

    cv.imshow("video-ssd", frame)
    c = cv.waitKey(10)
    if c == 27:
        break

cv.waitKey(0)

