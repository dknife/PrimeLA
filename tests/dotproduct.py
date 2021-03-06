import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.insert(0, 'src')
from drawvec import draw

u = np.array([7.5, -1.2])
v = np.array([3.0, 3.7])

dot_product = 0
for i in range(len(u)):
    dot_product += u[i]*v[i]
print(dot_product)

print(u*v)
print((u*v).sum())

dot_product = u.dot(v)
print(dot_product)
u_norm = np.linalg.norm(u)
v_norm = np.linalg.norm(v)
u_dir = u/u_norm
v_dir = v/v_norm

draw.draw_vectors([u, v,
                   (dot_product/u_norm) * u_dir, (dot_product/v_norm) * v_dir],
                  color_list=['r', 'g', 'b', 'b' ])