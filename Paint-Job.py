import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# 1st 3 are minimum last 3 maximum  hue min, sat min, val min
colorHSV = [[],
            [],
            []]


def findColors(img):
    # Convert bgr to hsv
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower =
    mask = cv2.inRange(imgHsv)


while True:
    success, img = cap.read()

    if not success:
        break

    cv2.imshow('Camera (Press Q to exit)', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
