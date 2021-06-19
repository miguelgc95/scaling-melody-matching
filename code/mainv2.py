# este archivo pretende sustituir a main ya que tiene la misma funcionalidad.
# es en realidad una copia de "intentando arreglar base de datos" ampliandola para que no solo compare 2 a 2
import modules
import pandas as pd
import os

BASE_PATH = os.getcwd()
query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'

Q = modules.auxiliar_functions.create_query(query_path)

# cargamos en una lista cada una de las canciones de la base de datos
all_references = modules.dataframe.dframe('none_deblas')

result = []
contInDB = 0
for i in range(len(all_references)):  # recorremos cada canción del dataframe
    contInDB = contInDB + 1
    flag = 0
    # en cada iteración va a ir cambiando la referencia
    R = modules.auxiliar_functions.prepare_melody(all_references[i])

    if Q[-1][1] > R[-1][1]:  # en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
        P = Q[:]
        Q = R[:]
        R = P[:]
        flag = 1

    maxeps = (R[-1][1]-Q[-1][1])/len(Q)
    Q[-1][1] = R[-1][1]
    (areainicial, h11, h22, h33) = modules.area_inicial.initial_area(R, Q)
    q = modules.calculoeventos.calculaeventos_main(R, Q, maxeps)
    h = modules.auxiliar_functions.heap(q)
    areamin, epsmin, ayuda = modules.actualizacionarea.actualizar(
        h, q, areainicial, h11, h22, h33, maxeps)
    # guardamos en una lista la info de cada una de las referencias
    result.append([areamin, epsmin])
    # auxiliar_functions.dibuja(R,Q,0)
    areas = modules.auxiliar_functions.comprueba_area(R, Q, q)

    # print('flag', flag)
    if flag == 1:  # como hemos machacado el valor de Q necesitamos recuperarlo
        Q = P[:]

    if abs(areas[-1] - ayuda[-1][0]) > 1:
        for i, j in zip(areas, ayuda):
            print(f"{i} - {j[0]} = {i-j[0]}")
            print(f"evento tipo {j[1]}")
