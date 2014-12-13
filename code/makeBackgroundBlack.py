# Floodfill from mouse click pixel example
# Used for filling background with black for an example image for 1.1 Understanding an Image

import cv2
import numpy as np
import sys

def make_click(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONUP:
		rows, cols, no_channels = image.shape
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		#cv2.imshow('gray', gray)
		#cv2.waitKey()
		ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
		kernel = np.ones((3,3),np.uint8)
		thresh = cv2.dilate(thresh, kernel, iterations = 1)
		thresh[thresh > 50] = 255
		thresh[thresh <= 50] = 0
		#cv2.imshow('thresh', thresh)
		#cv2.waitKey()
		mask = np.zeros((rows+2, cols+2), np.uint8)
		lo_diff = 0
		hi_diff = 0
		no_neighbors = 8
		cv2.floodFill(thresh, mask, (x,y), 128, lo_diff, hi_diff, no_neighbors)
		#cv2.imshow('image', thresh)
		#cv2.waitKey()
		image[thresh == 128] = (0,0,0)
		cv2.imshow('image', image)
		print 'filled background'

image_name = sys.argv[1]
image = cv2.imread(image_name)
cv2.namedWindow('image')
cv2.setMouseCallback('image',make_click)

while(1):
    cv2.imshow('image', image)
    key = cv2.waitKey()
    if key == ord('q'):
        break
cv2.destroyAllWindows()
rows, cols, no_channels = image.shape
cv2.imwrite('black_background.jpg', image)