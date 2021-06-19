# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules
import os
import numpy as np

BASE_PATH = os.getcwd()

all_deblas = modules.dataframe.dframe('none_deblas')
all_martinetes = modules.dataframe.dframe('none_martinetes')

all_database = np.append(all_deblas, all_martinetes)

all_areas = []

for i in range(len(all_database)-2):
    query_path = all_database[i].columns.values[3]
    Q = modules.auxiliar_functions.create_query(query_path)
    all_references = all_database[i+1:len(all_database)-1]
    areas = modules.auxiliar_functions.compare_query_against_referencesarray(
        Q, all_references)
    all_areas.append(areas)

for areas in all_areas:
    print('lenth: ', len(areas))
    print('areas', areas)
    print('\n')
