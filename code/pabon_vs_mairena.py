# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules
import os
import operator

BASE_PATH = os.getcwd()

pabon_query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'
mairena_query_path = BASE_PATH + '/DB_files/deblas/01-D_AMairena.csv'

Q_pabon = modules.auxiliar_functions.create_query(pabon_query_path)
Q_mairena = modules.auxiliar_functions.create_query(mairena_query_path)

# cargamos en una lista cada una de las canciones de la base de datos
all_references = modules.dataframe.dframe('exclude_pabon&mairena')

pabon_areas = modules.auxiliar_functions.compare_query_against_referencesarray(
    Q_pabon, all_references)

pabon_areas_sorted = sorted(pabon_areas.items(), key=operator.itemgetter(1))
print('pabon_areas_sorted', pabon_areas_sorted)
print('\n')

mairena_areas = modules.auxiliar_functions.compare_query_against_referencesarray(
    Q_mairena, all_references)
mairena_areas_sorted = sorted(
    mairena_areas.items(), key=operator.itemgetter(1))
print('mairena_areas_sorted', mairena_areas_sorted)
print('\n')

similiar_to_pabon = []
similiar_to_mairena = []
same_similarity = []

# da igual coger similiar_to_pabon que mairena_areas porque tienes las mismas keys
for name in pabon_areas.keys():
    if pabon_areas[name] < mairena_areas[name]:
        similiar_to_pabon.append(name)
    elif pabon_areas[name] > mairena_areas[name]:
        similiar_to_mairena.append(name)
    elif pabon_areas[name] == mairena_areas[name]:
        same_similarity.append(name)

print('similiar_to_pabon', similiar_to_pabon)
print('\n')
print('similiar_to_mairena', similiar_to_mairena)
print('\n')
print('same_similarity', same_similarity)
