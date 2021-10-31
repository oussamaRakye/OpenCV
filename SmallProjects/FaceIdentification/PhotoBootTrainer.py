import numpy as np
import cv2 as cv
import os

face_cascade = cv.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')

cap = cv.VideoCapture(0)

name = 'Oussama'
path = 'Faces/' + name

if not os.path.exists(path):
    os.makedirs(path)


def nameFile(file):
    return int(file[:len(file) - 4])


listFiles = sorted(map(nameFile, os.listdir(path)))

i = listFiles[-1] + 1 if len(listFiles) > 0 else 0

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = frame[y:y + h, x:x + w]
        img_item = "{}/{}.png".format(path, i)
        roi_gray = cv.cvtColor(roi_color, cv.COLOR_BGR2GRAY)
        cv.imwrite(img_item, roi_gray)
        i += 1
        print(i)

    frame = cv.flip(frame, 1)

    cv.imshow("Frame", frame)

    ch = cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
