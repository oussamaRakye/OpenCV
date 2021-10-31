import numpy as np
import cv2 as cv

image = cv.imread("thresh.jpg", 1)
cv.imshow("original", image)

blur = cv.GaussianBlur(image, (9, 15), 0)  # Blur in x,y axis by 9 and 15. Have to be odd numbers
cv.imshow("blur", blur)

kernel = np.ones((3,3), 'uint8')

dilate = cv.dilate(image, kernel, iterations=1)
erode = cv.erode(image, kernel, iterations=1)

cv.imshow("dilate", dilate)
cv.imshow("erode", erode)

cv.waitKey(0)
cv.destroyAllWindows()
