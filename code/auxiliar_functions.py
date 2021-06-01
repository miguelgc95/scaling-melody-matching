# auxiliar functions

import random
from matplotlib import pyplot
import heapq
import math
from io import StringIO

import area_inicial


# Creacion de melodías para tener datos con los que trabajar
# se van a crear una lista para cada melodia R y Q.
# cada elemeto de la lista va a ser una lista de 3 valores que indica el tiempo
# de comienzo de la nota, el tiempo de final y el valor de frecuencia

# el primer dato de cada melodia tendra por defecto tiempo de comienzo cero,
# los demas se generaran pseudoaleatoriamente
def generate_melodies():
    """generando melodías para tener con qué trabajar"""
    R = [[0, round(random.uniform(1, 4), 2), random.randint(100, 1000)]]
    Q = [[0, round(random.uniform(1, 4), 2), random.randint(100, 1000)]]

    # creando las notas de R:
    time = R[0][1]
    for i in range(1, 15):  # R tendra 5 notas(de momento, por tener algo)
        newnote = []
        newnote.append(R[i-1][1])
        newtime = random.uniform(1, 4)  # cada nota durara entre 1 y 4 secs
        time += newtime
        newnote.append(round(time, 2))
        # los valores posibles en frecuencia
        newpitch = random.randint(100, 1000)
        newnote.append(newpitch)
        R.append(newnote)

    # creando las notas de Q:
    t = Q[0][1]
    for j in range(1, 10):  # Q tendra 3 notas
        newnote = []
        newnote.append(Q[j-1][1])
        newtime = random.uniform(1, 4)
        t += newtime
        newnote.append(round(t, 2))
        newpitch = random.randint(100, 1000)
        newnote.append(newpitch)
        Q.append(newnote)

    # R=[[0, 1.5, 120], [1.5, 4, 500], [4, 7.8, 400], [7.8, 10, 700]]
    # Q=[[0, 3.8, 300], [3.8, 7, 900], [7, 8.5, 550]]
    # R=[[0, 1.5, 120], [1.5, 4, 500], [4, 7.5, 400], [7.5, 10, 700]]
    # Q=[[0, 3, 300], [3, 7, 900], [7, 8.2, 550]]
    # R=[[0, 1.5, 120], [1.5, 4, 500], [4, 7.5, 400], [7.5, 10, 700],[10,12,350]]
    # Q=[[0, 3.8, 300], [3.8, 7, 900], [7, 9, 550],[9,10.5,600]]
    # R=[[0, 3.45, 293],[3.45, 4.75, 591],[4.75, 8.43, 635],[8.43, 10.22, 544],[10.22, 13.67, 125],[13.67, 15.83, 599]]
    # Q=[[0, 1.98, 435], [1.98, 4.68, 601], [4.68, 6.14, 467], [6.14, 15.83, 177]]
    # vamos a machacar el valor del final de la última nota para que siempre
    # coincida con el de R(extender el valor de la ultima nota de Q hasta el final de los tiempos)

    # maxeps=(R[-1][1]-Q[-1][1])/len(Q)
    # Q[-1][1]=R[-1][1]
    return(R, Q)


def prepare_melody(x):
    """Tratamiento de la base datos para poder usarla en el algoritmo"""
    S = []  # es la lista en la que queda guardada la melodía en el formato correcto
    le = len(x)
    for i in range(le):
        # este if es para contemplar los silencios como una nota de pitch 0
        if i > 0 and abs(S[-1][1]-x.iloc[i, 0]) > 0.001:
            s = []
            # por eso se le da el final de la nota anterior como inicio de la nueva nota
            s.append(S[-1][1])
            # queremos que dure hasta que se empieza a cantar de nuevo
            s.append(x.iloc[i, 0])
            s.append(0)  # y el pitch evidentemente es 0
            S.append(s)
        s = []
        s.append(x.iloc[i, 0])
        s.append(x.iloc[i, 0]+x.iloc[i, 1])

        if i > 0 and (i+1) < le and S[-1][1] > x.iloc[i+1, 0]:
            S[-1][1] = x.iloc[i+1, 0]
        s.append(x.iloc[i, 2])
        S.append(s)
    return S

# def match_initial_time(Q,R):
#     """Ajustar el tiempo de comienzo de ambas melodías al instante cero"""
#     if Q[0][0]>=R[0][0]:
    # for u range(len())


def dibuja(R, Q, n):
    """Función para visualizar gráficamente lo que está pasando"""
    # preparando los datos
    x = []
    xmax = []
    y = []
    x2 = []
    x2max = []
    y2 = []

    for initial_time, end_time, pitch in R:
        x.append(initial_time)
        xmax.append(end_time)
        y.append(pitch)

    for initial_time, end_time, pitch in Q:
        x2.append(initial_time)
        x2max.append(end_time)
        y2.append(pitch)

    # a dibujar
    pyplot.figure(n)

    pyplot.hlines(y, x, xmax, "b", label="R")
    pyplot.vlines(xmax, 0, 1000, "b", "dotted")

    pyplot.hlines(y2, x2, x2max, "r", label="Q")
    pyplot.vlines(x2max, 0, 1000, "r", "dotted")

    pyplot.axhline(0, color="k")
    pyplot.axvline(0, color="k")

    pyplot.legend()
    pyplot.show()


def heap(q):
    """función que crea un heap en el que se guarda el primer evento de cada segmento de Q"""
    h = []
    for j in q:
        if len(j.eps) > 0:
            e = j.eps[0]
            #print('\nincluir en el heap el eveto {:>3} de la nota {}:'.format(round(e[0],2),j.index))
            heapq.heappush(h, [e[0], j.index, e[-1]])
            # show_tree(h)
    return h

# funcion en parte sacada de internet: https://rico-schmidt.name/pymotw-3/heapq/index.html


def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(round(n[0], 2)).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()


def secuencia(R, Q, q):
    """funcion para visualizar lo que se desplaza Q para cada epsilon"""
    n = 1
    r = []
    for qq in q:
        for qqq in qq.eps:
            r.append(qqq)
    r = sorted(r)

    for l in r:
        Qaux = []
        for j in range(len(Q)):
            notaux = []
            notaux.append(Q[j][0]+j*l[0])
            notaux.append(Q[j][1]+(j+1)*l[0])
            notaux.append(Q[j][2])
            Qaux.append(notaux)
        # print(Qaux)
        Qaux[-1][1] = R[-1][1]
        dibuja(R, Qaux, n)
        n += 1


def comprueba_area(R, Q, q):
    """función para comprobar el área para un epsilon concreto"""
    r = []
    for qq in q:
        for qqq in qq.eps:
            r.append(qqq)
    r = sorted(r)

    areas = []
    for l in r:
        Qaux = []
        for j in range(len(Q)):
            notaux = []
            notaux.append(Q[j][0]+j*l[0])
            notaux.append(Q[j][1]+(j+1)*l[0])
            notaux.append(Q[j][2])
            Qaux.append(notaux)
        # print(Qaux)
        Qaux[-1][1] = R[-1][1]
        pak = area_inicial.initial_area(R, Qaux)[0]
        areas.append(round(pak, 6))
    return(areas)
