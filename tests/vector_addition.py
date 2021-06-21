import matplotlib.pyplot as plt
import numpy as np

import importlib.util
spec = importlib.util.spec_from_file_location("draw", "../src/drawvec/draw.py")
draw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(draw)

## When Installed, import can be done as follows:
# from drawvec import draw


dim = 3

u = np.array( np.random.randn(dim)*2)
v = np.array( np.random.randn(dim)*2)
w = np.array( np.random.randn(dim)*2)

draw.draw_vectors([u, v, w], color_list=['r', 'g', 'b' ], linked=True)

draw.draw_vectors([u + v + w], color_list=['k'], linked=True)

