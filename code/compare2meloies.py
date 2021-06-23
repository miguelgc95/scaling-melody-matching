# este archivo pretende sustituir al main del programa, ya que tiene la misma funcionalidad. es en realidad una copia de "intentando arreglar base de datos" ampliandola para que no solo compare 2 a 2
import modules
import pandas as pd
import os

BASE_PATH = os.getcwd()

# QUERY PRE-TREATMENT
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


# REFERENCE PRE-TREATMENT
reference_path = BASE_PATH + '/DB_files/01-D_AMairena.csv'
# reference_path = BASE_PATH + '/DB_files/02-D_ChanoLobato.csv'
# reference_path = BASE_PATH + '/DB_files/03-D_Chocolate.csv'
# reference_path = BASE_PATH + '/DB_files/04-D_JAlmaden.csv'
# reference_path = BASE_PATH + '/DB_files/05-D_JHeredia.csv'
# reference_path = BASE_PATH + '/DB_files/09-D_PdeLucia.csv'

reference = pd.read_csv(reference_path, names=["inicio", "duración",
                                               "tono", "nidea"]).drop([0], axis=0)

time_where_song_starts = float(reference.iloc[0, 0])

# cambiar formato de string a float y desplazar la cancion para forzar que empiece en cero
for i in range(len(reference)):
    if type(reference.iloc[i, 0]) == str:
        reference.iloc[i, 0] = float(reference.iloc[i, 0])
    if type(reference.iloc[i, 1]) == str:
        reference.iloc[i, 1] = float(reference.iloc[i, 1])
    if type(reference.iloc[i, 2]) == str:
        reference.iloc[i, 2] = float(reference.iloc[i, 2])
    reference.iloc[i, 0] = (reference.iloc[i, 0]-time_where_song_starts)

R = auxiliar_functions.prepare_melody(reference)

# aplicamos el algoritmo
result = []
if Q[-1][1] > R[-1][1]:  # en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
    P = Q[:]
    Q = R[:]
    R = P[:]

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

print(result)

# if areamin < 0:
cont = 0
for i, j in zip(areas, ayuda):
    cont = cont + 1
    # print(i-j[0])
    # print('cont', cont)
    print(f"{i} - {j[0]} = {i-j[0]}")
    # print(f"evento tipo {j[1]}")
