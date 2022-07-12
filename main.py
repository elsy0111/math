import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True

fig = plt.figure()
ax = Axes3D(fig)

#define each vector----
xa = [0, 1]
ya = [0, 3]
za = [0, 5]

xb = [0,2]
yb = [0,-2]
zb = [0,4]

xc = [0,3]
yc = [0,1]
zc = [0,9]

xf = [0,5]
yf = [0,-3]
zf = [0,3]
#---------------------

ax.plot(xa, ya, za, "-", color="#ff0000", ms=6, mew=0.5,label = r"$\vec{a}$")
ax.plot(xb, yb, zb, "-", color="#00ff00", ms=6, mew=0.5,label = r"$\vec{b}$")
ax.plot(xc, yc, zc, "-", color="#0016ff", ms=6, mew=0.5,label = r"$\vec{c}$")
ax.plot(xf, yf, zf, "-", color="#f400ff", ms=12, mew=0.5,label = r"$\vec{f}$")


def plot_plane(axes, param, xrange, yrange, zrange, pcolor="blue", alpha=0.1):

    # 軸ラベルの設定
    axes.set_xlabel("x", fontsize = 16)
    axes.set_ylabel("y", fontsize = 16)
    axes.set_zlabel("z", fontsize = 16)

    # 軸範囲の設定
    axes.set_xlim(xrange[0], xrange[1])
    axes.set_ylim(yrange[0], yrange[1])
    axes.set_zlim(zrange[0], zrange[1])

    # 格子点の作成
    x = np.arange(xrange[0], xrange[1], 0.5)
    y = np.arange(yrange[0], yrange[1], 0.5)
    xx, yy = np.meshgrid(x, y)

    # 平面の方程式
    zz = -(param[0]*xx + param[1]*yy + param[3]) / param[2]

    # 平面をプロット
    ax.plot_surface(xx, yy, zz, color=pcolor, alpha=alpha)

# a,b,c,dを設定
param = [-22, -6, 8, 0]

# x,y,z軸の範囲
xr = [0, 5]
yr = [-5, 5]
zr = [0, 5]

# 平面をプロット
plot_plane(ax, param, xr, yr, zr)

"""
linesux = [1,3]
linesuy = [3,1]
linesuz = [5,9]


linetux = [1,-1]
linetuy = [3,-3]
linetuz = [5,-5]


ax.plot(linesux, linesuy, linesuz, "--", color="#f4ff00", ms=12, mew=0.5)
ax.plot(linetux, linetuy, linetuz, "--", color="#ff8500", ms=12, mew=0.5)
"""

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$z$')
ax.legend()


for i in range(1):
		ax.view_init(elev=30, azim=(i)*2)
		plt.savefig("images/"+str(i+1)+".svg")
plt.show()
