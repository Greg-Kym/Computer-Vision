import cv2
import numpy as np


cap = cv2.VideoCapture('http://192.168.0.101:8080/video')

widthImg = 720
heightImg = 720


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 150, 200)

    kernel = np.ones((5, 5))

    imgDilate = cv2.dilate(imgCanny, kernel, iterations=1)
    imgEroded = cv2.erode(imgDilate, kernel, iterations=1)

    return imgEroded


def getContours(img):
    contours, _ = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    biggest = np.array([])
    maxArea = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 5000:
            peri = cv2.arcLength(cnt, True)

            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            if len(approx) == 4 and area > maxArea:
                biggest = approx
                maxArea = area

    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)

    return biggest


def getWarped(points):
    print(points)

    reArrange(points)


def reArrange(points):


while True:
    succ, img = cap.read()

    if not succ or img is None:
        print('Connection not established')
        break

    img = cv2.resize(img, (widthImg, heightImg))
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    imgContour = img.copy()

    imgClear = preProcessing(img)

    biggest = getContours(imgClear)

    getWarped(biggest)

    cv2.imshow('Image (Press Q to cancel)', imgContour)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
