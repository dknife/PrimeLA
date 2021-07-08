import numpy as np
import matplotlib.pyplot as plt
import math

# 특정 서브플롯 axis에 벡터 v를 시작점 start에서 출발하도록 그림
# 화살표의 폭, 머리의 크기, 화살표 색상을 지정하고 선 스타일은 ls로 지정 가능
def draw_vector(axis, v, start = (0,0), 
                width = 1, headsize=0.3, color='k', ls='-'):
   
    # 인자에 따라 적절한 화살표를 그린다.
    s = np.array(start)
    if headsize > 0:
        headsize = np.linalg.norm(v)/15
    axis.arrow(start[0], start[1],
               v[0], v[1],
               linewidth = width, 
               head_width=headsize, head_length=headsize, 
               fc=color, ec=color,
               length_includes_head = True, ls = ls)


def draw_vector3d(axis, v, start = (0,0,0) , color='k', ls='-', arrow=True):
    s = np.array(start)
    if arrow == True:
        axis.quiver(s[0], s[1], s[2],
                    v[0], v[1], v[2], color=color, ls=ls)
    else:
        axis.plot([s[0], v[0]+s[0]],
                  [s[1], v[1]+s[1]],
                  [s[2], v[2]+s[2]], color=color, ls=ls)


def draw_line(axis, start, end, color='k', ls='-'):
    if len(start) == 2:
        axis.plot([start[0], end[0]],
                  [start[1], end[1]], color=color, ls=ls)
    elif len(start) == 3:
        axis.plot([start[0], end[0]],
                  [start[1], end[1]],
                  [start[2], end[2]], color=color, ls=ls)

def draw_vectors(vector_list, start = (0,0,0), color_list = [], figsize=(10,10), linked=False, axis=None) :
    if vector_list != None and len( vector_list) > 0:
        if len(vector_list) != len(color_list) :
            if len(color_list) > 0:
                 colors = [color_list[0] for _ in range(len(vector_list))]
            else:
                 colors = ['k' for _ in range(len(vector_list))]
        else:
             colors = color_list
    dim = len(vector_list[0])
    # figure and axis preparation

    vecsum = np.zeros_like(vector_list[0])
    for v in vector_list:
        vecsum += v
    maxvalue = max(abs(vecsum.min()), abs(vecsum.max())) * 1.1

    if dim == 2:
        s = np.array([start[0], start[1]], dtype=float)
        if axis == None:
            ax = createAxis2d(-maxvalue, maxvalue,  figsize = figsize)
            print(ax)
        else:
            ax = axis
        for v, c in zip(vector_list, colors):
            draw_vector(ax, v, color=c, start=s)
            if linked: s += v
        if linked:
            draw_vector(ax, s, color='k', ls='--', headsize=0.0)
        if axis == None:
            plt.show()
    if dim == 3:
        s = np.array([start[0], start[1], start[2]], dtype=float)
        if axis == None:
            ax = createAxis3d(-maxvalue, maxvalue,  figsize = figsize)
            print(ax)
        else:
            ax = axis
        for v, c in zip(vector_list, colors):
            draw_vector3d(ax, v, color=c, start=s)
            if linked: s += v
        if linked:
            draw_vector3d(ax, s, color='k', ls='--', arrow=False)
        if axis == None:
            plt.show()

def draw_matrix(mat, figsize=(10, 10), axis = None):
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
        if axis == None:
            ax = createAxis2d(-maxvalue, maxvalue, figsize = figsize)
        else:
            ax = axis
        u = vectors[0]
        v = vectors[1]
        for vec, c in zip(vectors, colors):
            draw_vector(ax, vec, color=c, start=(0,0))

        vectors = [-u,-v]
        for vec, c in zip(vectors, colors):
            draw_vector(ax, vec, start=u+v, color='gray', ls='--', headsize=0)
        if axis==None: plt.show()
        
    if dim == 3:
        if axis == None:
            ax = createAxis3d(-maxvalue, maxvalue,  figsize = figsize)
        else:
            ax = axis
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
        if axis==None: plt.show()


