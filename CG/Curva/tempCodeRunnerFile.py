import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def casteljau_iterativo(points, t):
    points = np.array(points)
    subdivisoes = [points]

    while len(points) > 1:
        points = np.array([(1 - t) * points[i] + t * points[i + 1] 
                           for i in range(len(points) - 1)])
        subdivisoes.append(points)

    return subdivisoes

def animate_casteljau(P, ax, title):
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 110)
    ax.set_title(title)

    linhas = []
    pontos, = ax.plot([], [], 'ro')

    def init():
        pontos.set_data([], [])
        return pontos,

    def update(frame):
        t = frame / 100
        subdivisoes = casteljau_iterativo(P, t)

        # limpar linhas anteriores
        for ln in linhas:
            ln.remove()
        linhas.clear()

        # desenha subdivisões intermediárias
        for sub in subdivisoes[:-1]:
            ln, = ax.plot(sub[:,0], sub[:,1], 'o--', color='gray', alpha=0.5)
            linhas.append(ln)

        ponto_final = subdivisoes[-1][0]
        pontos.set_data(ponto_final[0], ponto_final[1])

        return linhas + [pontos]

    ani = animation.FuncAnimation(fig, update, frames=101, init_func=init,
                                  blit=True, interval=50, repeat=True)
    return ani

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Pontos de controle
P_quadratica = np.array([[10, 10], [80, 80], [100, 20]])
P_cubica = np.array([[10, 10], [40, 60], [60, 60], [90, 10]])
P_n = np.array([[10, 10], [20, 80], [50, 100], [80, 80], [100, 40]])

# Animações
ani1 = animate_casteljau(P_quadratica, axes[0], "Quadrática")
ani2 = animate_casteljau(P_cubica, axes[1], "Cúbica")
ani3 = animate_casteljau(P_n, axes[2], "Grau N")

plt.tight_layout()
plt.show()
