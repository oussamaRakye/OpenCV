import numpy as np
import cv2 as cv

img = cv.imread("detect_blob.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
cv.imshow("Binary", thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1      # Index of the contours to be drawn, -1 for all of them
thickness = 4
color = (255, 78, 150)

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')
for c in contours:
    cv.drawContours(objects, [c], -1, color, -1)
    
    area = cv.contourArea(c)
    perimeter = cv.arcLength(c, True)   # Perimeter, true if it is a closed contour

    M = cv.moments(c)
    cx = int( M['m10']/M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv.circle(objects, (cx, cy), 4, (0,0,255), -1)
    
    print("Area: {}, perimeter: {}".format(area, perimeter))
    
cv.imshow("Contours", objects)

cv.waitKey(0)
cv.destroyAllWindows()