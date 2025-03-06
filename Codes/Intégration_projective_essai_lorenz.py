import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Notre système d'équations diff raides
def lorenz(state, t):
    x, y, z = state
    dx_dt = -10 * x + 10 * y
    dy_dt = 28 * x - y - x * z
    dz_dt = -8/3 * z + x * y
    return [dx_dt, dy_dt, dz_dt]

#Euler explicite
def euler_explicite(f, y0, t0, tf, h):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + h * np.array(f(y[i-1], t[i-1]))
    return t, y

#Itégration projective
def integra_proj(f, y0, t0, tf, h, k):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        yt = y[i-1]  
        for j in range(k):
            yt = yt + (h / k) * np.array(f(yt, t[i-1] + j * (h / k)))
        y[i] = y[i-1] + h * np.array(f(yt, t[i-1]))
    return t, y

#Paramètres intégration proj
y0 = np.array([1.0, 0.0, 0.0])
t0 = 0
tf = 1
h = 0.001
k = 10  #pas int proj

#Comparaisons et test
t_exact = np.arange(t0, tf, h)
y_exact = odeint(lorenz, y0, t_exact)
t_euler, y_euler = euler_explicite(lorenz, y0, t0, tf, h)
t_projective, y_projective = integra_proj(lorenz, y0, t0, tf, h, k)

plt.plot(t_exact, y_exact[:, 0], label='Solution exacte - x')
plt.plot(t_exact, y_exact[:, 1], label='Solution exacte - y')
plt.plot(t_exact, y_exact[:, 2], label='Solution exacte - z')

#plt.plot(t_euler, y_euler[:, 0], label='Euler explicite - x', linestyle='dotted')
#plt.plot(t_euler, y_euler[:, 1], label='Euler explicite - y', linestyle='dotted')
#plt.plot(t_euler, y_euler[:, 2], label='Euler explicite - z', linestyle='dotted')

plt.plot(t_projective, y_projective[:, 0], label='Intégration projective - x', linestyle='dashed')
plt.plot(t_projective, y_projective[:, 1], label='Intégration projective - y', linestyle='dashed')
plt.plot(t_projective, y_projective[:, 2], label='Intégration projective - z', linestyle='dashed')

plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Comparaison')
plt.show()
