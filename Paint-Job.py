import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# 1st 3 are minimum last 3 maximum  hue min, sat min, val min
colorHSV = [[0, 59, 255, 74, 255, 255],  # red color hsv
            [64, 96, 241, 154, 255, 255]]  # blue color hsv


def findColors(img, colorHSV):
    # Convert bgr to hsv
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    count = 0
    for color in colorHSV:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHsv, lower, upper)

        cv2.imshow(str(color[count]), mask)


while True:
    success, img = cap.read()

    if not success:
        break

    findColors(img, colorHSV)
    cv2.imshow('Camera (Press Q to exit)', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
