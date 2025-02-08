import matplotlib.pyplot as plt
import numpy as np

def draw_line_analytical(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx
    b = y1 - m * x1
    
    points = []
    x = x1
    while x <= x2:
        y = round(m * x + b)
        points.append((x, y))
        x += 1
    return points

def plot_pixels_with_ideal_line(points, x1, y1, x2, y2, title="Reta - Método Analitico"):
    # Determinar o tamanho da grade
    max_x = max(max(x for x, y in points), x2) + 1
    max_y = max(max(y for x, y in points), y2) + 1

    # Criar a matriz de pixels
    grid = np.zeros((max_y, max_x))
    for x, y in points:
        grid[y][x] = 1  # Ativar o pixel correspondente

    # Plotar os pixels com ajustes no `extent`
    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap="Greys", origin="lower", extent=[-0.5, max_x-0.5, -0.5, max_y-0.5])

    # Plotar a linha ideal
    x_ideal = np.linspace(x1, x2, 1000)
    y_ideal = y1 + (y2 - y1) * (x_ideal - x1) / (x2 - x1)  # Fórmula da reta
    plt.plot(x_ideal, y_ideal, color="blue", label="Reta Ideal")

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
    x1, y1 = 0, 0
    x2, y2 = 10, 20
    points = draw_line_analytical(x1, y1, x2, y2)
    print("Pontos gerados (Analítico):", points)
    plot_pixels_with_ideal_line(points, x1, y1, x2, y2)
