#Código da molécula de água

import networkx as nx

import matplotlib.pyplot as plt

# Criação do grafo

G = nx.Graph()

# Adição dos vértices

G.add_node('O')  # Átomo de oxigênio

G.add_nodes_from(['H1', 'H2'])  # Átomos de hidrogênio

# Adição das arestas

G.add_edges_from([('O', 'H1'), ('O', 'H2')])

# Visualização do grafo
plt.figure(figsize=(5, 5))

nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    edge_color="gray",
    node_size=800,
    font_size=16
)

plt.suptitle("Representação da Molécula de Água (H₂O)", fontsize=12)
plt.show()