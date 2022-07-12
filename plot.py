import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True

# 上記のライブラリをインストールの上、Latexのインストールが必要です。(表示にLatexを用いている為)

fig = plt.figure(figsize=(6,4))
ax = Axes3D(fig)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$z$')

# define each vector----
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

# 上記のベクトル(O原点)をプロット
ax.plot(xa, ya, za, "-", color="#ff0000", ms=6, mew=0.5,label = r"$\vec{a}$")
ax.plot(xb, yb, zb, "-", color="#00ff00", ms=6, mew=0.5,label = r"$\vec{b}$")
ax.plot(xc, yc, zc, "-", color="#0016ff", ms=6, mew=0.5,label = r"$\vec{c}$")
ax.plot(xf, yf, zf, "-", color="#f400ff", ms=12, mew=0.5,label = r"$\vec{f}$")

def plot_plane(ax, param, xrange, yrange, pcolor="blue", alpha=0.15):

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

# 平面のx,y軸の範囲
xr = [0, 3.1]
yr = [-2, 3.1]

# 平面をプロット
plot_plane(ax, param, xr, yr)

# ラベル(凡例)のプロット
plt.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1, 0.9))

# #png export-----------------------
# for i in range(180): # 回転のため
#     ax.view_init(elev=10, azim=(i)*2)
#     plt.savefig("images/"+str(i+1)+".png")
#     print("saved"+str(i+1))
# #---------------------------------

# #svg export-----------------------
# for i in range(180): # 回転のため
#     ax.view_init(elev=10, azim=(i)*2)
#     plt.savefig("images_svg/"+str(i+1)+".svg")
#     print("saved"+str(i+1))
# #---------------------------------

# 表示
plt.show()