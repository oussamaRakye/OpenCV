import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)    # Open camera

while True:
    ret, frame = cap.read()     # Reads frame from camera

    frame = cv.resize(frame, (0,0), fx=2, fy=2)     # Resize
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    path = 'haarcascade_frontalface_default.xml'

    face_cascade = cv.CascadeClassifier(path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.06, minNeighbors=5, minSize=(40, 40))
    print(len(faces))

    if(len(faces)==1):
        x, y, w, h = faces[0]
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 8)
    cv.imshow("Frame", frame)
    ch = cv.waitKey(1)  # Runs every n milliseconds
    if ch & 0xFF == ord("q"):       # Check if the key is q and break
        break

cap.release()       # Stop/close camera
cv.destroyAllWindows()