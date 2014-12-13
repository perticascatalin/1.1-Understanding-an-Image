# Run: python saveRectagle.py <image_name>
# Gets a rectangular region from an image using mouse clicks
# Image is scaled in memory to have 500 rows only
# 4 clicks needed
# Process can be repeated
# Program quits when 'q' key is pressed
# Obtained images saved under: last_rectangle.jpg, highlighted.jpg

import cv2
import numpy as np
import sys

# Saves the rectangle after 4th point is clicked
def save_rectangle():
	low_x = min(click_x)
	high_x = max(click_x)
	low_y = min(click_y) 
	high_y = max(click_y)
	print 'rows:', low_x, high_x
	print 'cols:', low_y, high_y
	sub_image = real_image[low_y:high_y, low_x:high_x]
	highlighted_region = real_image.copy()
	cv2.rectangle(highlighted_region, (low_x, low_y), (high_x, high_y), (0,255,0), 2)
	cv2.imwrite('last_rectangle.jpg', sub_image)
	cv2.imwrite('highlighted.jpg', highlighted_region)

# Cleans up image for further rectangular extraction
def wash_image():
	global display_image
	display_image = real_image.copy()

# Mouse event action
def make_click(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONUP:
		global click_count
		if click_count == 0:
			wash_image()
			cv2.imshow('image',display_image)
		click_x[click_count] = x
		click_y[click_count] = y
		cv2.circle(display_image, (x,y), 8, (0,255,0), 2)
		cv2.imshow('image',display_image)
		print 'drew circle'
		click_count += 1
		if click_count == 4:
			save_rectangle()
			click_count = 0

click_count = 0
click_x = [0,0,0,0]
click_y = [0,0,0,0]

image_name = sys.argv[1]
real_image = cv2.imread(image_name)
rows, cols, no_channels = real_image.shape
maxsz = 500.0
if rows > maxsz:
	ratio = float(rows)/maxsz
	n_rows = int(float(rows)/ratio)
	n_cols = int(float(cols)/ratio)
	real_image = cv2.resize(real_image, (n_cols, n_rows))
display_image = real_image.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image',make_click)

while(1):
    cv2.imshow('image',display_image)
    key = cv2.waitKey()
    if key == ord('q'):
        break
cv2.destroyAllWindows()

#cv2.imwrite('with_circles.jpg', display_image)