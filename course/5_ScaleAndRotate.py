import numpy as np
import cv2 as cv

img = cv.imread("players.jpg", 1)

# Scale
img_half = cv.resize(img, (0,0), fx=0.5, fy=0.5)    # Not absolute value but relative to the original one by fx fy
img_stretch = cv.resize(img, (600,600))     # Size to be 600x600px
img_stretch_near = cv.resize(img, (600,600), interpolation=cv.INTER_NEAREST)

cv.imshow("half", img_half)
cv.imshow("stretch", img_stretch)
cv.imshow("stretch near", img_stretch_near)

# Rotation
M  = cv.getRotationMatrix2D((0,0), -30, 1)      # Set point of rotation to be (0,0), rotate -30 degrees and scale 1
rotated = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))       # Rotate according to M and set the with-height same as original picture
cv.imshow("rotated", rotated)


cv.waitKey(0)
cv.destroyAllWindows()