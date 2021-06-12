# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena

import modules

import os

BASE_PATH = os.getcwd()

pabon_query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'
# mairena_query_path = BASE_PATH + '/DB_files/deblas/14-D_AMairena.csv'

Q_pabon = modules.auxiliar_functions.create_query(pabon_query_path)

# cargamos en una lista cada una de las canciones de la base de datos
all_references = modules.dataframe.dframe('exclude_pabon&mairena')

result = []
contInDB = 0
for i in range(len(all_references)):  # recorremos cada canción del dataframe
    contInDB = contInDB + 1
    switch_R_and_Q = False
    # en cada iteración va a ir cambiando la referencia
    R = modules.auxiliar_functions.prepare_melody(all_references[i])

    if Q_pabon[-1][1] > R[-1][1]:  # en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
        P = Q_pabon[:]
        Q_pabon = R[:]
        R = P[:]
        switch_R_and_Q = True

    maxeps = (R[-1][1]-Q_pabon[-1][1])/len(Q_pabon)
    Q_pabon[-1][1] = R[-1][1]
    (areainicial, h11, h22, h33) = modules.area_inicial.initial_area(R, Q_pabon)
    # (areainicial, h11, h22, h33) = initial_area(R, Q_pabon)
    q = modules.calculoeventos.calculaeventos_main(R, Q_pabon, maxeps)

    areas = modules.auxiliar_functions.comprueba_area(R, Q_pabon, q)

    if switch_R_and_Q:  # en caso de haber machacado el valor de Q necesitamos recuperarlo
        Q_pabon = P[:]

    print('nueva referencia:\n')
    print(f'area minima para i = {i}: {min(areas)}\n')
