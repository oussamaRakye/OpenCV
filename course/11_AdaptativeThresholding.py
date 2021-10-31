import numpy as np
import cv2 as cv

img = cv.imread('sudoku.png', 0)
cv.imshow("original", img)

ret, thresh_basic = cv.threshold(img, 70, 255, cv.THRESH_BINARY)     # 255 is the color that will be drawn
cv.imshow("Threshold_basic", thresh_basic)

# Adapts to each zone making it much better
thresh_adapt = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 151, 10)
cv.imshow("Threshold adaptive", thresh_adapt)

cv.waitKey(0)
cv.destroyAllWindows()