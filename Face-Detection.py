import cv2
from facenet_pytorch import MTCNN
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if not success:
        break

    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    boxes, probs = MTCNN.detect(img_RGB)

    if probs[0] is None:
        probs[0] = None
    else:
        probs[0] = int(probs[0] * 100)

    if boxes is not None:
        for box in boxes:
            x1, y1, x2, y2 = box.astype(int)
            cv2.rectangle(img_RGB, (x1, y1), (x2, y2), (255, 0, 0), 3)
    cv2.putText(img_RGB, str(
        probs[0]), (30, 30), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.3, (234, 134, 174), 2)
    cv2.imshow('Video Capturing (Press Q to exit)', img_RGB)

    if

cv2.clear
