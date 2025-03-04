import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.special import comb  # Para calcular coeficientes binomiais

def bernstein(n, i, t):
    """ Calcula o polinômio de Bernstein B_i^n (t) """
    return comb(n, i) * (t ** i) * ((1 - t) ** (n - i))

def bezier_generalized(t, P):
    """ Calcula pontos da curva Bézier de grau n usando a equação paramétrica """
    n = len(P) - 1  # Grau da curva (n = número de pontos - 1)
    B = np.zeros(2)  # Inicializa coordenadas X e Y
    
    for i in range(n + 1):  # Para cada ponto de controle
        B += bernstein(n, i, t) * P[i]  # Soma as contribuições dos Bernstein
    
    return B

def animate_bezier(P, ax, title):
    """ Animação da curva Bézier de grau arbitrário usando a equação paramétrica """
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
        bezier_points = np.array([bezier_generalized(t, P) for t in t_values])
        if len(bezier_points) > 1:
            curve_line.set_data(bezier_points[:, 0], bezier_points[:, 1])
        return curve_line,
    
    ani = animation.FuncAnimation(fig, update, frames=101, init_func=init, blit=True, interval=30)
    return ani

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Definição das curvas
P_quadratica = np.array([[10, 10], [60, 90], [100, 20]])  # Grau 2
P_cubica = np.array([[10, 10], [30, 40], [70, 80], [90, 10]])  # Grau 3
P_n_esima = np.array([[10, 10], [20, 80], [50, 100], [80, 60], [120, 90]])  # Grau N

# Criando animações
ani1 = animate_bezier(P_quadratica, axes[0], "Curva Quadrática (Grau 2)")
ani2 = animate_bezier(P_cubica, axes[1], "Curva Cúbica (Grau 3)")
ani3 = animate_bezier(P_n_esima, axes[2], "Curva de Grau N")

plt.legend()
plt.show()
