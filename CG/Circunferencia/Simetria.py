import matplotlib.pyplot as plt
import numpy as np
import math

def draw_circle_incremental_corrected(xc, yc, r):
    points = []
    
    # Inicializando variáveis conforme o método incremental correto
    x = r
    y = 0
    theta = 1 / r  # Incremento angular
    C = math.cos(theta)
    S = math.sin(theta)

    # Adiciona os primeiros pontos com simetria
    points.extend([
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ])

    while y < x:
        xt = x  # Armazena x temporariamente
        x = x * C - y * S  # Atualização incremental de x
        y = y * C + xt * S  # Atualização incremental de y

        # Arredonda para garantir a rasterização correta
        x_discreto = round(x)
        y_discreto = round(y)

        # Adiciona os pontos usando simetria
        points.extend([
            (xc + x_discreto, yc + y_discreto), (xc - x_discreto, yc + y_discreto),
            (xc + x_discreto, yc - y_discreto), (xc - x_discreto, yc - y_discreto),
            (xc + y_discreto, yc + x_discreto), (xc - y_discreto, yc + x_discreto),
            (xc + y_discreto, yc - x_discreto), (xc - y_discreto, yc - x_discreto)
        ])

    return points

def plot_circle_with_ideal_curve(points, xc, yc, r, title="Rasterização de Circunferência - Incremental com Simetria (Corrigido)"):
    max_x = max(max(x for x, y in points), xc + r) + 1
    max_y = max(max(y for x, y in points), yc + r) + 1

    grid = np.zeros((max_y, max_x))
    for x, y in points:
        if 0 <= y < grid.shape[0] and 0 <= x < grid.shape[1]:
            grid[y][x] = 1

    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap="Greys", origin="lower", extent=[-0.5, max_x-0.5, -0.5, max_y-0.5])

    # Plotar a curva ideal
    t = np.linspace(0, 2 * np.pi, 1000)
    x_ideal = xc + r * np.cos(t)
    y_ideal = yc + r * np.sin(t)
    plt.plot(x_ideal, y_ideal, color="blue", label="Curva Ideal")

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
    xc, yc = 10, 10  
    r = 3
    points = draw_circle_incremental_corrected(xc, yc, r)
    print("Pontos gerados (Incremental com Simetria Corrigido):", points)
    plot_circle_with_ideal_curve(points, xc, yc, r)
