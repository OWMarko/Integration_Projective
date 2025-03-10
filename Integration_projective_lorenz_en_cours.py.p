import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

def lorenz_deriv(x_y_z, t0, sigma=10.0, beta=8./3, rho=28.0):
    x, y, z = x_y_z
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]

# Euler explicite
def euler_explicite(f, y0, t0, tf, h, sigma, beta, rho):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + h * np.array(f(y[i-1], t[i-1], ))
    return t, y

# Intégration projective
def integra_proj(f, y0, t0, tf, h, k, sigma, beta, rho):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        yt = y[i-1]
        for j in range(k):
            yt = yt + (h / k) * np.array(f(yt, t[i-1] + j * (h / k), )
        y[i] = y[i-1] + h * np.array(f(yt, t[i-1], sigma, beta, rho))
        Diff_divise = (np.array(f(yt, t[i-1] + h, sigma, beta, rho)) - np.array(f(yt, t[i-1], ))) / h
        y[i] = yt - h * Diff_divise
    return t, y

# Paramètres intégration projective
y0 = [1, 1, 1]
t0 = 0
tf = 25
h = 0.01 # pas
k = 100 # pas int proj
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# Comparaisons et test
t_exact = np.arange(t0, tf, h)
y_exact = integrate.odeint(lorenz_deriv, y0, t_exact, arg
t_euler_exp, y_euler_exp = euler_explicite(lorenz_deriv, y0, t0, tf, h, 
t_projective, y_projective = integra_proj(lorenz_deriv, y0, t0, tf, h, k, )

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(y_exact[:,0], y_exact[:,1], y_exact[:,2], label='Solution exacte', linestyle='dashed')
ax.plot(y_euler_exp[:,0], y_euler_exp[:,1], y_euler_exp[:,2], label='Euler explicite', linestyle='dashed')
ax.plot(y_projective[:,0], y_projective[:,1], y_projective[:,2], label='Intégration projective')

