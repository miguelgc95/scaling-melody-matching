# este archivo sirve para comparar la eficiencia temporal de aplicar el algoritmo eficiente vs NO eficiente a 2 melodias
import modules
import os
import time

BASE_PATH = os.getcwd()

query_path = BASE_PATH + '/DB_files/deblas/11-D_TPabon.csv'

Q = modules.auxiliar_functions.create_query(query_path)

reference_path = BASE_PATH + '/DB_files/deblas/01-D_AMairena.csv'

# We can use the function 'create_query' to create the reference as long as it just create a valid melody from a .csv file
R = modules.auxiliar_functions.create_query(reference_path)


# en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
if Q[-1][1] > R[-1][1]:
    P = Q[:]
    Q = R[:]
    R = P[:]

maxeps = (R[-1][1]-Q[-1][1])/len(Q)
Q[-1][1] = R[-1][1]

# Applying eficient algorithm
start_time_eficient = time.time()

(areainicial, h11, h22, h33) = modules.area_inicial.initial_area(R, Q)
q = modules.calculoeventos.calculaeventos_main(R, Q, maxeps)
h = modules.auxiliar_functions.heap(q)
areamin, epsmin, ayuda = modules.actualizacionarea.actualizar(
    h, q, areainicial, h11, h22, h33, maxeps)

result = [areamin, epsmin]

end_time_eficient = time.time()

print('Time for eficient algorith:', end_time_eficient - start_time_eficient)

# Applying non eficient algorithm
start_time_non_eficient = time.time()

q = modules.calculoeventos.calculaeventos_main(R, Q, maxeps)
areas = modules.auxiliar_functions.comprueba_area(R, Q, q)

result = min(areas)

end_time_non_eficient = time.time()

print('Time for non eficient algorith:',
      end_time_non_eficient - start_time_non_eficient)
