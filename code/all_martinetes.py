# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules
import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import string

BASE_PATH = os.getcwd()

all_martinetes = modules.dataframe.dframe('none_martinetes')

all_areas = []

for i in range(len(all_martinetes)):
    query_path = all_martinetes[i].columns.values[3]
    Q = modules.auxiliar_functions.create_query(query_path)
    all_references = all_martinetes[i+1:len(all_martinetes)]
    areas = modules.auxiliar_functions.compare_query_against_referencesarray(
        Q, all_references)
    all_areas.append(areas)


distance_matrix = np.zeros((len(all_martinetes), len(all_martinetes)))

for i in range(len(all_areas)):
    values = list(all_areas[i].values())
    for j in range(len(values)):
        distance_matrix[i][len(all_martinetes) - j -
                           1] = values[len(values)-j-1]
        distance_matrix[len(all_martinetes) - j -
                        1][i] = values[len(values)-j-1]


print(distance_matrix)

G = nx.from_numpy_matrix(distance_matrix)
G.nodes
nx.draw(G)
plt.show()
