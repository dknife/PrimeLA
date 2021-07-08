import matplotlib.pyplot as plt
import numpy as np

import importlib.util
spec = importlib.util.spec_from_file_location("draw", "../src/drawvec/draw.py")
draw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(draw)

I2 = np.eye(2)
I3 = np.eye(3)
print(I2)
print(I3)
print('det I2 = {}, det I3 = {}'.format(np.linalg.det(I2),
                                        np.linalg.det(I3)))

#draw.draw_matrix(I2)

#draw.draw_points(I3, color='r', ls=':')

ax = draw.createAxis2d(-1, 4)
draw.draw_line(3, -2, -1, ax, ls = '-', color='r')
draw.draw_line(1,  1, -2, ax, ls = '-', color='k')
plt.show()