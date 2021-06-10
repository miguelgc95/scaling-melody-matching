# The purpose of this file is to compare deblas and clasify deblas between the 2 schools Tomas Pabon and Juan de Mairena
import auxiliar_functions
import area_inicial
import calculoeventos
import actualizacionarea
import dataframe
import pandas as pd
import os

BASE_PATH = os.getcwd()
pabon_query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'

pabon_query = pd.read_csv(pabon_query_path, names=["inicio", "duración",
                                                   "tono", "nidea"]).drop([0], axis=0)

time_where_pabon_starts = float(pabon_query.iloc[0, 0])

# cambiar formato de string a float y desplazar la cancion para forzar que empiece en cero
for i in range(len(pabon_query)):
    if type(pabon_query.iloc[i, 0]) == str:
        pabon_query.iloc[i, 0] = float(pabon_query.iloc[i, 0])
    if type(pabon_query.iloc[i, 1]) == str:
        pabon_query.iloc[i, 1] = float(pabon_query.iloc[i, 1])
    if type(pabon_query.iloc[i, 2]) == str:
        pabon_query.iloc[i, 2] = float(pabon_query.iloc[i, 2])
    pabon_query.iloc[i, 0] = (pabon_query.iloc[i, 0]-time_where_pabon_starts)

Q_pabon = auxiliar_functions.prepare_melody(pabon_query)
# cargamos en una lista cada una de las canciones de la base de datos
all_references = dataframe.dframe('exclude_pabon&mairena')

result = []
contInDB = 0
for i in range(len(all_references)):  # recorremos cada canción del dataframe
    contInDB = contInDB + 1
    switch_R_and_Q = False
    # en cada iteración va a ir cambiando la referencia
    R = auxiliar_functions.prepare_melody(all_references[i])

    if Q_pabon[-1][1] > R[-1][1]:  # en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
        P = Q_pabon[:]
        Q_pabon = R[:]
        R = P[:]
        switch_R_and_Q = True

    maxeps = (R[-1][1]-Q_pabon[-1][1])/len(Q_pabon)
    Q_pabon[-1][1] = R[-1][1]
    (areainicial, h11, h22, h33) = area_inicial.initial_area(R, Q_pabon)
    q = calculoeventos.calculaeventos_main(R, Q_pabon, maxeps)

    areas = auxiliar_functions.comprueba_area(R, Q_pabon, q)

    if switch_R_and_Q:  # en caso de haber machacado el valor de Q necesitamos recuperarlo
        Q_pabon = P[:]

    print('nueva referencia:\n')
    print(f'area minima para i = {i}: {min(areas)}\n')
