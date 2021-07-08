import matplotlib.pyplot as plt
import numpy as np
import math

import importlib.util
spec = importlib.util.spec_from_file_location("draw", "../src/drawvec/draw.py")
draw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(draw)

## When Installed, import can be done as follows:
# from drawvec import draw

A = np.array([[2, 1],
              [0, 3],])
B = np.array([[2, 1],
              [1, 2],])
s = 1.5
ax = draw.createAxis2d(-1, 6, subplot=(1,4), figsize=(20,10))
draw.draw_matrix(  A, axis = ax[0])
draw.draw_matrix(s*A, axis = ax[1])
draw.draw_matrix(  B, axis = ax[2])
draw.draw_matrix(s*B, axis = ax[3])
plt.show()              # 모두 화면에 나타나게 함


A = np.array([[2, 1, 0],
              [0, 3, 1],
              [0, 1, 3],])

s = 2
ax = draw.createAxis3d(-1, 8, subplot=(1,2), figsize=(20,10))
draw.draw_matrix(  A, axis = ax[0])
draw.draw_matrix(s*A, axis = ax[1])
plt.show()