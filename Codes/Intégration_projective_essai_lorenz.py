import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from mpl_toolkits.mplot3d import Axes3D

def lorenz_systeme(etat, t, sigma=10, rho=28, beta=8/3):
    x, y, z = etat
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz])

def euler_explicite(f, y0, t0, tf, h):
    t_valeurs = np.arange(t0, tf + h, h)
    y_valeurs = np.zeros((len(t_valeurs), len(y0)))
    y_valeurs[0] = y0
    for i in range(1, len(t_valeurs)):
        y_valeurs[i] = y_valeurs[i-1] + h * f(y_valeurs[i-1], t_valeurs[i-1])
    return t_valeurs, y_valeurs

def euler_projectif(f, y0, t0, tf, h_micro, K, T_macro):
    y0 = np.array(y0, dtype=float)
    n = len(y0)
    dt_global = K * h_micro + T_macro
    N = int(np.floor((tf - t0) / dt_global)) + 1
    t_valeurs = np.zeros(N)
    y_valeurs = np.zeros((N, n))
    t_valeurs[0] = t0
    y_valeurs[0] = y0
    for i in range(1, N):
        t_local = t_valeurs[i-1]
        y_local = y_valeurs[i-1].copy()
        for j in range(K):
            y_local = y_local + h_micro * f(y_local, t_local)
            t_local += h_micro
        y_extra = y_local + h_micro * f(y_local, t_local)
        pente = (y_extra - y_local) / h_micro
        temps_projection = T_macro - (K + 1) * h_micro
        y_projete = y_extra + temps_projection * pente
        y_valeurs[i] = y_projete
        t_valeurs[i] = t_valeurs[i-1] + dt_global
    return t_valeurs, y_valeurs

y0 = [0.0, 1.0, 1.05]
t0 = 0.0
tf = 30.0
h_micro = 0.005
T_macro = 0.04
K = 3
dt_global = K * h_micro + T_macro


t_exact = np.arange(t0, tf, 0.001)
y_exact = odeint(lambda y, t: lorenz_systeme(y, t), y0, t_exact)
t_euler, y_euler = euler_explicite(lorenz_systeme, y0, t0, tf, dt_global)
t_proj, y_proj = euler_projectif(lorenz_systeme, y0, t0, tf, h_micro, K, T_macro)
y_ref_interp = np.zeros(y_proj.shape)


for dim in range(y_proj.shape[1]):
    fonction_interp = interp1d(t_exact, y_exact[:, dim], kind='linear')
    y_ref_interp[:, dim] = fonction_interp(t_proj)
erreur_proj = y_ref_interp - y_proj
erreur_absolue_proj = np.abs(erreur_proj)
norme_erreur = np.linalg.norm(erreur_proj, axis=1)
print("Erreurs (norme L2) par macro temps :")
print(norme_erreur)
print("\nErreur moyenne (norme L2) :", np.mean(norme_erreur))
print("Erreur maximale (norme L2) :", np.max(norme_erreur))



fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot(y_exact[:, 0], y_exact[:, 1], y_exact[:, 2], color='black', lw=0.5)
ax1.set_title("odeint (référence)")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")


ax2 = fig.add_subplot(132, projection='3d')
ax2.plot(y_euler[:, 0], y_euler[:, 1], y_euler[:, 2], 'b-o', markersize=2)
ax2.set_title("Euler explicite")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")


ax3 = fig.add_subplot(133, projection='3d')
ax3.plot(y_proj[:, 0], y_proj[:, 1], y_proj[:, 2], 'r-s', markersize=4)
ax3.set_title("Euler projectif")
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.set_zlabel("Z")


plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 5))
plt.plot(t_proj, norme_erreur, 'r-s', label="Erreur L2 de la méthode projective")
plt.xlabel("Temps")
plt.ylabel("Norme L2 de l'erreur")
plt.title("Évolution de l'erreur de la méthode projective")
plt.legend()


plt.grid(True)
plt.show()
