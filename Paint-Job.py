import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# 1st 3 are minimum last 3 maximum  hue min, sat min, val min
colorHSV = [[132, 92, 0, 255, 255, 255],  # red color hsv
            [83, 177, 156, 255, 255, 255],  # blue color hsv
            [0, 93, 255, 255, 255, 255],  # orange hsv
            [14, 68, 213, 91, 255, 255]  # green
            ]

# Colors in BGR
myColors = [
    [0, 40, 255],  # red
    [255, 0, 0],  # blue
    [0, 106, 255],  # orange
    [0, 255, 200]  # green
]

myPoints = []


def findColors(img, colorHSV, myColors):
    # Convert bgr to hsv
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    count = 0
    points = []

    for color in colorHSV:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHsv, lower, upper)

        x, y = getContours(mask)

        cv2.circle(imgResult, (x, y), 10, myColors[count], cv2.FILLED)

        if x != 0 and y != 0:
            points.append([x, y, count])

        count += 1

    return points


def getContours(mask):
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x, y, w, h = 0, 0, 0, 0

    for cnt in contours:
        # calculate Area
        area = cv2.contourArea(cnt)

        if area > 500:
            # Calculate perimeter
            peri = cv2.arcLength(cnt, True)

            # Approximate contour shape
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            # Get Bounding rectangle
            x, y, w, h = cv2.boundingRect(approx)

    return x + w // 2, y


def draw(myPoints, myColors):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]),
                   10, (myColors[point[2]]), cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()

    if not success:
        break

    points = findColors(img, colorHSV, myColors)

    if len(points) != 0:
        for newPoint in points:
            myPoints.append(newPoint)

    if len(myPoints) != 0:
        draw(myPoints, myColors)

    cv2.imshow('Camera (Press Q to exit)', imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
