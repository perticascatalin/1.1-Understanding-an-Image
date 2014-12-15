import cv2
import numpy as np
import sys

def replaceRectByAverage(image, startRow, endRow, startCol, endCol):
	blue_sum = 0.0
	green_sum = 0.0
	red_sum = 0.0
	pixel_count = 0

	rectangle = image[startRow:endRow+1, startCol:endCol+1]
	rows = rectangle.shape[0]
	cols = rectangle.shape[1]

	for pixel in rectangle:
		blue_sum += float(pixel[0])
		green_sum += float(pixel[1])
		red_sum += float(pixel[2])
		pixel_count += 1

	average_blue = int(blue_sum/float(pixel_count))
	average_green = int(green_sum/float(pixel_count))
	average_red = int(red_sum/float(pixel_count))

	new_image = image.copy()
	new_rectangle = np.zeros((1,1,3), np.uint8)
	new_rectangle = cv2.resize(new_rectangle, (cols, rows))
	new_image[startRow:endRow+1, startCol:endCol+1] = new_rectangle

	return new_image

image_name = sys.argv[1]
sr = int(sys.argv[2])
er = int(sys.argv[3])
sc = int(sys.argv[4])
ec = int(sys.argv[5])
image = cv2.imread(image_name)
average_image = replaceRectByAverage(image, sr, er, sc, ec)

cv2.imwrite('average_' + image_name, average_image)