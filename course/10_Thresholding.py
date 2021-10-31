import numpy as np
import cv2 as cv

bw = cv.imread('detect_blob.png', 0)    # Load as a black and white image
height, width = bw.shape[0:2]
cv.imshow("Original", bw)

binary = np.zeros([height, width, 1], 'uint8')

threshold = 85

for row in range(height):
    for col in range(width):
        if bw[row][col]>threshold:
            binary[row][col]=255

cv.imshow("Slow binary", binary)

# Does the same but more efficient
ret, threshold = cv.threshold(bw, threshold, 255, cv.THRESH_BINARY)     # 255 is the color that will be drawn
cv.imshow("Threshold", threshold)

cv.waitKey(0)
cv.destroyAllWindows()