import matplotlib.pyplot as plt
import numpy as np
import math

def draw_circle_parametric(xc, yc, r):
    points = []
    step = 1 / r  # Define o incremento para suavidade
    t = 0
    while t <= 2 * math.pi:
        x = round(xc + r * math.cos(t))
        y = round(yc + r * math.sin(t))
        points.append((x, y))
        t += step
    return points

def plot_circle_with_ideal_curve(points, xc, yc, r, title="Rasterização de Circunferência - Paramétrica"):
    # Determinar o tamanho da grade
    max_x = max(x for x, y in points) + 1
    max_y = max(y for x, y in points) + 1

    # Criar a matriz de pixels
    grid = np.zeros((max_y, max_x))
    for x, y in points:
        grid[y][x] = 1  # Ativar o pixel correspondente

    # Plotar os pixels com ajustes no `extent`
    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap="Greys", origin="lower", extent=[-0.5, max_x-0.5, -0.5, max_y-0.5])

    # Plotar a curva ideal
    t = np.linspace(0, 2 * np.pi, 1000)
    x_ideal = xc + r * np.cos(t)
    y_ideal = yc + r * np.sin(t)
    plt.plot(x_ideal, y_ideal, color="blue", label="Curva Ideal")

    # Ajustar o gráfico
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xticks(np.arange(0, max_x, 1))
    plt.yticks(np.arange(0, max_y, 1))
    plt.gca().set_xticks(np.arange(-0.5, max_x, 1), minor=True)
    plt.gca().set_yticks(np.arange(-0.5, max_y, 1), minor=True)
    plt.grid(which="minor", color="black", linestyle="-", linewidth=0.5)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    xc, yc = 50, 50  # Centro da circunferência
    r = 50  # Raio
    points = draw_circle_parametric(xc, yc, r)
    print("Pontos gerados (Paramétrico):", points)
    plot_circle_with_ideal_curve(points, xc, yc, r)
