import cv2 as cv
import numpy as np

black = np.zeros([150, 200, 1], 'uint8')    #Creates an array of black sixe 150x200px and 1 channel
cv.imshow("black", black)

ones = np.ones([150,200,3], 'uint8')
cv.imshow("ones", ones)

white = np.ones([150,200,3], 'uint16')
white *= (2**16-1)
cv.imshow("white", white)

color = ones.copy()
color[:,:] = (255,0,0)
cv.imshow("blue", color)

cv.waitKey(0)
cv.destroyAllWindows()