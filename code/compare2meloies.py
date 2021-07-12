# este archivo pretende sustituir al main del programa, ya que tiene la misma funcionalidad. es en realidad una copia de "intentando arreglar base de datos" ampliandola para que no solo compare 2 a 2
import modules
import os
import numpy as np

BASE_PATH = os.getcwd()

# query_path = BASE_PATH + '/DB_files/deblas/01-D_AMairena.csv'
# query_path = BASE_PATH + '/DB_files/deblas/02-D_ChanoLobato.csv'
# query_path = BASE_PATH + '/DB_files/deblas/03-D_Chocolate.csv'
# query_path = BASE_PATH + '/DB_files/deblas/04-D_JAlmaden.csv'
# query_path = BASE_PATH + '/DB_files/deblas/05-D_JHeredia.csv'
# query_path = BASE_PATH + '/DB_files/deblas/06-D_MSimon.csv'
# query_path = BASE_PATH + '/DB_files/deblas/07-D_MVargas.csv'
# query_path = BASE_PATH + '/DB_files/deblas/08-D_Naranjito.csv'
# query_path = BASE_PATH + '/DB_files/deblas/09-D_PdeLucia.csv'
# query_path = BASE_PATH + '/DB_files/deblas/10-D_TalegondeCordoba.csv'
# query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'
query_path = BASE_PATH + '/DB_files/deblas/18-D_DiegoClavel.csv'
Q_dict = modules.auxiliar_functions.create_query(query_path)
Q = list(Q_dict.values())[0]

# We can use the function 'create_query' to create the reference as long as it just create a valid melody from a .csv file
reference_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'
R_dict = modules.auxiliar_functions.create_query(reference_path)
R = list(R_dict.values())[0]

# aplicamos el algoritmo

if Q[-1][1] > R[-1][1]:  # en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
    P = Q[:]
    Q = R[:]
    R = P[:]

maxeps = (R[-1][1]-Q[-1][1])/len(Q)
modules.auxiliar_functions.dibuja(R, Q, 0)

Q[-1][1] = R[-1][1]
(areainicial, h11, h22, h33) = modules.area_inicial.initial_area(R, Q)
q = modules.calculoeventos.calculaeventos_main(R, Q, maxeps)
h = modules.auxiliar_functions.heap(q)
areamin, epsmin, ayuda = modules.actualizacionarea.actualizar(
    h, q, areainicial, h11, h22, h33, maxeps)


# auxiliar_functions.dibuja(R,Q,0)
areas = modules.auxiliar_functions.comprueba_area(R, Q, q)


result_eficient = areamin

result_non_eficient = min(areas)

# print(R.columns.values[3])

print('result_eficient \t\t\t', result_eficient)
print('result_non_eficient \t', result_non_eficient)

modules.auxiliar_functions.dibuja(R, Q, 0)
print(epsmin)

Qaux = []
for j in range(len(Q)):
    notaux = []
    notaux.append(Q[j][0]+j*epsmin)
    notaux.append(Q[j][1]+(j+1)*epsmin)
    notaux.append(Q[j][2])
    Qaux.append(notaux)
# print(Qaux)
Qaux[-1][1] = R[-1][1]

modules.auxiliar_functions.dibuja(R, Qaux, 1)

# if areamin < 0:
# cont = 0
# for i, j in zip(areas, ayuda):
#     cont = cont + 1
#     # print(i-j[0])
#     # print('cont', cont)
#     print(f"{i} - {j[0]} = {i-j[0]}")
# print(f"evento tipo {j[1]}")
