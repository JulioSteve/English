import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

N = int(50)
a = 0
b = 3

X0 = np.random.rand(N)
X = a+(b-a)*X0
Y0 = np.random.rand(N)


X_lin = np.linspace(a,b,1000)
f = lambda x: np.tanh(x)
y_min = min(f(X_lin))
y_max = max(f(X_lin))

Y = y_min+(y_max-y_min)*Y0

# F = lambda x: np.log(np.cosh(x))

def plot(flag):
    if flag:
        fig,ax = plt.subplots(layout="constrained")
        ax.plot(X_lin,f(X_lin), color="red", lw=5, label=r"$f(x)$")
        ax.plot(X,Y, marker="x", color="black", ls="None", markersize=7, label="Random points")
        ax.fill_between(X_lin,f(X_lin),y_min, color="green", alpha=0.5)
        ax.legend(fontsize=15, loc="upper left", framealpha=1)
        ax.set_xticks([a,0,b], [r"$a$", "0",r"$b$"], size=15)
        ax.set_yticks([y_min,0,y_max], [r"$y_{min}$", "0",r"$y_{max}$"], size=15)
        ax.grid()
        ax.set_xlabel(r'$x$', size=20)
        ax.set_ylabel(r"$y$", size=20)

        # ax.plot(Xa,Ya,marker="o", color="blue", ls="None")
        
        # plt.show()

        plt.savefig("Basic_Int.pdf", format="pdf", dpi=1200)

def accept(points,f):
    X,Y = points
    mask = (Y<=f(X))
    return np.sum(mask), (X[mask],Y[mask])

Nacc, (Xa,Ya) = accept((X,Y),f)
plot(True)

p = Nacc/N
A = (b-a)*(y_max-y_min)
I = (b-a)*y_min+A*p
print(f"I_MC = {I:.3f}")

I_res = quad(f,a,b)[0]
print(f"I_ex = {I_res:.3f}")