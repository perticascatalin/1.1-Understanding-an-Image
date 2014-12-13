# Run: python BGR_Components_Grayscale.py <image_name>
# Computes blue, green and red components of a BGR image
# Computes grayscale
# Obtained images saved under: 'blue_<image_name>',..., 'gray_<image_name>' 

import cv2
import sys

image_name = sys.argv[1]
image = cv2.imread(image_name)
blue_component = image.copy() 
green_component = image.copy()
red_component = image.copy()

# First copy image into 3 separate images
# Then make other components equal to 0
# Can use the code for iterating an image

no_rows = image.shape[0]
no_cols = image.shape[1]

# Isolate blue component
for row in range(no_rows):
	for col in range(no_cols):
		blue = blue_component[row, col, 0]
		blue_component[row, col] = (blue, 0, 0)
		
cv2.imwrite('blue_' + image_name, blue_component)
		
# Isolate green component
for row in range(no_rows):
	for col in range(no_cols):
		green = green_component[row, col, 1]
		green_component[row, col] = (0, green, 0)

cv2.imwrite('green_' + image_name, green_component)
		
# Isolate red component
for row in range(no_rows):
	for col in range(no_cols):
		red = red_component[row, col, 2]
		red_component[row, col] = (0, 0, red)
		
cv2.imwrite('red_' + image_name, red_component)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_' + image_name, gray)