# Run: python grayscaleLandscape.py <image_name>
# Plots a kind of landscape from a grayscale image(converts automatically if not)
# The brighter the intensity, the higher the surface point

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

image_name = sys.argv[1]
image = cv2.imread(image_name, 0)
no_rows = image.shape[0]
no_cols = image.shape[1]

X = np.zeros((no_rows, no_cols), np.uint8)
for row in range(no_rows):
	for col in range(no_cols):
		X[row, col] = row

Y = np.zeros((no_rows, no_cols), np.uint8)
for row in range(no_rows):
	for col in range(no_cols):
		Y[row, col] = col


fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(X, Y, image, rstride=1, cstride=1, cmap=cm.gray,
        linewidth=0, antialiased=False)
ax.set_zlim(0.0, 255.0)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()