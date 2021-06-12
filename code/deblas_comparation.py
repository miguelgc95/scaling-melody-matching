# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules
import os

BASE_PATH = os.getcwd()

pabon_query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'
# mairena_query_path = BASE_PATH + '/DB_files/deblas/14-D_AMairena.csv'

Q_pabon = modules.auxiliar_functions.create_query(pabon_query_path)

# cargamos en una lista cada una de las canciones de la base de datos
all_references = modules.dataframe.dframe('exclude_pabon&mairena')

pabon_areas = modules.auxiliar_functions.compare_query_against_referencesarray(
    Q_pabon, all_references)
print(pabon_areas)
