import numpy as np
import matplotlib.pyplot as plt

# 특정 서브플롯 axis에 벡터 v를 시작점 start에서 출발하도록 그림
# 화살표의 폭, 머리의 크기, 화살표 색상을 지정하고 선 스타일은 ls로 지정 가능
def draw_vector(axis, v, start = (0,0), 
                width = 1, headsize=0.3, color='k', ls='-'):
   
    # 인자에 따라 적절한 화살표를 그린다. 
    axis.arrow(start[0], start[1],
               v[0], v[1],
               linewidth = width, 
               head_width=headsize, head_length=headsize, 
               fc=color, ec=color,
               length_includes_head = True, ls = ls)


def draw_vector3d(axis, v, start = (0,0,0) , color='k', ls='-', arrow=True):
    if arrow == True:
        axis.quiver(start[0], start[1], start[2],
                    v[0], v[1], v[2], color=color, ls=ls)
    else:
        axis.plot([start[0], v[0]+start[0]],
                  [start[1], v[1]+start[1]],
                  [start[2],v[2]+start[2]], color=color, ls=ls)



def draw_vectors(vector_list, start = (0,0,0), color_list = [], figsize=(10,10)) :


    if vector_list != None and len( vector_list) > 0:
        if len(vector_list) != len(color_list) :
            if len(color_list) > 0:
                 colors = [color_list[0] for _ in range(len(vector_list))]
            else:
                 colors = ['k' for _ in range(len(vector_list))]
        else:
             colors = color_list
    dim = len(vector_list[0])
    print(dim)
    # figure and axis preparation
    
    flatten_numbers = np.array(vector_list).flatten()
    minvalue = flatten_numbers.min()
    maxvalue = flatten_numbers.max()
    d = maxvalue - minvalue
    minvalue -= d*0.25
    maxvalue += d*0.25

    if dim == 2:
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlim([minvalue, maxvalue])
        ax.set_ylim([minvalue, maxvalue])
        ax.grid(True)
        for v, c in zip(vector_list, colors):            
            draw_vector(ax, v, color=c, start=start)
        plt.show()
    if dim == 3:
        fig = plt.figure(figsize = figsize)   # figure 크기를 결정
        ax = fig.gca(projection='3d')  
        ax.set_xlim([minvalue, maxvalue])
        ax.set_ylim([minvalue, maxvalue])
        ax.set_zlim([minvalue, maxvalue])
        ax.grid(True)
        for v, c in zip(vector_list, colors):
            draw_vector3d(ax, v, color=c, start=start)
        plt.show()

def draw_matrix(mat, figsize=(10, 10)):
    cols = mat.shape[1]
    color = ['r', 'g', 'b' ]
    vectors = []
    colors = []
    for i in range(cols):
        vectors.append(mat[:, i])
        colors.append(color[i%3])

    dim = vectors[0].shape[0]
    
    flatten_numbers = np.array(vectors).flatten()
    minvalue = flatten_numbers.min()
    maxvalue = flatten_numbers.max()
    d = maxvalue - minvalue
    minvalue -= d*0.25
    maxvalue += d*0.25
    
    if dim == 2:
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlim([minvalue, maxvalue])
        ax.set_ylim([minvalue, maxvalue])
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.grid(True)
        u = vectors[0]
        v = vectors[1]
        for vec, c in zip(vectors, colors):            
            draw_vector(ax, vec, color=c, start=(0,0))
        vectors = [-u,-v]
        for vec, c in zip(vectors, colors):
            draw_vector(ax, vec, start=u+v, color='gray', ls='--', headsize=0)
        plt.show()
        
    if dim == 3:
        fig = plt.figure(figsize = figsize)   # figure 크기를 결정
        ax = fig.gca(projection='3d')  
        ax.set_xlim([minvalue, maxvalue])
        ax.set_ylim([minvalue, maxvalue])
        ax.set_zlim([minvalue, maxvalue])
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_zlabel('$z$')
        ax.grid(True)
        u = vectors[0]
        v = vectors[1]
        w = vectors[2]
        for vec, c in zip(vectors, colors):
            draw_vector3d(ax, vec, color=c, start=(0,0,0))
        colors = ['r', 'g', 'b']
        vectors = [-u, v, -w]
        for vec, c in zip(vectors, colors):
            draw_vector3d(ax, vec, start=u+w, color='gray', ls='--', arrow=False)
        vectors = [-u,-v, w]
        for vec, c in zip(vectors, colors):
            draw_vector3d(ax, vec, start=u+v, color='gray', ls='--', arrow=False)
        vectors = [u, -v,-w]
        for vec, c in zip(vectors, colors):
            draw_vector3d(ax, vec, start=v+w, color='gray', ls='--', arrow=False)
        plt.show()
