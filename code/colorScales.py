# Run: python colorScales.py
# Creates image examples for 1.1 Understanding an image
# Obtained images saved under: 'blackwhite.jpg', 'grayscale.jpg', 'blue.jpg', 'green.jpg', 'red.jpg'

import cv2
import numpy as np
import sys

rows = int(sys.argv[1])
cols = 256

blackwhite = np.zeros((rows, cols), np.uint8)
for col in range(cols/2, cols):
	for row in range(rows):
		blackwhite[row, col] = 255

grayscale = np.zeros((rows, cols), np.uint8)
for col in range(cols):
	for row in range(rows):
		grayscale[row, col] = col

blue = np.zeros((rows, cols, 3), np.uint8)
for col in range(cols):
	for row in range(rows):
		blue[row, col] = (col,0,0)

green = np.zeros((rows, cols, 3), np.uint8)
for col in range(cols):
	for row in range(rows):
		green[row, col] = (0,col,0)

red = np.zeros((rows, cols, 3), np.uint8)
for col in range(cols):
	for row in range(rows):
		red[row, col] = (0,0,col)

blackwhite = cv2.copyMakeBorder(blackwhite, 2,2,2,2, cv2.BORDER_CONSTANT,value = 0)
grayscale = cv2.copyMakeBorder(grayscale, 2,2,2,2, cv2.BORDER_CONSTANT,value = 0)
blue = cv2.copyMakeBorder(blue, 2,2,2,2, cv2.BORDER_CONSTANT,value = 0)
green = cv2.copyMakeBorder(green, 2,2,2,2, cv2.BORDER_CONSTANT,value = 0)
red = cv2.copyMakeBorder(red, 2,2,2,2, cv2.BORDER_CONSTANT,value = 0)

cv2.imwrite('blackwhite.jpg', blackwhite)
cv2.imwrite('grayscale.jpg', grayscale)
cv2.imwrite('blue.jpg', blue)
cv2.imwrite('green.jpg', green)
cv2.imwrite('red.jpg', red)
