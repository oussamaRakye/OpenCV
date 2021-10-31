import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)    # Open camera

while True:
    ret, frame = cap.read()     # Reads frame from camera

    frame = cv.resize(frame, (0,0), fx=2, fy=2)     # Resize
    
    frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    width, height, _ = frame.shape

    for w in range(width):
        for h in range(height):
            temp = frame[w][h]
            if temp[0] < 70 or temp[0] > 95:
                frame[w][h] = [0, 0, 255]

    frame = cv.cvtColor(frame, cv.COLOR_HSV2BGR)
    cv.imshow("Frame", frame)

    ch = cv.waitKey(30)  # Runs every n milliseconds
    if ch & 0xFF == ord("q"):       # Check if the key is q and break
        break

cap.release()       # Stop/close camera
cv.destroyAllWindows()