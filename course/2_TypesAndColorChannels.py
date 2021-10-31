import numpy as np
import cv2 as cv

color = cv.imread("butterfly.jpg", 1)
cv.imshow("Image", color)
cv.moveWindow("Image", 0, 0)
print(color.shape)
height, width, channels = color.shape


b, g, r = cv.split(color)

rgb_split = np.empty([height,width*3,3], "uint8")  # Creates an initialized array

rgb_split[:, 0:width] = cv.merge([b,b,b])
rgb_split[:, width:width*2] = cv.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv.merge([r,r,r])

cv.imshow("rgb channels", rgb_split)
cv.moveWindow("rgb channels", width, 0)


hsv = cv.cvtColor(color, cv.COLOR_BGR2HSV)      #rgb to hsv
h,s,v = cv.split(hsv)
hsv_split = np.concatenate((h,s,v), axis=1)     #Makes the same as before but more efficient, axis=1 is telling numpy to set images side-by-side
cv.imshow("hsv channels", hsv_split)
cv.moveWindow("hsv channels", width, height)


cv.waitKey(0)
cv.destroyAllWindows()
