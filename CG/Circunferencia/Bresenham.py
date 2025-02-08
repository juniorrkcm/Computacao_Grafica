import matplotlib.pyplot as plt
import numpy as np

def draw_circle_bresenham(xc, yc, r):
    points = []
    x = 0
    y = r
    d = 3 - 2 * r  # Decisão inicial

    while x <= y:
        # Adiciona os pontos de todos os octantes usando simetria
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ])
        
        # Atualiza a decisão
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

def plot_circle_with_ideal_curve(points, xc, yc, r, title="Rasterização de Circunferência - Bresenham"):
    # Determinar o tamanho da grade
    max_x = max(max(x for x, y in points), xc + r) + 1
    max_y = max(max(y for x, y in points), yc + r) + 1

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
    points = draw_circle_bresenham(xc, yc, r)
    print("Pontos gerados (Bresenham):", points)
    plot_circle_with_ideal_curve(points, xc, yc, r)
