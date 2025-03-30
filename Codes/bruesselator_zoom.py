import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

A = 1.0
B = 1.7

def brusselator(y, t):
    X, Y = y
    dXdt = A + X**2 * Y - B * X - X
    dYdt = B * X - X**2 * Y
    return [dXdt, dYdt]

def euler_explicite(f, y0, t0, tf, h):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + h * np.array(f(y[i-1], t[i-1]))
    return t, y


def integra_proj(f, y0, t0, tf, h, k):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        yt = y[i-1]
        for j in range(k):
            yt += (h / k) * np.array(f(yt, t[i-1] + j * (h / k)))
        diff_div = (np.array(f(yt, t[i-1] + h)) - np.array(f(yt, t[i-1]))) / h
        y[i] = yt - h * diff_div
    return t, y

#Paramètres
y0 = [1.0, 1.0] 
t0 = 0.0
tf = 10.0
h = 0.1
k = 500

#Solutions
t_exact = np.arange(t0, tf, h)
y_exact = odeint(brusselator, y0, t_exact)
t_euler, y_euler = euler_explicite(brusselator, y0, t0, tf, h)
t_proj, y_proj = integra_proj(brusselator, y0, t0, tf, h, k)


X_exact, Y_exact = y_exact[:, 0], y_exact[:, 1]
X_euler, Y_euler = y_euler[:, 0], y_euler[:, 1]
X_proj, Y_proj = y_proj[:, 0], y_proj[:, 1]



#Illustrations
plt.figure(figsize=(10, 6))
plt.plot(t_exact, X_exact, label="Exact X(t)", linestyle='dashed', color ="navy")
plt.plot(t_euler, X_euler, label="Euler explicite X(t)", color = "teal")
plt.plot(t_proj, X_proj, label="Intégration projective X(t)", color = "magenta")
plt.xlabel("Temps (t)")
plt.ylabel("X(t)")
plt.legend()
plt.title(f"Comparaison des méthodes | h ={h} & k = {k}")
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t_exact, Y_exact, label="Exact Y(t)", linestyle='dashed', color = "black")
plt.plot(t_euler, Y_euler, label="Euler explicite Y(t)", color = "teal")
plt.plot(t_proj, Y_proj, label="Intégration projective Y(t)", color = "magenta")
plt.xlabel("Temps (t)")
plt.ylabel("Y(t)")
plt.legend()
plt.title(f"Comparaison des méthodes | h ={h} & k = {k}")
plt.grid()
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(X_exact, Y_exact, label="Exact (X, Y)", linestyle='dashed', color="black")
plt.plot(X_euler, Y_euler, label="Euler explicite (X, Y)", color="purple")
plt.plot(X_proj, Y_proj, label="Intégration projective (X, Y)", color="aqua")
plt.xlabel("Concentration X")
plt.ylabel("Concentration Y")
plt.title(f"Portrait de phase | h ={h} & k = {k}")
plt.legend() 
plt.grid()
plt.show()