def draw_points(mat, figsize=(10, 10), color='k', ls='-', axis=None):

    dim = mat.shape[0]

    flatten_numbers = np.array(mat).flatten()
    minvalue = flatten_numbers.min()
    maxvalue = flatten_numbers.max()
    d = maxvalue - minvalue
    minvalue -= d * 0.25
    maxvalue += d * 0.25

    if dim == 2:
        if axis == None:
            ax = createAxis2d(-maxvalue, maxvalue, figsize=figsize)
        else:
            ax = axis

        ax.plot(mat[0,:], mat[1,:], color=color, ls=ls)
        if axis == None: plt.show()

    if dim == 3:
        if axis == None:
            ax = createAxis3d(-maxvalue, maxvalue, figsize=figsize)
        else:
            ax = axis
        ax.plot(mat[0,:], mat[1,:], mat[2, :], color=color, ls=ls)
        if axis == None: plt.show()

def draw_line(a, b, c, axis, ls = '-', color=None): # draw line: ax + by + c = 0
    if math.fabs(b) > 1e-5 :
        y = - (c / b)
        dir = np.array([1, -a / b])
        if math.fabs(a) > 1e-5:
            x = - (c + b*y) / a
        else:
            x = 0.0
    else:
        y = 0.0
        x = - (c / a)
        dir = np.array([0, 1])

    p = np.array([x, y])
    p0 = p - dir * 10000
    p1 = p + dir* 10000
    axis.plot([p0[0], p1[0]], [p0[1], p1[1]], ls = ls, color=color)


def createAxis2d(minvalue, maxvalue, subplot=(1,1), figsize=(10,10)):

    if subplot == (1,1):
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlim([minvalue, maxvalue])
        ax.set_ylim([minvalue, maxvalue])
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.grid(True)
        return ax
    elif subplot[0] > 1 and subplot[1] > 1:
        fig, ax = plt.subplots(subplot[0], subplot[1], figsize=figsize)  # figure 크기를 결정
        for row in range(subplot[0]):
            for col in range(subplot[1]):
                ax[row, col].set_xlim([minvalue, maxvalue])
                ax[row, col].set_ylim([minvalue, maxvalue])
                ax[row, col].set_xlabel('$x$')
                ax[row, col].set_ylabel('$y$')
                ax[row, col].grid(True)
        return ax
    else:
        dim = max(subplot[0], subplot[1])
        fig, ax = plt.subplots(subplot[0], subplot[1], figsize=figsize)  # figure 크기를 결정
        for d in range(dim):
            ax[d].set_xlim([minvalue, maxvalue])
            ax[d].set_ylim([minvalue, maxvalue])
            ax[d].set_xlabel('$x$')
            ax[d].set_ylabel('$y$')
            ax[d].grid(True)
        return ax


def createAxis3d(minvalue, maxvalue, subplot=(1,1), figsize=(10,10)):

    if subplot == (1,1):
        fig = plt.figure(figsize = figsize)   # figure 크기를 결정
        ax = fig.gca(projection='3d')
        ax.set_xlim([minvalue, maxvalue])
        ax.set_ylim([minvalue, maxvalue])
        ax.set_zlim([minvalue, maxvalue])
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_zlabel('$z$')
        ax.grid(True)
        return ax
    elif subplot[0] > 1 and subplot[1] > 1:
        fig, ax = plt.subplots(subplot[0], subplot[1], figsize = figsize)   # figure 크기를 결정
        i = 1
        for row in range(subplot[0]):
            for col in range(subplot[1]):
                ax[row, col] = fig.add_subplot(subplot[0], subplot[1], i, projection='3d')
                ax[row, col].set_xlim([minvalue, maxvalue])
                ax[row, col].set_ylim([minvalue, maxvalue])
                ax[row, col].set_zlim([minvalue, maxvalue])
                ax[row, col].set_xlabel('$x$')
                ax[row, col].set_ylabel('$y$')
                ax[row, col].set_zlabel('$z$')
                ax[row, col].grid(True)
                i+=1
        return ax
    else:
        dim = max(subplot[0], subplot[1])
        fig, ax = plt.subplots(subplot[0], subplot[1], figsize=figsize)  # figure 크기를 결정
        i = 1
        for d in range(dim):
            ax[d] = fig.add_subplot(subplot[0], subplot[1], i, projection='3d')
            ax[d].set_xlim([minvalue, maxvalue])
            ax[d].set_ylim([minvalue, maxvalue])
            ax[d].set_zlim([minvalue, maxvalue])
            ax[d].set_xlabel('$x$')
            ax[d].set_ylabel('$y$')
            ax[d].set_zlabel('$z$')
            ax[d].grid(True)
            i += 1
        return ax


