import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)    # Open camera

while True:
    ret, frame = cap.read()     # Reads frame from camera

    frame = cv.resize(frame, (0,0), fx=2, fy=2)     # Resize


    cv.imshow("Frame", frame)

    ch = cv.waitKey(1)  # Runs every n milliseconds
    if ch & 0xFF == ord("q"):       # Check if the key is q and break
        break

cap.release()       # Stop/close camera
cv.destroyAllWindows()