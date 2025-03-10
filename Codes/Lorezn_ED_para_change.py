import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate


def solve_lorenz(sigma=10.0, beta=8./3, rho=28.0):
    tps_max = 4.0
    N = 30

    graph = plt.figure(1)
    ax = graph.add_axes([0, 0, 1, 1], projection='3d')
    ax.axis('off')
    ax.set_xlim((-25, 25))
    ax.set_ylim((-35, 35))
    ax.set_zlim((5, 55))
    
    def lorenz_der(x_y_z, t0, sigma=sigma, beta=beta, rho=rho):
        x, y, z = x_y_z
        return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]

    np.random.seed(1)
    x0 = -15 + 30 * np.random.random((N, 3))

    t = np.linspace(0, max_time, int(250*max_time))
    x_t = []

    for x0i in x0:
        sol = integrate.odeint(lorenz_deriv, x0i, t)
        x_t.append(sol)

    x_t = np.asarray(x_t)

    colors = plt.cm.viridis(np.linspace(0, 1, N))


    for i in range(N):
        x, y, z = x_t[i,:,:].T
        lines = ax.plot(x, y, z, '-', c=colors[i])
        plt.setp(lines, linewidth=2)
    angle = 104
    ax.view_init(30, angle)
    plt.show()

    return t, x_t
