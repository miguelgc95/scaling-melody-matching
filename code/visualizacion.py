#intentando hacer funcional la funcion "secuencia" del archivo auxiliar_functions

import auxiliar_functions
import area_inicial
import calculoeventos
import actualizacionarea

# R,Q=auxiliar_functions.generate_melodies()
# print(R,Q)

#Ejemplo para el doc:
# R=[[0, 1.0, 676], [1.0, 4.8, 106], [4.8, 6.2, 797], [6.2, 7.9, 533], [7.9, 9.18, 406], [9.18, 12.36, 651], [12.36, 13.42, 799], [13.42, 17.02, 657], [17.02, 20.49, 970], [20.49, 23.76, 906], [23.76, 24.78, 591], [24.78, 27.06, 828], [27.06, 28.87, 825], [28.87, 30.38, 537], [30.38, 33.54, 115]] 
# Q=[[0, 1.84, 836], [1.84, 5.58, 372], [5.58, 7.83, 595], [7.83, 11.69, 853], [11.69, 15.47, 386], [15.47, 18.41, 156], [18.41, 20.09, 574], [20.09, 23.74, 194], [23.74, 26.1, 852], [26.1, 28.61, 909]]

#caso normal, solo con evento final
# R=[[0, 4, 40],
#   [4, 6, 30]]

# Q=[[0, 1, 50],
#   [1, 3, 10],
#   [3, 5, 60]]

#caso normal con 1 evento:
# R=[[0, 3.2, 40],
#   [3.2, 6, 30]]

# Q=[[0, 1, 50],
#   [1, 3, 20],
#   [3, 5, 60]]

#2 notas que coinciden en un punto temporal
# R=[[0, 1, 20],
#     [1, 2, 30],
#     [2, 5, 50]]

# Q=[[0, 2, 10],
#     [2, 3, 40],
#     [3, 4, 60]]



#ejemplo con primera nota igual y 2 notas por medio que empiezan a la vez
# R=[[0.0, 1, 30],
#   [1, 3, 50],
#   [3, 4, 20],
#   [4, 8, 60]]

# Q=[[0.0, 1, 40],
#   [1, 2, 70],
#   [2, 3, 10],
#   [3, 5, 80]]


#2 melodías iguales en tiempo
# R=[[0.0, 0.43333299999999997, 66.43],
#   [0.433333, 1.45, 67.43],
#   [1.45, 6, 60]]

# Q=[[0.0, 0.43333299999999997, 65.35],
#   [0.43333299999999997, 1.45, 66.35],
#   [1.45, 4.5, 62.35]]

if Q[-1][1]>R[-1][1]:#en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
    P=Q[:]
    Q=R[:]
    R=P[:]
        
maxeps=round((R[-1][1]-Q[-1][1])/len(Q),5)
Q[-1][1]=R[-1][1]

(areainicial,h11,h22,h33)=area_inicial.initial_area(R,Q)
q=calculoeventos.calculaeventos_main(R,Q,maxeps)
h=auxiliar_functions.heap(q)
areamin, epsmin, ayuda=actualizacionarea.actualizar(h,q,areainicial,h11,h22,h33,maxeps)
result=[areamin, epsmin]
auxiliar_functions.dibuja(R,Q,0)
# auxiliar_functions.secuencia(R,Q,q)
areas=auxiliar_functions.comprueba_area(R,Q,q)
#print(result)

for i,j in zip(areas,ayuda): 
    print(i-j[0])
    # print(f"evento tipo {j[1]}")