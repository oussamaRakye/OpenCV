import numpy as np
import cv2 as cv
import pickle

face_cascade = cv.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')

labels = {}
with open('labels.pickle', 'rb') as f:   # read bytes = rb
    temp = pickle.load(f)
    labels = {v:k for k,v in temp.items()}

cap = cv.VideoCapture(0)


while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y + h, x:x + w]

        id_, conf = recognizer.predict(roi_gray)
        print(conf)
        if conf < 45:
            cv.putText(frame, labels[id_], (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv.LINE_AA)


    cv.imshow("Frame", frame)

    ch = cv.waitKey(30)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
