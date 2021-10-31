import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
template = cv.imread("re.jpg", 0)


while cap.isOpened():
    ret, frame = cap.read()  # Reads frame from camera

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    canny = cv.Canny(gray, 150, 180)
    circles = cv.HoughCircles(canny, cv.HOUGH_GRADIENT, 1, 20,
                              param1=50, param2=30, minRadius=0, maxRadius=0)
    if circles is not None and len(circles)>0:
        detected_circles = np.uint16(np.around(circles))
        for (x, y, r) in detected_circles[0, :]:
            cv.circle(frame, (x, y), r, (0, 255, 0), -1)
            cv.circle(frame, (x, y), 2, (0, 255, 255), 3)

    cv.imshow("Frame", frame)
    ch = cv.waitKey(1)  # Runs every n milliseconds
    if ch & 0xFF == ord("q"):  # Check if the key is q and break
        break
cv.waitKey(0)  # Runs every n milliseconds
cv.destroyAllWindows()
cap.release()
