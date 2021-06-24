import modules
import os
import time

BASE_PATH = os.getcwd()

all_martinetes = modules.dataframe.dframe('none_martinetes')

all_areas = []

start_time_eficient = time.time()

for i in range(len(all_martinetes)):
    query_path = all_martinetes[i].columns.values[3]
    Q = modules.auxiliar_functions.create_query(query_path)
    all_references = all_martinetes[i+1:len(all_martinetes)]
    areas = modules.auxiliar_functions.eficient_compare_query_against_referencesarray(
        Q, all_references)
    all_areas.append(areas)

end_time_eficient = time.time()
print('Time for eficient algorith:', end_time_eficient - start_time_eficient)


start_time_non_eficient = time.time()

for i in range(len(all_martinetes)):
    query_path = all_martinetes[i].columns.values[3]
    Q = modules.auxiliar_functions.create_query(query_path)
    all_references = all_martinetes[i+1:len(all_martinetes)]
    areas = modules.auxiliar_functions.compare_query_against_referencesarray(
        Q, all_references)
    all_areas.append(areas)

end_time_non_eficient = time.time()

print('Time for non eficient algorith:',
      end_time_non_eficient - start_time_non_eficient)
