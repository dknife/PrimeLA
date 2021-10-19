import matplotlib.pyplot as plt
import numpy as np
import math

import sys
sys.path.insert(0, 'src')
from drawvec import draw

## When Installed, import can be done as follows:
# from drawvec import draw

A = np.array([[2, 1],
              [0, 3],], dtype=float)
B = np.array([[-2, 1],
              [1, 2],], dtype=float)


print(A)
print(B)

def mult(A, B):
    C = np.zeros((A.shape[0], B.shape[1]), dtype=float)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]
    return C

C = mult(A, B)
print(C)

print(A*B)

print(A.dot(B))
print(A @ B)

ax = draw.createAxis2d(-3, 10, subplot=(2,2), figsize = (10, 10))

draw.draw_matrix(A, axis = ax[0,0])
draw.draw_matrix(B, axis = ax[0,1])
draw.draw_matrix(mult(A, B), axis = ax[1,0])
draw.draw_matrix(A @ B, axis = ax[1,1])
plt.show()
