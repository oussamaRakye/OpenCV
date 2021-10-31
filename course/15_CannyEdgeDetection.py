import numpy as np
import cv2 as cv

img = cv.imread("tomatoes.jpg")

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
res, thresh = cv.threshold(hsv[:,:,0], 25, 255, cv.THRESH_BINARY_INV)

edges = cv.Canny(img, 100, 70) # Edge detection

final = cv.bitwise_and(thresh, cv.bitwise_not(edges))

cv.imshow("Final", final)

cv.waitKey(0)
cv.destroyAllWindows()