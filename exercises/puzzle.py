# Source code for 2. Make a Puzzle  exercise
# Run: python puzzle.py <image_name> <no pixels/block side> <border thickness in pixels>

import cv2
import numpy as np
import sys
import random

# Input: which image to scramble, 
# the number of pixels on one side of a square block, 
# the number of pixels for border between blocks
# Output: scrambled image
def scrambleImage(image, pixs, addBorder):
	scrambled = image.copy()

	no_rows = scrambled.shape[0]
	no_cols = scrambled.shape[1]

	rows_n = (no_rows/pixs)*pixs
	cols_n = (no_cols/pixs)*pixs

	# resize to make sure each block has the same number of pixels from the initial image
	scrambled = cv2.resize(scrambled, (cols_n, rows_n))

	# store all the blocks in a list, which we shuffle later and remerge
	allBlocks = []

	# for loops to extract all blocks
	for row in range(rows_n-pixs+1):
		for col in range(cols_n-pixs+1):
			if (row % pixs == 0 and col % pixs == 0):
				block = scrambled[row:row+pixs, col:col+pixs].copy()
				allBlocks.append(block)

	# randomly shuffle
	random.shuffle(allBlocks)

	# recompute the number of rows and columns after border is added
	hm_rows = rows_n/pixs
	hm_cols = cols_n/pixs
	rows_n = rows_n + 2*hm_rows*addBorder
	cols_n = cols_n + 2*hm_cols*addBorder
	scrambled = np.zeros((rows_n, cols_n, 3), np.uint8)
	pixs = pixs + 2*addBorder

	next_block = 0

	# reassemble the blocks
	for row in range(rows_n-pixs+1):
		for col in range(cols_n-pixs+1):
			if (row % pixs == 0 and col % pixs == 0):
				cur_block = allBlocks[next_block].copy()
				next_block += 1
				with_borders = cv2.copyMakeBorder(cur_block,
					addBorder,addBorder,addBorder,addBorder,cv2.BORDER_CONSTANT,value = 0)
				scrambled[row:row+pixs, col:col+pixs] = with_borders

	return scrambled

image_name = sys.argv[1]
pix_per_square = int(sys.argv[2])
border_thick = int(sys.argv[3])
image = cv2.imread(image_name)

scrambled = scrambleImage(image, pix_per_square, border_thick)

cv2.imwrite(str(pix_per_square) + '_scrambled_' + image_name, scrambled)

