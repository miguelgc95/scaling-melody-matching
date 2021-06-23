import networkx as nx
import numpy as np
import string
import matplotlib.pyplot as plt

A = np.array([(0, 2, 1, 9),
              (2, 0, 1, 1),
              (1, 1, 0, 1),
              (9, 1, 1, 0)
              ])

G = nx.from_numpy_matrix(A, parallel_edges=False, create_using=temp)

# G = nx.from_numpy_matrix(A)

# G = nx.relabel_nodes(
#     G, dict(zip(range(len(G.nodes())), ['q', 'w', 'srtyjdsr', 'e'])))


# G = nx.drawing.nx_agraph.to_agraph(G)

nx.draw(G, with_labels=True)
# nx.draw_networkx_nodes(G, pos, node_color="black")
# # nx.draw(G, with_labels=True, node_color='red')
plt.show()
