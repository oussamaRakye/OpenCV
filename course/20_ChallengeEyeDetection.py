import numpy as np
import cv2 as cv

img = cv.imread("faces.jpeg", 1)
img = cv.resize(img, (0,0), fx=0.3, fy=0.3)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
path = 'haarcascade_eye.xml'

eye_cascade = cv.CascadeClassifier(path)
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=20, minSize=(10,10))

for (x, y, w, h) in eyes:
    cv.circle(img, (int(x+w/2), int(y+h/2)), w//2, (0, 255, 0), 2)
    print(x, y)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()