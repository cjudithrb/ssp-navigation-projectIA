import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos al grafo
nodes = range(1, 42)
G.add_nodes_from(nodes)

# Añadir aristas al grafo
edges = [
(1, 1),
(1, 5),
(1, 2),
(2, 41),
(2, 2),
(2, 6),
(2, 3),
(2, 1),
(3, 41),
(3, 3),
(3, 7),
(3, 4),
(3, 2),
(4, 4),
(4, 8),
(4, 3),
(5, 5),
(5, 6),
(5, 1),
(5, 9),
(8, 8),
(8, 7),
(8, 4),
(8, 12),
(9, 9),
(9, 10),
(9, 5),
(9, 13),
(12, 12),
(12, 11),
(12, 8),
(12, 16),
(13, 13),
(13, 14),
(13, 9),
(13, 17),
(16, 16),
(16, 15),
(16, 12),
(16, 20),
(17, 17),
(17, 18),
(17, 13),
(17, 21),
(20, 20),
(20, 19),
(20, 16),
(20, 24),
(21, 21),
(21, 22),
(21, 17),
(21, 25),
(24, 24),
(24, 23),
(24, 20),
(24, 28),
(25, 25),
(25, 26),
(25, 21),
(25, 29),
(28, 28),
(28, 27),
(28, 24),
(28, 32),
(29, 29),
(29, 30),
(29, 25),
(29, 33),
(32, 32),
(32, 31),
(32, 28),
(32, 36),
(33, 33),
(33, 34),
(33, 29),
(33, 37),
(36, 36),
(36, 35),
(36, 32),
(36, 40),
(40, 40),
(6, 10),
(6, 2),
(6, 7),
(6, 5),
(6, 41),
(7, 11),
(7, 3),
(7, 8),
(7, 6),
(7, 41),
(10, 14),
(10, 6),
(10, 11),
(10, 9),
(10, 41),
(11, 15),
(11, 7),
(11, 12),
(11, 10),
(11, 41),
(14, 18),
(14, 10),
(14, 15),
(14, 13),
(14, 41),
(15, 19),
(15, 11),
(15, 16),
(15, 14),
(15, 41),
(18, 22),
(18, 14),
(18, 19),
(18, 17),
(18, 41),
(19, 23),
(19, 15),
(19, 20),
(19, 18),
(19, 41),
(22, 26),
(22, 18),
(22, 23),
(22, 21),
(22, 41),
(23, 27),
(23, 19),
(23, 24),
(23, 22),
(23, 41),
(26, 30),
(26, 22),
(26, 27),
(26, 25),
(26, 41),
(27, 31),
(27, 23),
(27, 28),
(27, 26),
(27, 41),
(30, 34),
(30, 26),
(30, 31),
(30, 29),
(30, 41),
(31, 35),
(31, 27),
(31, 32),
(31, 30),
(31, 41),
(34, 38),
(34, 30),
(34, 35),
(34, 33),
(34, 41),
(35, 39),
(35, 31),
(35, 36),
(35, 34),
(35, 41),
(37, 37),
(37, 33),
(37, 38),
(38, 41),
(38, 38),
(38, 34),
(38, 39),
(38, 37),
(39, 41),
(39, 39),
(39, 35),
(39, 40),
(39, 38),
(41, 41)
]

G.add_edges_from(edges)

# Definir las posiciones de los nodos en un diseño de columnas
pos = {}
for i in range(1, 42):
        col = (i - 1) % 4
        row = (i - 1) // 4
        pos[i] = (col, -row)

# Dibujar el grafo
plt.figure(figsize=(15, 10))
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='black', edgecolors='black', linewidths=0)
nx.draw_networkx_labels(G, pos, font_size=12, font_color='white')
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15, edge_color='black')

# Mejorar el diseño visual
plt.title("Graph Problem Navegation - navigator4-10-0-0.json", fontsize=16)
plt.axis('off')  # Ocultar los ejes

# Mostrar la gráfica
plt.show()
