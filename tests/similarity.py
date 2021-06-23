import matplotlib.pyplot as plt
import numpy as np
import math

import importlib.util
spec = importlib.util.spec_from_file_location("draw", "../src/drawvec/draw.py")
draw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(draw)

## When Installed, import can be done as follows:
# from drawvec import draw

vectors = []                            # 벡터를 담을 리스트
n_vectors = 30                          # 리스트에 담을 벡터의 개수
for _ in range(n_vectors):              # n_vectors 만큼 반복
    vectors.append( np.random.rand(2) ) # 2차원 벡터를 임의로 생성해 추가

ax = draw.createAxis2d(-0.2, 1.2, figsize=(10,10))
draw.draw_vectors(vectors, axis = ax)   # n_vectors 개수의 벡터를 그리기

red_vec = np.random.rand(2)             # 빨간색으로 그릴 임의의 벡터
draw.draw_vectors([red_vec], color_list=['r'], axis = ax) # 추가 그리기

plt.show()                              # 모두 화면에 나타나게 함


def cos_sim(u, v):
    return u.dot(v)/(u.dot(u)*v.dot(v))

similarity = np.array( [cos_sim(red_vec, vectors[i]) for i in range(n_vectors)] )
similar_vec_index = similarity.argmax()

ax = draw.createAxis2d(-0.2, 1.2, figsize=(10,10))
draw.draw_vectors([vectors[similar_vec_index], red_vec], color_list=['b', 'r'], axis = ax)
plt.show()