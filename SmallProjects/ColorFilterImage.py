import numpy as np
import cv2 as cv

frame = cv.imread('ar.png', 1)    # Load as a black and white image
height, width = frame.shape[0:2]


frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

for h in range(height):
    for w in range(width):
        temp = frame[h][w]
        # if temp[0] > 0:
        #     print(temp[0])
        if temp[0] < 70 or temp[0] > 95:
            frame[h][w] = [0,0,255]

frame = cv.cvtColor(frame, cv.COLOR_HSV2BGR)


cv.imshow("Original", frame)

cv.waitKey(0)
cv.destroyAllWindows()