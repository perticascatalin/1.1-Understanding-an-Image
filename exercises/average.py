# Source code for 3. Replace by the Average Pixel exercise
# Run: python average.py <image_name> <start_row> <end_row> <start_col> <end_col>

import cv2
import numpy as np
import sys

# replaces a given rectangluar portion by its average
def replaceRectByAverage(image, startRow, endRow, startCol, endCol):
	blue_sum = 0.0
	green_sum = 0.0
	red_sum = 0.0
	pixel_count = 0

	rectangle = image[startRow:endRow+1, startCol:endCol+1]
	rows = rectangle.shape[0]
	cols = rectangle.shape[1]

	for row in range(rows):
		for col in range(cols):
			pixel = rectangle[row, col]
			blue_sum += float(pixel[0])
			green_sum += float(pixel[1])
			red_sum += float(pixel[2])
			pixel_count += 1

	#print blue_sum, green_sum, red_sum, pixel_count

	average_blue = int(blue_sum/float(pixel_count))
	average_green = int(green_sum/float(pixel_count))
	average_red = int(red_sum/float(pixel_count))

	#print average_blue, average_green, average_red

	new_image = image.copy()
	new_rectangle = np.zeros((1,1,3), np.uint8)
	new_rectangle[0,0] = (average_blue, average_green, average_red)
	new_rectangle = cv2.resize(new_rectangle, (cols, rows))
	new_image[startRow:endRow+1, startCol:endCol+1] = new_rectangle

	return new_image

# replaces each row by the average pixel in the row
def replaceEachRowByAverage(image):
	average_rows = image.copy()
	no_rows = image.shape[0]
	no_cols = image.shape[1]
	for row in range(no_rows):
		average_rows = replaceRectByAverage(average_rows, row, row, 0, no_cols - 1)
	cv2.imwrite('average_rows.jpg', average_rows)

# replaces each column by the average pixel in the column
def replaceEachColByAverage(image):
	average_cols = image.copy()
	no_rows = image.shape[0]
	no_cols = image.shape[1]
	for col in range(no_cols):
		average_cols = replaceRectByAverage(average_cols, 0, no_rows - 1, col, col)
	cv2.imwrite('average_cols.jpg', average_cols)

image_name = sys.argv[1]
sr = int(sys.argv[2]) # start row
er = int(sys.argv[3]) # end row
sc = int(sys.argv[4]) # start col
ec = int(sys.argv[5]) # end col

image = cv2.imread(image_name)

average_image = replaceRectByAverage(image, sr, er, sc, ec)
cv2.imwrite('average_' + image_name, average_image)

replaceEachRowByAverage(image)
replaceEachColByAverage(image)