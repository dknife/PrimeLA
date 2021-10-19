import matplotlib.pyplot as plt
import numpy as np
import math

import sys
sys.path.insert(0, 'src')
from drawvec import draw

## When Installed, import can be done as follows:
# from drawvec import draw



ax = draw.createAxis3d(-2, 4, subplot=(2,2), figsize=(10,10))
A = np.array([
              [2, 1, -1],
              [0, 2, 0],
              [0, 1, 2],
             ])
B = np.array([
              [2, 1, 1],
              [1, 2, 0],
              [0, 0, 2],
             ])
C = A + B

u1, u2 = A[:, 0], B[:, 0]
v1, v2 = A[:, 1], B[:, 1]
w1, w2 = A[:, 2], B[:, 2]

draw.draw_matrix(A, axis = ax[0,0])
draw.draw_matrix(B, axis = ax[0,1])
draw.draw_matrix(C, axis = ax[1,0])
draw.draw_vectors([u1, u2], linked = True, color_list=['r', 'r'], axis = ax[1,1])
draw.draw_vectors([v1, v2], linked = True, color_list=['g', 'g'], axis = ax[1,1])
draw.draw_vectors([w1, w2], linked = True, color_list=['b', 'b'], axis = ax[1,1])
plt.show()