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
    print(query_path)
    Q_dict = modules.auxiliar_functions.create_query(query_path)
    Q = list(Q_dict.values())[0]
    all_references = all_deblas[i+1:len(all_deblas)]
    areas = modules.auxiliar_functions.compare_query_against_referencesarray(
        Q, all_references)
    all_areas.append(areas)


distance_matrix = np.zeros((len(all_deblas), len(all_deblas)))

for i in range(len(all_areas)):
    values = list(all_areas[i].values())
    for j in range(len(values)):
        distance_matrix[i][len(all_deblas) - j - 1] = values[len(values)-j-1]
        distance_matrix[len(all_deblas) - j - 1][i] = values[len(values)-j-1]

for row in distance_matrix:
    for value in range(len(row)):
        if value == len(row)-1:
            print(row[value])
        else:
            print(row[value], end=',')
    # print('\n')

# G = nx.from_numpy_matrix(distance_matrix)
# nx.draw(G)
# plt.show()


# G = nx.relabel_nodes(
#     G, dict(zip(range(len(G.nodes())), string.ascii_uppercase)))

# G = nx.drawing.nx_agraph.to_agraph(G)

# # G.node_attr.update(color="red", style="filled")
# G.edge_attr.update(color="blue", width="1.0")

# G.draw('/tmp/out.png', format='png', prog='neato')
