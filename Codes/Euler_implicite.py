import numpy as np
import matplotlib as mpltb
import math
from Newton import Newton

def Eulerimplicite(x0, f, df, T, N): 
    dt = T / (N - 1) 
    t = np.linspace(0, T, N) 
    x = np.zeros(N) 
    x[0] = x0 
    for k in range(1, N): 
        xk = x[k-1] 
        tk = t[k] 
        g = lambda y: y - xk - dt * f(tk, y) 
        dg = lambda y: 1 - dt * df(tk, y) 
        x[k] = Newton(xk, g, 10, 1e-10, 1e-10, tk, dt, xk) 
    return t, x