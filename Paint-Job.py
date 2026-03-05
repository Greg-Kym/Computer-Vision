import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# 1st 3 are minimum last 3 maximum  hue min, sat min, val min
colorHSV = [[132, 92, 0, 255, 255, 255],  # red color hsv
            [83, 177, 156, 255, 255, 255],  # blue color hsv
            [0, 93, 255, 255, 255, 255]  # orange hsv
            [14, 68, 213, 91, 255, 255]  # green
            ]


def findColors(img, colorHSV):
    # Convert bgr to hsv
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    count = 0
    for color in colorHSV:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHsv, lower, upper)

        x, y = getContours(mask)

        cv2.imshow(str(color[count]), mask)


def getContours(mask):
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x, y, w, h = 0, 0, 0, 0

    for cnt in contours:
        # calculate Area
        area = cv2.contourArea(cnt)

        if area > 500:
            # Calculate perimeter
            peri = cv2.arcLength(cnt)

            # Approximate contour shape
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            # Get Bounding rectangle
            x, y, w, h = cv2.boundingRect(approx)

    return (x + w) / 2, y


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
