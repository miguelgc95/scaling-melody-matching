# este archivo pretende sustituir al main del programa, ya que tiene la misma funcionalidad. es en realidad una copia de "intentando arreglar base de datos" ampliandola para que no solo compare 2 a 2
import auxiliar_functions
import area_inicial
import calculoeventos
import actualizacionarea
import dataframe
import pandas as pd
import os

BASE_PATH = os.getcwd()
query_path = BASE_PATH + '/DB_files/11-D_TPabon.csv'

query = pd.read_csv(query_path, names=["inicio", "duración",
                                       "tono", "nidea"]).drop([0], axis=0)

time_where_song_starts = float(query.iloc[0, 0])

# cambiar formato de string a float y desplazar la cancion para forzar que empiece en cero
for i in range(len(query)):
    if type(query.iloc[i, 0]) == str:
        query.iloc[i, 0] = float(query.iloc[i, 0])
    if type(query.iloc[i, 1]) == str:
        query.iloc[i, 1] = float(query.iloc[i, 1])
    if type(query.iloc[i, 2]) == str:
        query.iloc[i, 2] = float(query.iloc[i, 2])
    query.iloc[i, 0] = (query.iloc[i, 0]-time_where_song_starts)

Q = auxiliar_functions.prepare_melody(query)
# cargamos en una lista cada una de las canciones de la base de datos
all_references = dataframe.dframe()

result = []
contInDB = 0
for i in range(len(all_references)):  # recorremos cada canción del dataframe
    contInDB = contInDB + 1
    flag = 0
    # en cada iteración va a ir cambiando la referencia
    R = auxiliar_functions.prepare_melody(all_references[i])

    if Q[-1][1] > R[-1][1]:  # en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
        P = Q[:]
        Q = R[:]
        R = P[:]
        flag = 1

    maxeps = (R[-1][1]-Q[-1][1])/len(Q)
    Q[-1][1] = R[-1][1]
    (areainicial, h11, h22, h33) = area_inicial.initial_area(R, Q)
    q = calculoeventos.calculaeventos_main(R, Q, maxeps)
    h = auxiliar_functions.heap(q)
    areamin, epsmin, ayuda = actualizacionarea.actualizar(
        h, q, areainicial, h11, h22, h33, maxeps)
    # guardamos en una lista la info de cada una de las referencias
    result.append([areamin, epsmin])
    # auxiliar_functions.dibuja(R,Q,0)
    areas = auxiliar_functions.comprueba_area(R, Q, q)

    # print('flag', flag)
    if flag == 1:  # como hemos machacado el valor de Q necesitamos recuperarlo
        Q = P[:]

    # if areamin < 0:
    #     print('contInDB', contInDB)
    #     cont = 0
    #     for i, j in zip(areas, ayuda):
    #         cont = cont + 1
    #         # print(i-j[0])
    #         print('cont', cont)
    #         print(f"{i} - {j[0]} = {i-j[0]}")
    #         print(f"evento tipo {j[1]}")
# print(result)
# print(ayuda)
