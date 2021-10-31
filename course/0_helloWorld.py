import cv2 as cv
import numpy as np

img = cv.imread("course/opencv-logo.png", 1)   #Read the image with the color channels, 0 would be black and white
#print(img)     #it's actually an array
#img.dtype       #the bits for each color in each pixel (usually 8 , range from 0 to 255)
#img.size       #total nuber of pixels
cv.namedWindow("Image", cv.WINDOW_NORMAL)   #Creates a window with given name and be normal (for cv)
cv.imshow("Image", img)                     #Opens window
cv.waitKey(0)                               #Keeps the window open until any key pressed
cv.imwrite("course/output.jpg", img)   #Saves the image with given name
