import numpy as np

def euler_explicit(t0, tf, f, y0, N):
    y0 = np.atleast_1d(y0)
    m = y0.size
    y = np.zeros((m, N+1))
    y[:, 0] = y0
    for n in range(N):
        y[:, n+1] = y[:, n] + h * f(t[n], y[:, n])
    return t, y
