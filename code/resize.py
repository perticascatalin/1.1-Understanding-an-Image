# Resizes an image with a given ratio

import cv2
import numpy as np
import sys

image_name = sys.argv[1]
ratio = float(sys.argv[2])
image = cv2.imread(image_name)
rows, cols, ch = image.shape
n_rows = int(float(rows)/ratio)
n_cols = int(float(cols)/ratio)
image = cv2.resize(image, (n_cols, n_rows))
cv2.imwrite('resized.jpg', image)