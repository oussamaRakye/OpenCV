import numpy as np
import cv2 as cv

template = cv.imread("template.jpg", 0)
frame = cv.imread("players.jpg", 0)



result = cv.matchTemplate(frame, template, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
print(max_val, max_loc)
cv.circle(frame, max_loc, 15, 255, 2)
cv.imshow("Matching", result)

cv.imshow("Frame", frame)
cv.imshow("Template", template)

cv.waitKey(0)
cv.destroyAllWindows()