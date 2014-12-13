## Used to make a grid out of a map, as example in 1.1 Understanding an Image

import cv2
import numpy as np
import sys

image_name = sys.argv[1]
image = cv2.imread(image_name)
no_rows = image.shape[0]
no_cols = image.shape[1]
pix = 20
t_rows = (no_rows/pix)*pix
t_cols = (no_cols/pix)*pix
image = cv2.resize(image, (t_cols, t_rows))
image_b = cv2.copyMakeBorder(image,0,pix,0,pix,cv2.BORDER_CONSTANT,value = 0)
no_rows = image_b.shape[0]
no_cols = image_b.shape[1]

blue_pixel = np.zeros((pix,pix,3), np.uint8)
green_pixel = np.zeros((pix,pix,3), np.uint8)
red_pixel = np.zeros((pix,pix,3), np.uint8)

mask = np.ones((pix,pix), np.uint8)

blue_pixel[mask == 1] = (255,0,0)
green_pixel[mask == 1] = (0,255,0)
red_pixel[mask == 1] = (0,0,255)

# place some pixels at different positions
image_b[3*pix:4*pix,5*pix:6*pix] = red_pixel
image_b[13*pix:14*pix, 8*pix:9*pix] = green_pixel
image_b[10*pix:11*pix, 21*pix:22*pix] = blue_pixel


for row in range(no_rows-pix+1):
	for col in range(no_cols-pix+1):
		if (row % pix) == 0:
			image_b[row, col] = (0,255,0)
		if (col % pix) == 0:
			image_b[row, col] = (0,255,0)

image_b = cv2.copyMakeBorder(image_b,pix,0,pix,0,cv2.BORDER_CONSTANT,value = 0)
cv2.imwrite('street_house.jpg', image_b)

