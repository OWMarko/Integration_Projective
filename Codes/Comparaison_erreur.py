import numpy as np
import matplotlib.pyplot as plt
import math

# Initialisation de notre fonction
def f(t, x):
    return -4 * x

# On définit nos paramètres
itermax = 20
x0 = 1
T = 8
N = 20
epsabs = 10e-18
epsrel = math.sqrt(10e-18)

# Code Euler Explicite
def EulerExplicite(x0, f, T, N):
    t = np.linspace(0, T, N)
    x = np.empty(N)
    dt = T / (N - 1)
    x[0] = x0
    for k in range(N - 1):
        x[k + 1] = x[k] + dt * f(t[k], x[k])
    return t, x

def fonctionG(y, x, t, dt, f):
    G = y - x - dt * f(t, y)
    return G

def derivef(t, x):
    z = -4
    return z

def Newton(x0, f, itermax, epsabs, epsrel, t, dt, x):
    y = x0
    fG = fonctionG(y, x, t, dt, f)
    normeres0 = math.fabs(fG)
    normeres = normeres0
    iter = 0
    while iter < itermax and normeres > epsrel * normeres0 + epsabs:
        iter += 1
        deriveG = 1 - dt * derivef(t, y)
        if math.fabs(deriveG) <= np.finfo(float).eps:
            print('derivee nulle')
            break
        fG = fonctionG(y, x, t, dt, f)
        y = y - fG / deriveG
        fG = fonctionG(y, x, t, dt, f)
        normeres = math.fabs(fG)
    return y

# Code Euler Implicite
def EulerImplicite(x0, f, T, N):
    t = np.linspace(0, T, N)
    x = np.empty(N)
    dt = T / (N - 1)
    x[0] = x0
    for k in range(N - 1):
        x[k + 1] = Newton(x[k], f, itermax, epsabs, epsrel, t[k], dt, x[k])
    return t, x

# Code Point Milieu
def PointMilieu(x0, f, T, N):
    t = np.linspace(0, T, N)
    x = np.empty(N)
    x[0] = x0
    dt = t[1] - t[0]
    for k in range(N - 1):
        xk = x[k] + 0.5 * dt * f(t[k], x[k])
        tk = 0.5 * (t[k] + t[k + 1])
        x[k + 1] = x[k] + dt * f(tk, xk)
    return t, x

# Fonction pour calculer les erreurs
def calculer_erreurs(approx, exacte):
    erreur_absolue = np.abs(approx - exacte)
    erreur_relative = erreur_absolue / np.abs(exacte)
    return erreur_absolue, erreur_relative

# On récupère les sorties de nos fonctions en fonction de nos paramètres
(t, xEulerExplicite) = EulerExplicite(x0, f, T, N)
(t, xEulerImplicite) = EulerImplicite(x0, f, T, N)
(t, xPointMilieu) = PointMilieu(x0, f, T, N)
Exacte = x0 * np.exp(-4 * t)

# Calcul des erreurs
erreur_absolue_EulerExplicite, erreur_relative_EulerExplicite = calculer_erreurs(xEulerExplicite, Exacte)
erreur_absolue_EulerImplicite, erreur_relative_EulerImplicite = calculer_erreurs(xEulerImplicite, Exacte)
erreur_absolue_PointMilieu, erreur_relative_PointMilieu = calculer_erreurs(xPointMilieu, Exacte)

# Préparer les données pour le tableau LaTeX
erreurs_data = {
    'Temps t': t,
    'Erreur abs. Euler exp.': erreur_absolue_EulerExplicite,
    'Erreur rel. Euler exp.': erreur_relative_EulerExplicite,
    'Erreur abs. Euler imp.': erreur_absolue_EulerImplicite,
    'Erreur rel. Euler imp.': erreur_relative_EulerImplicite,
    'Erreur abs. Point milieu': erreur_absolue_PointMilieu,
    'Erreur rel. Point milieu': erreur_relative_PointMilieu
}

# Générer le fichier LaTeX
with open('erreurs_tableau.tex', 'w') as f:
    f.write(r'\documentclass{article}' + '\n')
    f.write(r'\usepackage{booktabs}' + '\n')
    f.write(r'\begin{document}' + '\n')
    f.write(r'\begin{tabular}{ccccccc}' + '\n')
    f.write(r'\toprule' + '\n')
    f.write(r'Temps t & Erreur abs. Euler exp. & Erreur rel. Euler exp. & Erreur abs. Euler imp. & Erreur rel. Euler imp. & Erreur abs. Point milieu & Erreur rel. Point milieu \\' + '\n')
    f.write(r'\midrule' + '\n')
    for i in range(len(t)):
        f.write(f'{t[i]:.2f} & {erreurs_data["Erreur abs. Euler exp."][i]:.2e} & {erreurs_data["Erreur rel. Euler exp."][i]:.2e} & {erreurs_data["Erreur abs. Euler imp."][i]:.2e} & {erreurs_data["Erreur rel. Euler imp."][i]:.2e} & {erreurs_data["Erreur abs. Point milieu"][i]:.2e} & {erreurs_data["Erreur rel. Point milieu"][i]:.2e} \\' + '\n')
    f.write(r'\bottomrule' + '\n')
    f.write(r'\end{tabular}' + '\n')
    f.write(r'\end{document}' + '\n')

# Affichage des résultats
print("Erreur absolue Euler explicite:", erreur_absolue_EulerExplicite)
print("Erreur relative Euler explicite:", erreur_relative_EulerExplicite)
print("Erreur absolue Euler implicite:", erreur_absolue_EulerImplicite)
print("Erreur relative Euler implicite:", erreur_relative_EulerImplicite)
print("Erreur absolue Point milieu:", erreur_absolue_PointMilieu)
print("Erreur relative Point milieu:", erreur_relative_PointMilieu)

# Courbes
plt.clf()
plt.axis([0, 8, -1.0, 1.0])  # Ajustement de l'échelle des axes pour une meilleure visualisation
plt.grid(True)
plt.plot(t, xEulerExplicite, 'ro-', label='Euler explicite')
plt.plot(t, xEulerImplicite, 'bo-', label='Euler implicite')
plt.plot(t, xPointMilieu, 'm^-', label='Point milieu')
plt.plot(t, Exacte, 'gs-', label='Exacte')
plt.title('Comparaison des méthodes numériques')
plt.xlabel('Temps t')
plt.ylabel('x(t)')
plt.legend(loc='best')
plt.show()
