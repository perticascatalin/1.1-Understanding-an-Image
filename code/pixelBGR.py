# Run: python pixelBGR.py <image_name> <ratio>
# For running default case, set ratio to 1
# Looks at the image under the 'microscope'
# With zooming, only blue, green and red pixels can be seen
# Obtained images saved under: 'BGR.png'

import cv2
import numpy as np
import sys

image_name = sys.argv[1]
ratio = int(sys.argv[2])
image = cv2.imread(image_name)
rows, cols, ch = image.shape
g_ratio = 10
n_rows = rows * ratio * g_ratio
n_cols = cols * ratio * g_ratio
big_ratio = ratio * g_ratio
BGR = np.zeros((n_rows, n_cols, 3), np.uint8)
for row in range(rows):
	for col in range(cols):
		
		B = image[row, col, 0]
		G = image[row, col, 1]
		R = image[row, col, 2]
		background = (0,20,40)
		
		for n_row in range(row*big_ratio + 1, (row+1)*big_ratio - 1):
			for n_col  in range(col*big_ratio + 1, (col+1)*big_ratio - 1):
				BGR[n_row, n_col] = background

		Bratio = float(B)/255.0
		Gratio = float(G)/255.0
		Rratio = float(R)/255.0
		
		Blines = int(Bratio * float(big_ratio))
		Glines = int(Gratio * float(big_ratio))
		Rlines = int(Rratio * float(big_ratio))
		start_col = col*big_ratio
		for n_row in range((row+1)*big_ratio - Blines - 1, (row+1)*big_ratio - 1):
			for n_col in range(start_col + ratio, start_col + 3*ratio):
				BGR[n_row, n_col] = (255,0,0)

		for n_row in range((row+1)*big_ratio - Glines - 1, (row+1)*big_ratio - 1):
			for n_col in range(start_col + 4*ratio, start_col + 6*ratio):
				BGR[n_row, n_col] = (0,255,0)

		for n_row in range((row+1)*big_ratio - Rlines - 1, (row+1)*big_ratio - 1):
			for n_col in range(start_col + 7*ratio, start_col + 9*ratio):
				BGR[n_row, n_col] = (0,0,255)

cv2.imwrite('BGR.png', BGR)