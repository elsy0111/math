""" --------------------------------------
Author  : 3I 17  Saito Kengo
Repository    :  github.com/elsy0111/math/3I
    -------------------------------------- """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['text.usetex'] = True

# ================ Define ================= #
# define pi
pi = np.pi
# define x-range
x = np.arange(-5*pi, 5*pi + 0.1, 0.1)

# define function x sin(x)
def func(x):
    y = x * np.sin(x)
    return y
# ================ Define ================= #


# ================= Plot ================== #
# plot x sin(x)
y = func(x)
plt.plot(x,y,linewidth = 0.8,color = "blue",label = r"$f(x) = x\sin x$")

# plot x
y = x
plt.plot(x,y,linewidth = 0.8,color = "gray",linestyle = "dashed",label = r"$g(x) = \pm x$")   

# plot -x
y = -x
plt.plot(x,y,linewidth = 0.8,color = "gray",linestyle = "dashed")
# ================= Plot ================== #

# =============== Plot Axis ================ #
plt.axis("off")
y = 0 * x

plt.plot(x,y,linewidth = 0.5,color = "black")
plt.plot(y,x,linewidth = 0.5,color = "black")

for xi in range(-5,6):
    if xi == -1:
        s = r"$-\pi$"
    elif xi == 1:
        s = r"$\pi$"
    elif xi == 0:
        s = r"$" + str(xi) + "$"
    else:
        s = r"$" + str(xi) + "\pi$"
    plt.text(xi*pi-1,-1.6,s,fontsize=10,backgroundcolor = "white")

plt.text(5.2*pi, -0.4, r"$x$", fontsize=12)
plt.text(-0.3, 5.3*pi, r"$y$", fontsize=12)

plt.legend(fontsize=12, loc='upper right', bbox_to_anchor=(1.03, 1.03)) 

# =============== Plot Axis ================ #

plt.show()

plt.savefig("images_svg/img.svg")