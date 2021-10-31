import numpy as np
import cv2 as cv

img = cv.imread("fuzzy.png",1)
cv.imshow("Image", img)
img = cv.GaussianBlur(img, (9,9), 0)
#img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#thresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3501, 50)

img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h = img[:,:,0]
s = img[:,:,1]
v = img[:,:,2]

s = cv.adaptiveThreshold(s, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 1001, 10)
v = cv.adaptiveThreshold(v, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 1001, 10)

contours, hierarchy = cv.findContours(v, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

index = -1  # Index of the contours to be drawn, -1 for all of them
thickness = 4
color = (255, 255, 255)

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')
for c in contours:
    area = cv.contourArea(c)
    if area>1000:
        cv.drawContours(objects, [c], -1, color, -1)

#v = cv.bitwise_and(s, v)
objects = cv.cvtColor(objects, cv.COLOR_BGR2GRAY)
#objects = cv.adaptiveThreshold(objects, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 101, 10)
cv.imshow("Contours", objects)

cv.waitKey(0)
cv.destroyAllWindows()