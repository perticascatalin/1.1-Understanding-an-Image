# Source code for 1. Mirror the Image exercise
# Run: python mirror.py <image_name>

import cv2
import sys

# flips around the horizontal axis, done manually(with iteration)
def flipHorizontallyWithIteration(image):
	flipped = image.copy()
	no_rows = flipped.shape[0]
	no_cols = flipped.shape[1]
	for col in range(no_cols):
		halfway = no_rows/2
		for row in range(halfway):
			pix = flipped[row, col].copy()
			flipped[row, col] = flipped[no_rows - row - 1, col].copy()
			flipped[no_rows - row - 1, col] = pix
	return flipped

# flips around the vertical axis, done manually(with iteration)
def flipVerticallyWithIteration(image):
	flipped = image.copy()
	no_rows = flipped.shape[0]
	no_cols = flipped.shape[1]
	for row in range(no_rows):
		halfway = no_cols/2
		for col in range(halfway):
			pix = flipped[row, col].copy()
			flipped[row, col] = flipped[row, no_cols - col - 1].copy()
			flipped[row, no_cols - col - 1] = pix
	return flipped

# flips around the horizontal axis
def flipHorizontally(image):
	flipped = cv2.flip(image, 0)
	return flipped

# flips around the vertical axis
def flipVertically(image):
	flipped = cv2.flip(image, 1)
	return flipped

# fetch the name of the image and store it in memory
image_name = sys.argv[1]
image = cv2.imread(image_name)

vertical = flipVerticallyWithIteration(image)
horizontal = flipHorizontallyWithIteration(image)

# output the images
cv2.imwrite('vertical_flip.jpg', vertical)
cv2.imwrite('horizontal_flip.jpg', horizontal)
