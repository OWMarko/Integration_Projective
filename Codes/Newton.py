import numpy as np
import matplotlib.pyplot as plt
import math 

def f(t, x):
   y = - 3 * x
   return(y)

def derivef(t, x):
    z = -3
    return (z)

def fonctionG(y, x, t, dt, f):
    G = y - x - dt * f(t, y)
    return (G)

def Newton(x0, f, itermax, epsabs, epsrel, t, dt, x):
   y = x0
   fG = fonctionG(y, x, t, dt, f)
   normeres0 = math.fabs(fG) 
   normeres  = normeres0
   iter0 = 0
   
   while (iter0 < itermax and normeres > epsrel * normeres0 + epsabs):
      iter0 += 1
      deriveG = 1 - dt * derivef(t, y)
      if math.fabs(deriveG) <= np.finfo(float).eps:
         print("La dérivée est nulle")
         break
                
      fG = fonctionG(y, x, t, dt, f)
      y  = y - fG/deriveG
      fG = fonctionG(y, x, t, dt, f)
      normeres = math.fabs(fG) 
      return (y)
