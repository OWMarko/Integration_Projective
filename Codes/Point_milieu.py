import numpy as np 

def PointMilieu(x0, f, T, N): 
    dt = T / (N - 1) 
    t = np.linspace(0, T, N) 
    x = np.zeros(N) 
    x[0] = x0 
    for k in range(1, N): 
        tk = t[k-1] + dt / 2 
        xk = x[k-1] + (dt / 2) * f(t[k-1], x[k-1]) 
        x[k] = x[k-1] + dt * f(tk, xk) 
        return t,x