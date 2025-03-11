import numpy as np
import matplotlib.pyplot as plt

def PMCurva(P0, P1, P2, P3):
    """
    Calcula os pontos intermediários da curva de Bézier usando o método de De Casteljau.
    Retorna os novos pontos para subdivisão.
    """
    # Primeira subdivisão
    P0xN1 = (P0 + P1) / 2
    P1xN1 = (P1 + P2) / 2
    P2xN1 = (P2 + P3) / 2
    
    # Segunda subdivisão
    P0xN2 = (P0xN1 + P1xN1) / 2
    P1xN2 = (P1xN1 + P2xN1) / 2
    
    # Terceira subdivisão (ponto na curva)
    P0xN3 = (P0xN2 + P1xN2) / 2
    
    return P0xN1, P1xN1, P2xN1, P0xN2, P1xN2, P0xN3

def casteljau_recursive(P0, P1, P2, P3, t, curve_points):
    """
    Algoritmo de De Casteljau recursivo para calcular pontos da curva de Bézier.
    """
    if t > 0.005:
        e = t / 2
        P0xN1, P1xN1, P2xN1, P0xN2, P1xN2, P0xN3 = PMCurva(P0, P1, P2, P3)
        casteljau_recursive(P0, P0xN1, P0xN2, P0xN3, e, curve_points)
        casteljau_recursive(P0xN3, P1xN2, P2xN1, P3, e, curve_points)
    else:
        curve_points.append(P0)

# Definir os pontos de controle
P0 = np.array([0, 0])
P1 = np.array([2, 4])
P2 = np.array([6, 4])
P3 = np.array([8, 0])

# Criar a curva de Bézier
t_values = np.linspace(0, 1, 100)
bezier_curve = []
casteljau_recursive(P0, P1, P2, P3, 1, bezier_curve)
bezier_curve = np.array(bezier_curve)

# Criar a figura
fig, ax = plt.subplots()
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 10)
ax.set_title("Curva de Bézier - Algoritmo de Casteljau Recursivo")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Plotar os pontos de controle
control_points = [P0, P1, P2, P3]
ax.plot([p[0] for p in control_points], [p[1] for p in control_points], 'ro--', label="Pontos de Controle")

# Plotar a curva de Bézier
if len(bezier_curve) > 0:
    ax.plot(bezier_curve[:, 0], bezier_curve[:, 1], 'b-', lw=2, label="Curva de Bézier")

plt.legend()
plt.show()