# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules
import os
import operator

BASE_PATH = os.getcwd()

pabon_query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'

Q_pabon_dict = modules.auxiliar_functions.create_query(pabon_query_path)
Q_pabon = list(Q_pabon_dict.values())[0]

# cargamos en una lista cada una de las canciones de la base de datos
all_references = modules.dataframe.dframe('exclude_pabon&mairena')


areas = modules.auxiliar_functions.areainicial_vs_areamin(
    Q_pabon, all_references)

for key, value in areas.items():
    print(f'{key[23:-4]} {value[0]} - {value[1]} = {value[0] - value[1]}')

print(569.7960850100035 - 569.778013)
