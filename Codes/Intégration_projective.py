import numpy as np

def pfe(f, y0, t0, tf, h_micro, K, T_macro):
    y0 = np.array(y0, dtype=float)
    n = len(y0)
    dt_global = (K + 1) * h_micro + T_macro
    N = int(np.floor((tf - t0) / dt_global))
    y_f = np.zeros((N, n))
    t_f = np.zeros(N)
    y_f[0] = y0
    t_f[0] = t0
    for i in range(1, N):
        yt = y_f[i - 1].copy()
        for j in range(K):
            yt = yt + h_micro * f(yt, t_f[i - 1] + j * h_micro)
        yt_2 = yt + h_micro * f(yt, t_f[i - 1] + K * h_micro)
        pente = (yt_2 - yt) / h_micro
        y_proj = yt_2 + (dt_global - (K + 1) * h_micro) * pente
        y_f[i] = y_proj
        t_f[i] = t_f[i - 1] + dt_global

    return t_f, y_f
