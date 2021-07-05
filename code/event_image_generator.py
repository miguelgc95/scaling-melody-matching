import modules

# antesevento0
# R = [[0, 2, 0], [2, 4, 200], [4, 5, 300]]
# Q = [[0, 1, 0], [1, 3, 100], [3, 6, 400]]

# despuesevento0
# R = [[0, 2, 0], [2, 4, 200], [4, 5, 300]]
# Q = [[0, 1.5, 0], [1.5, 4.5, 100], [4.5, 7, 400]]

# antesevento1
# R = [[0, 1, 0], [1, 3, 200], [3, 5, 300]]
# Q = [[0, 2, 0], [2, 3, 100], [4, 6, 400]]

# # despuesevento1
# R = [[0, 1, 0], [1, 4, 200], [4, 6, 300]]
# Q = [[0, 2.5, 0], [2.5, 4.5, 100], [4.5, 5.5, 400]]

# antesevento2
# R = [[0, 2, 0], [2, 4, 200], [4, 6, 300]]
# Q = [[0, 1, 0], [1, 3, 100], [3, 5, 400]]

# # despuesevento2
# R = [[0, 2, 0], [2, 4, 200], [4, 6, 300]]
# Q = [[0, 1.5, 0], [1.5, 4.5, 100], [4.5, 5.5, 400]]

# antesevento3
# R = [[0, 1, 0], [1, 4, 200], [4, 5, 300]]
# Q = [[0, 2, 0], [2, 3, 100], [3, 6, 400]]

# despuesevento3
R = [[0, 1, 0], [1, 4, 200], [4, 5, 300]]
Q = [[0, 2.5, 0], [2.5, 4.5, 100], [4.5, 6, 400]]

i = 0
modules.auxiliar_functions.dibuja(R, Q, i)


maxeps = (R[-1][1]-Q[-1][1])/len(Q)
Q[-1][1] = R[-1][1]
(areainicial, h11, h22, h33) = modules.area_inicial.initial_area(R, Q)
q = modules.calculoeventos.calculaeventos_main(R, Q, maxeps)
h = modules.auxiliar_functions.heap(q)
areamin, epsmin, ayuda = modules.actualizacionarea.actualizar(
    h, q, areainicial, h11, h22, h33, maxeps)

modules.auxiliar_functions.secuencia(R, Q, q)
