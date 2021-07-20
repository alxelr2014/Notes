import matplotlib.pyplot as plt
import numpy as np


def xor_dataset():
    points = {'+': {'green': [(1, 1), (-1, -1)]}, '_': {'red': [(-1, 1), (1, -1)]}}
    for _marker in points:
        color_map = points[_marker]
        for _colour in color_map:
            data = color_map[_colour]
            x = []
            y = []
            for _point in data:
                x.append(_point[0])
                y.append(_point[1])
            plt.scatter(x, y, s=200, c=_colour, marker=_marker, linewidths=3.0, zorder=3.0)
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    plt.grid(zorder=0.5)

    plt.show()


def xor_3d():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    points = {'+': {'green': [(1, 1, 1), (-1, -1, 1)]}, '_': {'red': [(-1, 1, -1), (1, -1, -1)]}}
    for _marker in points:
        color_map = points[_marker]
        for _colour in color_map:
            data = color_map[_colour]
            x = []
            y = []
            z = []
            for _point in data:
                x.append(_point[0])
                y.append(_point[1])
                z.append(_point[2])
            ax.scatter(x, y, z, s=200, c=_colour, marker=_marker, linewidths=3.0, zorder=3.0, depthshade=False)
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    xx, yy = np.meshgrid(range(-2,3), range(-2,3))
    zz = xx - xx
    print(zz)

    # plot the plane
    ax.plot_surface(xx, yy, zz, alpha=0.25)
    plt.grid(zorder=0.5)
    plt.show()

