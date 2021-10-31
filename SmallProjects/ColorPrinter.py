import time

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)  # Open camera

while True:
    ret, frame = cap.read()  # Reads frame from camera

    frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    width, height, _ = frame.shape

    print(frame[width//2][height//2])

    frame = cv.cvtColor(frame, cv.COLOR_HSV2BGR)

    cv.circle(frame, (height//2,width//2), 4, (0,255,0), 2)

    cv.imshow("Frame", frame)

    time.sleep(0.5)

    ch = cv.waitKey(30)  # Runs every n milliseconds
    if ch & 0xFF == ord("q"):  # Check if the key is q and break
        break

cap.release()  # Stop/close camera
cv.destroyAllWindows()