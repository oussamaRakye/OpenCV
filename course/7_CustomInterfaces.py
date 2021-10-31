import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)  # Open camera

color = (0, 255, 0)  # Green color
line_width = 3  # -1 if wanted the circle filled
radius = 100
point = (0, 0)  # Initial point coordinates


def click(event, x, y, flags, param):  # Callback of the click
    global point, pressed
    if event == cv.EVENT_LBUTTONDOWN:
        print("pressed", x, y)
        point = (x, y)


cv.namedWindow("Frame")
cv.setMouseCallback("Frame", click)     # Attach the method click to the callback of the window

while True:
    ret, frame = cap.read()  # Reads frame from camera

    frame = cv.resize(frame, (0, 0), fx=2, fy=2)  # Resize
    cv.circle(frame, point, radius, color, line_width)
    cv.imshow("Frame", frame)

    ch = cv.waitKey(1)  # Runs every n milliseconds
    if ch & 0xFF == ord("q"):  # Check if the key is q and break
        break

cap.release()  # Stop/close camera
cv.destroyAllWindows()
