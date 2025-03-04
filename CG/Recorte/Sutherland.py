import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definição da janela de recorte
xmin, ymin, xmax, ymax = 100, 100, 400, 400

# Definição dos polígonos
a = [[200, 200], [200, 500], [500, 200]]
b = [[140, 260], [280, 260], [330, 380], [210, 460], [90, 380]]
c = [[150, 100], [150, 150], [200, 150], [200, 200], [300, 200], [300, 150], [350, 150], [350, 100], [350, 50], [300, 50], [300, 0], [200, 0], [200, 50], [150, 50]]
d = [[120, 320], [120, 480], [380, 480], [380, 340], [300, 340], [300, 410], [200, 410], [200, 320]]

# Escolha do polígono a ser desenhado
poligono_escolhido = c  # Modifique para a, b, c ou d

# Aplicar deslocamento apenas ao polígono b
if poligono_escolhido == b:
    deslocamento_x = -100  # Valor do deslocamento para a esquerda
    poligono_escolhido = [[x + deslocamento_x, y] for x, y in poligono_escolhido]

def inside(point, clip_edge):
    x, y = point
    edge_x1, edge_y1, edge_x2, edge_y2 = clip_edge
    # Verifica se o ponto está à esquerda, direita, abaixo ou acima da aresta de recorte
    if edge_x1 == edge_x2:  # Aresta vertical
        return x >= edge_x1 if edge_x1 == xmin else x <= edge_x1
    else:  # Aresta horizontal
        return y >= edge_y1 if edge_y1 == ymin else y <= edge_y1

def intersection(p1, p2, clip_edge):
    x1, y1 = p1
    x2, y2 = p2
    edge_x1, edge_y1, edge_x2, edge_y2 = clip_edge

    if edge_x1 == edge_x2:  # Aresta vertical
        x_int = edge_x1
        m = (y2 - y1) / (x2 - x1) if x2 != x1 else 0
        y_int = y1 + m * (x_int - x1)
    else:  # Aresta horizontal
        y_int = edge_y1
        m = (y2 - y1) / (x2 - x1) if x2 != x1 else 0
        x_int = x1 + (y_int - y1) / m if m != 0 else x1

    return (x_int, y_int)

def clip_polygon(polygon, clip_rect):
    x_min, x_max, y_min, y_max = clip_rect
    clip_edges = [
        (x_min, y_min, x_min, y_max),  # Aresta esquerda
        (x_min, y_max, x_max, y_max),  # Aresta superior
        (x_max, y_max, x_max, y_min),  # Aresta direita
        (x_max, y_min, x_min, y_min)   # Aresta inferior
    ]

    clipped_polygon = polygon[:]
    for clip_edge in clip_edges:
        new_polygon = []
        prev_point = clipped_polygon[-1]
        for curr_point in clipped_polygon:
            if inside(curr_point, clip_edge):
                if not inside(prev_point, clip_edge):
                    intersec = intersection(prev_point, curr_point, clip_edge)
                    new_polygon.append(intersec)
                new_polygon.append(curr_point)
            elif inside(prev_point, clip_edge):
                intersec = intersection(prev_point, curr_point, clip_edge)
                new_polygon.append(intersec)
            prev_point = curr_point
        clipped_polygon = new_polygon

    return clipped_polygon

def update(frame):
    plt.cla()
    plt.xlim(-200, 600)
    plt.ylim(-200, 600)
    plt.gca().set_aspect('equal')
    plt.gca().set_xticks([])
    plt.gca().set_yticks([])
    
    # Desenhar a área de recorte
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'k-', linewidth=2)
    
    if frame == 0:
        # Desenhar apenas o polígono original na primeira etapa
        poligono_x, poligono_y = zip(*poligono_escolhido + [poligono_escolhido[0]])
        plt.plot(poligono_x, poligono_y, 'b-', linewidth=2, label='Original')
    elif frame == 1:
        # Desenhar apenas o polígono recortado na segunda etapa
        clipped = clip_polygon(poligono_escolhido, (xmin, xmax, ymin, ymax))
        if clipped:
            clipped_x, clipped_y = zip(*clipped + [clipped[0]])
            plt.plot(clipped_x, clipped_y, 'r-', linewidth=2, label='Recortado')
    
    plt.legend()

def animate():
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, update, frames=2, interval=1000, repeat=False)
    plt.show()

# Executar animação
animate()