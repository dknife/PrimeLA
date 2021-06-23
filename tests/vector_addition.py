import matplotlib.pyplot as plt
import numpy as np

import importlib.util
spec = importlib.util.spec_from_file_location("draw", "../src/drawvec/draw.py")
draw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(draw)

## When Installed, import can be done as follows:
# from drawvec import draw


dim = 2

u = np.array( np.random.randn(dim)*2)
v = np.array( np.random.randn(dim)*2)
w = np.array( np.random.randn(dim)*2)

draw.draw_vectors([u, v, w], color_list=['r', 'g', 'b' ], linked=True)

draw.draw_vectors([u + v + w], color_list=['k'], linked=True)

u = np.array([1.0, 3.2, 0])
v = np.array([-1.0, 0.7, 2])
w = np.array([-1.0, -6.0, 0.3])
draw.draw_vectors([u, v, w], color_list=['r', 'g', 'b' ])
draw.draw_vectors([u, v, w, 2*u, 2*v, w/2, 3*u, 3*v,
                   w/3, 4*u, 4*v, w/4], color_list=['r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b' ])


ax = draw.createAxis3d(-8, 8, figsize=(5,5))

draw.draw_vectors([u, v, w], color_list=['r', 'g', 'b' ], axis = ax)
draw.draw_vectors([u, v, w, 2*u, 2*v, w/2, 3*u, 3*v,
                   w/3, 4*u, 4*v, w/4], color_list=['r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b' ], axis=ax)

draw.draw_line(ax, [0,0,0], [5, 5, 0], ls=':')

plt.show()

