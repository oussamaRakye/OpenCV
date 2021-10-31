import numpy as np
import cv2 as cv

img = cv.imread("detect_blob.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("gray", gray)
thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
cv.imshow("Binary", thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1      # Index of the contours to be drawn, -1 for all of them
thickness = 4
color = (255, 78, 150)

cv.drawContours(img2, contours, index, color, thickness)
cv.imshow("Contours", img2)

cv.waitKey(0)
cv.destroyAllWindows()
