# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules
import os

BASE_PATH = os.getcwd()

all_deblas = modules.dataframe.dframe('all_deblas')

all_areas = []

for i in range(len(all_deblas)-2):
    query_path = all_deblas[i].columns.values[3]
    Q = modules.auxiliar_functions.create_query(query_path)
    all_references = all_deblas[i+1:len(all_deblas)-1]
    areas = modules.auxiliar_functions.compare_query_against_referencesarray(
        Q, all_references)
    all_areas.append(areas)

for areas in all_areas:
    print('lenth: ', len(areas))
    print('areas', areas)
    print('\n')
