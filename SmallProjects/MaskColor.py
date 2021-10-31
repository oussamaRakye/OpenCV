import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Read the picure - The 1 means we want the image in BGR

while True:
    ret, frame = cap.read()

    # convert BGR image to a HSV image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    print(hsv)

    # NumPy to create arrays to hold lower and upper range
    # The “dtype = np.uint8” means that data type is an 8 bit integer

    lower_range = np.array([160, 170, 0], dtype=np.uint8)
    upper_range = np.array([180, 230, 255], dtype=np.uint8)

    # create a mask for image
    mask = cv2.inRange(hsv, lower_range, upper_range)

    # display both the mask and the image side-by-side
    cv2.imshow('mask', mask)
    cv2.imshow('image', frame)

# wait to user to press [ ESC ]
    k = cv2.waitKey(1)
    if (k == 27):
        break

cap.release()
cv2.destroyAllWindows()