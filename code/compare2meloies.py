# este archivo pretende sustituir al main del programa, ya que tiene la misma funcionalidad. es en realidad una copia de "intentando arreglar base de datos" ampliandola para que no solo compare 2 a 2
import modules
import pandas as pd
import os

BASE_PATH = os.getcwd()

query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'

Q = modules.auxiliar_functions.create_query(query_path)

reference_path = BASE_PATH + '/DB_files/deblas/01-D_AMairena.csv'

# We can use the function 'create_query' to create the reference as long as it just create a valid melody from a .csv file
R = modules.auxiliar_functions.create_query(reference_path)

# aplicamos el algoritmo

if Q[-1][1] > R[-1][1]:  # en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
    P = Q[:]
    Q = R[:]
    R = P[:]

maxeps = (R[-1][1]-Q[-1][1])/len(Q)
Q[-1][1] = R[-1][1]
(areainicial, h11, h22, h33) = modules.area_inicial.initial_area(R, Q)
q = modules.calculoeventos.calculaeventos_main(R, Q, maxeps)
h = modules.auxiliar_functions.heap(q)
areamin, epsmin, ayuda = modules.actualizacionarea.actualizar(
    h, q, areainicial, h11, h22, h33, maxeps)

result = [areamin, epsmin]

# auxiliar_functions.dibuja(R,Q,0)
areas = modules.auxiliar_functions.comprueba_area(R, Q, q)

print(result)

# if areamin < 0:
cont = 0
for i, j in zip(areas, ayuda):
    cont = cont + 1
    # print(i-j[0])
    # print('cont', cont)
    print(f"{i} - {j[0]} = {i-j[0]}")
    # print(f"evento tipo {j[1]}")
