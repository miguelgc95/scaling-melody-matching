import networkx as nx
import numpy as np
import string
import matplotlib.pyplot as plt

nodes_names = ['a', 'b', 'c', 'd']

distance_matrix = np.array([(0, 2, 1, 9),
                            (2, 0, 1, 9),
                            (1, 1, 0, 9),
                            (9, 9, 9, 0)
                            ])

G = nx.Graph()

G.add_nodes_from(nodes_names)

for i in range(len(nodes_names)):
    for j in range(len(nodes_names)):
        G.add_edge(nodes_names[i], nodes_names[j],
                   weight=distance_matrix[i][j])

G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())), nodes_names)))
print(G)

print(list(G.nodes))
print(list(G.edges.data()))

nx.draw_spring(G, with_labels=True, node_color='red')
# nx.draw_spectral(G)
# nx.draw_networkx_nodes(G, node_color='red')

plt.show()

# G = nx.from_numpy_matrix(A, parallel_edges=False, create_using=temp)

# G = nx.from_numpy_matrix(A)

# G = nx.relabel_nodes(
#     G, dict(zip(range(len(G.nodes())), ['q', 'w', 'srtyjdsr', 'e'])))


# G = nx.drawing.nx_agraph.to_agraph(G)

# nx.draw(G, with_labels=True)
# nx.draw_networkx_nodes(G, pos, node_color="black")
# # nx.draw(G, with_labels=True, node_color='red')
