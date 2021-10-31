import numpy as np
import cv2 as cv

img = cv.imread('faces.jpeg', 1)
img = cv.resize(img, (0,0), fx=0.2, fy=0.2)
cv.imshow("original", img)


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split = np.concatenate((h, s, v), axis=1)     # axis=1 means concatenate horizontally
hsv_split = cv.resize(hsv_split, (0,0), fx=0.4, fy=0.4)
cv.imshow("split HSV", hsv_split)

ret, min_sat = cv.threshold(s, 40,255, cv.THRESH_BINARY)
cv.imshow("Saturation filter", min_sat)

ret, max_hue = cv.threshold(h, 15,255, cv.THRESH_BINARY_INV)
cv.imshow("Hue filter", max_hue)

final = cv.bitwise_and(min_sat, max_hue)    # White in both pictures, check them to see
cv.imshow("Final", final)


cv.waitKey(0)
cv.destroyAllWindows()