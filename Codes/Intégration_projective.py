import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Notre système d'équations différentielles raides
def f(y, t):
    return -15 * y

#Euler explicite
def euler_explicite(f, y0, t0, tf, h):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + h * np.array(f(y[i-1], t[i-1]))
    return t, y

#Intégration projective
def integra_proj(f, y0, t0, tf, h, k):
    t = np.arange(t0, tf, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        yt = y[i-1]  
        for j in range(k):
            yt = yt + (h / k) * f(yt, t[i-1] + j * (h / k))
        y[i] = y[i-1] + h * f(yt, t[i-1])
        Diff_divise = (f(yt, t[i-1] + h) - f(yt, t[i-1])) / h
        y[i] = yt - h * Diff_divise
    return t, y

#PFE
def pfe (f, y0, t0, tf, h_micro, K, T_macro):\n
    y0 = np.array(y0, dtype=float)  #on vectorise la condition initial\n",
    n= len(y0)\n",
    dt_global =  K * h_micro + T_macro # delta temps entre chaque iteration pfe\n",
    N= int(np.floor((tf - t0) / dt_global)) # calcule le nombre exact d'iteration pfe (on peut ajouter une derniere iteration avec pas ajuster pour finir exactement a tf *non fait ici*)\n",
    y_f=np.zeros((N,n))\n",
    t_f = np.zeros(N)\n",
    y_f[0]= y0\n",
    t_f[0]= t0\n",
    for i in range (1,N)
        yt=y_f[i-1].copy()
        for j in range(1,K):
               yt= yt + h_micro*f(yt,t_f[i-1] + j*h_micro)
               yt_2 = yt +  h_micro*f(yt,t_f[i-1] + K*h_micro)
               pente = (yt_2 - yt)/h_micro
               y_proj = yt_2 + (T_macro - (K + 1) * h_micro) * pente
               y_f[i] = y_proj\n",
               t_f[i] = t_f[i - 1] + dt_global\n",
        return t_f, y_f
        
#Paramètres intégration projective
y0 = [1]
t0 = 0
tf = 1
h = 0.01 # pas
k = 100 # pas int proj

#Comparaisons et test
t_exact = np.arange(t0, tf, h)
y_exact = odeint(f, y0, t_exact)
t_euler_exp, y_euler_exp = euler_explicite(f, y0, t0, tf, h)
t_projective, y_projective = integra_proj(f, y0, t0, tf, h, k)

plt.plot(t_exact, y_exact, label='Solution exacte', linestyle='dashed')
plt.plot(t_euler_exp, y_euler_exp, label='Euler explicite', linestyle='dashed')
plt.plot(t_projective, y_projective, label='Intégration projective')

#Zoom sur la courbure
plt.xlim(0, 0.05)
plt.ylim(0.1, 1)

plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Comparaison')
plt.show()
