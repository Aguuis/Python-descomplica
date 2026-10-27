#Código da molécula de Dióxido de carbono

import networkx as nx

import matplotlib.pyplot as plt

# Criação do grafo

G = nx.Graph()

# Adição dos vértices

G.add_node('C')  # Átomo de carbono

G.add_nodes_from(['O1', 'O2'])  # Átomos de oxigênio

# Adição das arestas

G.add_edges_from([('C', 'O1'), ('C', 'O2')])

# Visualização do grafo

plt.figure(figsize=(5,5))

nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_size=16)

plt.suptitle("Representação da Molécula de Dióxido de carbono (CO₂) com Grafos")

plt.show()