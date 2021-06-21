import matplotlib.pyplot as plt
import numpy as np

import importlib.util
spec = importlib.util.spec_from_file_location("draw", "../src/drawvec/draw.py")
draw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(draw)

## When Installed, import can be done as follows:
# from drawvec import draw


A = np.array([[4, -1, 1],
              [1,  3, 0],
              [1,  -1, 4]], dtype = float)

u = A[:2, 0]  # 행렬 A의 첫 열벡터 (4,1)
v = A[:2, 1]  # 행렬 A의 두번째 열벡터 (-1,3)

draw.draw_vectors([u, v])


u = np.array([1,0,0])                 # x축 방향 벡터
v = np.array([0,1,0])                 # y축 방향 벡터
w = np.array([0,0,1])                 # z축 방향 벡터

draw.draw_vectors([u, v, w], color_list=['r', 'g', 'b'])

draw.draw_matrix(A[:2, :2])

draw.draw_matrix(A)
