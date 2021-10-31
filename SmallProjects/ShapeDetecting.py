import numpy as np
import cv2

img = cv2.imread('circle.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 80, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0,0,0),2)

height, width = img.shape[0:2]
empty = np.ones([height, width, 3], 'uint8')*255

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    if len(approx) != 4:
        cv2.drawContours(img, [approx], 0, (0, 0, 0), -1)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 80, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0,0,0),2)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    print(len(approx))
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) > 14:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    


cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()