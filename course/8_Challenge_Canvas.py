import numpy as np
import cv2 as cv

# Global variables
canvas = np.ones([500, 500, 3], 'uint8') * 255
pint = False
color = (0, 255, 0)  # Green color
line_width = -1  # -1 if wanted the circle filled
radius = 5
point = (0, 0)  # Initial point coordinates

# click callback
def click(event, x, y, flags, param):
    global canvas, point, pint, color
    if event == cv.EVENT_LBUTTONDOWN:
        print("LButton Down")
        pint = True
    elif event == cv.EVENT_MOUSEMOVE:
        print("Mouse Move")
        point = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        pint = False
        print("LButton Up")


# window initialization and callback assignment
cv.namedWindow("canvas")
cv.setMouseCallback("canvas", click)

# Forever draw loop
while True:
    cv.imshow("canvas", canvas)
    if(pint):
        cv.circle(canvas, point, radius, color, line_width)

    # key capture every 1ms
    ch = cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cv.destroyAllWindows()