import numpy as np
import cv2 as cv

color = cv.imread("butterfly.jpg", 1)

gray = cv.cvtColor(color, cv.COLOR_BGR2GRAY)    #rgb to gray
#cv.imshow("gray", gray)
cv.imwrite("gray.jpg", gray)

b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba = cv.merge((b,g,r,g))      #Alpha is depending of g (non green zones will appear tranparent)
cv.imwrite("rgba.png", rgba)

