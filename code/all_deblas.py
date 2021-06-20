# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules
import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import string

BASE_PATH = os.getcwd()

all_deblas = modules.dataframe.dframe('none_deblas')

all_areas = []

for i in range(len(all_deblas)):
    query_path = all_deblas[i].columns.values[3]
    Q = modules.auxiliar_functions.create_query(query_path)
    all_references = all_deblas[i+1:len(all_deblas)]
    areas = modules.auxiliar_functions.compare_query_against_referencesarray(
        Q, all_references)
    all_areas.append(areas)

print('allareas', len(all_areas))


distance_matrix = np.zeros((len(all_deblas), len(all_deblas)))


for i in range(len(all_areas)):
    values = list(all_areas[i].values())
    for j in range(len(values)):
        distance_matrix[i][len(all_deblas) - j - 1] = values[len(values)-j-1]
        distance_matrix[len(all_deblas) - j - 1][i] = values[len(values)-j-1]


G = nx.from_numpy_matrix(distance_matrix)
nx.draw(G)
plt.show()
# G = nx.relabel_nodes(
#     G, dict(zip(range(len(G.nodes())), string.ascii_uppercase)))

# G = nx.drawing.nx_agraph.to_agraph(G)

# # G.node_attr.update(color="red", style="filled")
# G.edge_attr.update(color="blue", width="1.0")

# G.draw('/tmp/out.png', format='png', prog='neato')
