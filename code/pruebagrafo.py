import networkx as nx
import numpy as np
import string
import matplotlib.pyplot as plt

dt = [('len', float)]
A = np.array([(0, 3, 4, 7),
              (3, 0, 9, 2),
              (4, 9, 0, 1),
              (7, 2, 1, 0)
              ])*10
A = A.view(dt)

G = nx.from_numpy_matrix(A)

# G = nx.relabel_nodes(
#     G, dict(zip(range(len(G.nodes())), string.ascii_uppercase)))

# G = nx.drawing.nx_agraph.to_agraph(G)

# G.node_attr.update(color="red", weight=4, style="filled")
# G.edge_attr.update(color="blue", width=".5")

# G.draw('/tmp/out.png', format='png', prog='neato')


# print("node degree clustering")
# for v in nx.nodes(G):
#     print(f"{v} {nx.degree(G, v)} {nx.clustering(G, v)}")

# print()
# print("the adjacency list")
# for line in nx.generate_adjlist(G):
#     print(line)

# nx.draw(G)
# plt.show()

nx.draw(G)
plt.show()
