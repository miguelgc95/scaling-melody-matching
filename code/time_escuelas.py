import modules
import os
import operator
import time

BASE_PATH = os.getcwd()

pabon_query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'
mairena_query_path = BASE_PATH + '/DB_files/deblas/01-D_AMairena.csv'

Q_pabon = modules.auxiliar_functions.create_query(pabon_query_path)
Q_mairena = modules.auxiliar_functions.create_query(mairena_query_path)

# cargamos en una lista cada una de las canciones de la base de datos
all_references = modules.dataframe.dframe('exclude_pabon&mairena')

start_time_eficient = time.time()
pabon_areas_eficient = modules.auxiliar_functions.eficient_compare_query_against_referencesarray(
    Q_pabon, all_references)
mairena_areas_eficient = modules.auxiliar_functions.eficient_compare_query_against_referencesarray(
    Q_mairena, all_references)

end_time_eficient = time.time()

print('Time for eficient algorith:', end_time_eficient - start_time_eficient)


start_time_non_eficient = time.time()

pabon_areas_no_eficient = modules.auxiliar_functions.compare_query_against_referencesarray(
    Q_pabon, all_references)

mairena_areas_no_eficient = modules.auxiliar_functions.compare_query_against_referencesarray(
    Q_mairena, all_references)

end_time_non_eficient = time.time()

print('Time for non eficient algorith:',
      end_time_non_eficient - start_time_non_eficient)
