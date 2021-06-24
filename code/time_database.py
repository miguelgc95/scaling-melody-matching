# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules
import os
import time

BASE_PATH = os.getcwd()

all_deblas = modules.dataframe.dframe('none_deblas')
all_martinetes = modules.dataframe.dframe('none_martinetes')

all_database = all_deblas + all_martinetes

all_areas = []

start_time_eficient = time.time()
for i in range(len(all_database)):
    query_path = all_database[i].columns.values[3]
    Q = modules.auxiliar_functions.create_query(query_path)
    all_references = all_database[i+1:len(all_database)]
    areas = modules.auxiliar_functions.eficient_compare_query_against_referencesarray(
        Q, all_references)
    all_areas.append(areas)

end_time_eficient = time.time()
print('Time for eficient algorith:', end_time_eficient - start_time_eficient)

all_areas = []

start_time_non_eficient = time.time()
for i in range(len(all_database)):
    query_path = all_database[i].columns.values[3]
    Q = modules.auxiliar_functions.create_query(query_path)
    all_references = all_database[i+1:len(all_database)]
    areas = modules.auxiliar_functions.compare_query_against_referencesarray(
        Q, all_references)
    all_areas.append(areas)
    end_time_non_eficient = time.time()

print('Time for non eficient algorith:',
      end_time_non_eficient - start_time_non_eficient)
