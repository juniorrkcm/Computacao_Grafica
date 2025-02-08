import matplotlib.pyplot as plt
import numpy as np

def draw_line_bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    
    err = dx - dy
    points = []
    
    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    
    return points

def plot_pixels_with_ideal_line(points, x1, y1, x2, y2, title="Reta - Método Bresenham"):
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
    points = draw_line_bresenham(x1, y1, x2, y2)
    print("Pontos gerados (Bresenham):", points)
    plot_pixels_with_ideal_line(points, x1, y1, x2, y2)
