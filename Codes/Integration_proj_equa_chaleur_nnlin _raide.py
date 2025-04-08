import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Notre équation différentielle raide (équation de la chaleur non linéaire raide)
def heat_eq(t, y, dx, nx):
    dydx2 = np.zeros_like(y)
    dydx2[1:-1] = (y[2:] - 2*y[1:-1] + y[:-2]) / dx**2
    dydx2[0] = (y[1] - y[0]) / dx**2  # Condition aux limites
    dydx2[-1] = (y[-2] - y[-1]) / dx**2  # Condition aux limites
    return dydx2 - 1000 * y

# Euler explicite
def euler_explicite(f, y0, t0, tf, h, dx, nx):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1], dx, nx)
    return t, y

# Intégration projective
def integra_proj(f, y0, t0, tf, h, k, dx, nx):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        yt = y[i-1]
        for j in range(k):
            yt = yt + (h / k) * f(t[i-1] + j * (h / k), yt, dx, nx)
        y[i] = y[i-1] + h * f(t[i-1], yt, dx, nx)
        Diff_divise = (f(t[i-1] + h, yt, dx, nx) - f(t[i-1], yt, dx, nx)) / h
        y[i] = yt - h * Diff_divise
    return t, y

# Paramètres
nx = 100  # Nombre de points spatiaux
dx = 1 / (nx - 1)  # Pas spatial
y0 = np.sin(np.linspace(0, np.pi, nx))  # Condition initiale
t0 = 0
tf = 0.01
h = 0.0001  # Pas temporel
k = 100  # Pas int proj

# Comparaisons et test
t_exact = np.arange(t0, tf, h)
sol = solve_ivp(heat_eq, [t0, tf], y0, method='RK45', t_eval=t_exact, args=(dx, nx))
t_euler_exp, y_euler_exp = euler_explicite(heat_eq, y0, t0, tf, h, dx, nx)
t_projective, y_projective = integra_proj(heat_eq, y0, t0, tf, h, k, dx, nx)

plt.plot(sol.t, sol.y[0, :], label='Solution exacte', linestyle='dashed')
plt.plot(t_euler_exp, y_euler_exp[:, 0], label='Euler explicite', linestyle='dashed')
plt.plot(t_projective, y_projective[:, 0], label='Intégration projective')

# Zoom sur la courbure
plt.xlim(0, 0.001)
plt.ylim(-0.1, 1)

plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Comparaison sur l\'équation de la chaleur non linéaire raide')
plt.show()
