# este archivo pretende sustituir al main del programa, ya que tiene la misma funcionalidad. es en realidad una copia de "intentando arreglar base de datos" ampliandola para que no solo compare 2 a 2
import auxiliar_functions
import area_inicial
import calculoeventos
import actualizacionarea
import dataframe
import pandas as pd


x = pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\11-D_TPabon.csv",
                names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0)

aux = float(x.iloc[0, 0])
for i in range(len(x)):

    if type(x.iloc[i, 0]) == str:
        x.iloc[i, 0] = float(x.iloc[i, 0])
    if type(x.iloc[i, 1]) == str:
        x.iloc[i, 1] = float(x.iloc[i, 1])
    if type(x.iloc[i, 2]) == str:
        x.iloc[i, 2] = float(x.iloc[i, 2])
    x.iloc[i, 0] = (x.iloc[i, 0]-aux)

Q = auxiliar_functions.prepare_melody(x)
# cargamos en una lista cada una de las canciones de la base de datos
tr = dataframe.dframe()

result = []
for i in range(len(tr)):  # recorremos cada canción del dataframe

    flag = 0
    # en cada iteración va a ir cambiando la referencia
    R = auxiliar_functions.prepare_melody(tr[i])

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

    print(flag)
    if flag == 1:  # como hemos machacado el valor de Q necesitamos recuperarlo
        Q = P[:]

    if areamin < 0:
        print(i)
       # for i,j in zip(areas,ayuda):
       #      print(i-j[0])
       #      print(f"evento tipo {j[1]}")
print(result)
