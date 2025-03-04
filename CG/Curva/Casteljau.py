import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def casteljau_recursive(points, t):
    """ Calcula um ponto na curva Bézier usando o algoritmo de Casteljau de forma recursiva. """
    if len(points) == 1:
        return points[0]
    
    new_points = [(1 - t) * points[i] + t * points[i + 1] for i in range(len(points) - 1)]
    return casteljau_recursive(new_points, t)

def bezier_casteljau(points, num_samples=100):
    """ Gera pontos da curva Bézier usando o algoritmo de Casteljau. """
    return np.array([casteljau_recursive(points, t) for t in np.linspace(0, 1, num_samples)])

def animate_bezier_casteljau(P, ax, title):
    """ Animação da curva Bézier usando o algoritmo de Casteljau. """
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 110)
    ax.set_title(title)
    
    control_line, = ax.plot(P[:, 0], P[:, 1], 'bo--', label="Pontos de Controle")
    curve_line, = ax.plot([], [], 'r-', lw=2, label="Curva Bézier")
    
    def init():
        curve_line.set_data([], [])
        return curve_line,
    
    def update(frame):
        t_values = np.linspace(0, frame / 100, frame)
        bezier_points = np.array([casteljau_recursive(P, t) for t in t_values])
        if len(bezier_points) > 1:
            curve_line.set_data(bezier_points[:, 0], bezier_points[:, 1])
        return curve_line,
    
    ani = animation.FuncAnimation(fig, update, frames=101, init_func=init, blit=True, interval=30)
    return ani

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Definição das curvas
P_quadratica = np.array([[10, 10], [80, 80], [100, 20]])  # Grau 2
P_cubica = np.array([[10, 10], [40, 60], [60, 60], [90, 10]])  # Grau 3
P_n_esima = np.array([[10, 10], [20, 80], [50, 100], [80, 80], [100, 40]])  # Grau N

# Criando animações
ani1 = animate_bezier_casteljau(P_quadratica, axes[0], "Curva Quadrática (Grau 2)")
ani2 = animate_bezier_casteljau(P_cubica, axes[1], "Curva Cúbica (Grau 3)")
ani3 = animate_bezier_casteljau(P_n_esima, axes[2], "Curva de Grau N")

plt.legend()
plt.show()
