import numpy as np
import cv2 as cv

img = cv.imread("faces.jpeg", 1)
img = cv.resize(img, (0,0), fx=0.3, fy=0.3)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
path = 'haarcascade_frontalface_default.xml'

face_cascade = cv.CascadeClassifier(path)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.06, minNeighbors=5, minSize=(40,40))
print(len(faces))

for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)


cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()
