import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

N = int(1e2/2)
a = 0
b = 1

X = np.random.uniform(a,b,N)
X_plot = np.linspace(a,b,N)

f = lambda x: 2*x-10*x**3+5*x**2
y_min = min(f(X_plot))-0.5
y_max = max(f(X_plot))

fm = np.sum(f(X))/N

def plot(flag):
    if flag:
        fig,ax = plt.subplots(layout="constrained")
        ax.hlines(fm,a,b, ls="dashed", lw=5, label=r"$\left<f\right>$", color="red")
        ax.plot(X_plot,f(X_plot), lw=5, color="red",label=r"$f(x)$")
        ax.plot(X,f(X), ls="None", marker='x', markersize=7, color="black", label="Random points")

        ax.fill_between(X_plot,f(X_plot),y_min, color="green", alpha=0.5)
        ax.legend(fontsize=15, loc="lower left", framealpha=1)
        ax.set_xticks([a,0,b], [r"$a$", "0",r"$b$"], size=15)
        ax.set_yticks([y_min,0,y_max], [r"$y_{min}$", "0",r"$y_{max}$"], size=15)
        ax.grid()
        ax.set_xlabel(r'$x$', size=20)
        ax.set_ylabel(r"$y$", size=20)

        # plt.show()
        plt.savefig("Uniform.pdf", format="pdf", dpi=1200)

plot(True)

I = (b-a)*fm
print(f"I_MC = {I:.4f}")

I_res = quad(f,a,b)[0]
print(f"I_ex = {I_res:.4f}")