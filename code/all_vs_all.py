# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules
import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import string

BASE_PATH = os.getcwd()

all_deblas = modules.dataframe.dframe('none_deblas')

all_martinetes = modules.dataframe.dframe('none_martinetes')

all_database = all_deblas + all_martinetes

all_areas = []

for i in range(len(all_database)):
    query_path = all_database[i].columns.values[3]
    print(query_path)
    Q_dict = modules.auxiliar_functions.create_query(query_path)
    Q = list(Q_dict.values())[0]
    all_references = all_database[i+1:len(all_database)]
    areas = modules.auxiliar_functions.compare_query_against_referencesarray(
        Q, all_references)
    print('areas', areas.values())
    if i < len(all_deblas) and areas.values() > 100:
        all_areas.append(areas.values())

    all_areas.append(areas)

distance_matrix = np.zeros((len(all_database), len(all_database)))

for i in range(len(all_areas)):
    values = list(all_areas[i].values())
    for j in range(len(values)):
        distance_matrix[i][len(all_database) - j - 1] = values[len(values)-j-1]
        distance_matrix[len(all_database) - j - 1][i] = values[len(values)-j-1]

for row in distance_matrix:
    for value in range(len(row)):
        if value == len(row)-1:
            print(row[value])
        else:
            print(row[value], end=',')


# G = nx.from_numpy_matrix(distance_matrix)
# color_map = []
# for node in G:
#     if node < len(all_deblas):
#         color_map.append('blue')
#     else:
#         color_map.append('red')
# nx.draw(G, node_color=color_map, with_labels=True)
# plt.show()
