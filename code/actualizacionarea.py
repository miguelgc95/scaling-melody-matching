# actualizacion y calculo de area

import heapq

# inicializamos area minima como area inicial

# while (mientras queden elementos en el heap):
#     sacar el nodo raiz del heap,
#     mirar a que segmento de q pertenece el evento que acabamos de sacar,
#     ver si para dicho segmento quedan eventos que meter en el heap,
#     en caso afirmativo, meter dicho evento en el heap

#     para el evento sacado:
#     recalcular el area
#     comparar la nueva area con el area minima
#     si la nueva es menor sobreescribimos area minima con este nuevo valor
#     actualizar las alturas de los rectangulos involucrados en el evento para el proximo evento


def actualizar(h, q, areainicial, h11, h22, h33, maxeps):
    areamin = areainicial
    areaanterior = areainicial
    epsilonanterior = 0
    epsmin = 0
    i = 0
    ayuda = []
    while(h):
        # recupera es una lista de 3 elementos. el 0 es un valor de epsilon, el 1 es la nota de Q para la que se produce dicho epsilon y el 2 el nº de evento para esa nota
        recupera = heapq.heappop(h)
        nuevoepsilon = recupera[0]
        j = recupera[1]
        n = recupera[2]
        # en esta lista hemos guardado toda la info relativa al proximo evento que se producira en el tiempo(osea, el menos evento siguiente)
        nuevoevento = q[j].eps[n]

        nuevaarea = areaanterior+(nuevoepsilon-epsilonanterior)*(h11+h22-h33)
        ayuda.append([nuevaarea, nuevoevento[1]])
        if nuevaarea < areamin:
            areamin = nuevaarea
            epsmin = nuevoepsilon

        if nuevoepsilon == maxeps:
            break

        # si aun quedan eventos para el segmento del que acabamos de sacar nuevoevento:
        if len(q[j].eps) > (n+1):
            heapq.heappush(h, [q[j].eps[n+1][0], q[j].index, n+1])

        # preparamos los datos para la siguiente ejecucion:
        areaanterior = nuevaarea
        epsilonanterior = nuevoepsilon

        # chequeamos topología para saber como actualizar las alturas
        if nuevoevento[1] == 0:
            h11 = h11
            # h22=h22-(j+1)*nuevoevento[3]+(j+1)*nuevoevento[5]
            # h33=h33-j*nuevoevento[4]+j*nuevoevento[6]

            h22 = h22-(j+1)*nuevoevento[3]+(j+1)*nuevoevento[5]
            h33 = h33-(j+1)*nuevoevento[4]+(j+1)*nuevoevento[6]

        elif nuevoevento[1] == 1:
            h11 = h11-nuevoevento[3]+nuevoevento[6]
            # h22=h22-(j+1)*nuevoevento[6]+(j+1)*nuevoevento[5]
            # h33=h33-j*nuevoevento[4]+j*nuevoevento[3]

            h22 = h22-(j+2)*nuevoevento[6]+(j+1)*nuevoevento[5]
            h33 = h33-(j+1)*nuevoevento[4]+(j)*nuevoevento[3]

        elif nuevoevento[1] == 2:
            h11 = h11+nuevoevento[6]
            # h22=h22-(j+1)*nuevoevento[3]-(j+1)*nuevoevento[6]+(j+1)*nuevoevento[5]
            # h33=h33-j*nuevoevento[4]

            h22 = h22-(j+1)*nuevoevento[3]-(j+2) * \
                nuevoevento[6]+(j+1)*nuevoevento[5]
            h33 = h33-(j+1)*nuevoevento[4]

        elif nuevoevento[1] == 3:
            h11 = h11-nuevoevento[3]
            # h22=h22+(j+1)*nuevoevento[5]
            # h33=h33-j*nuevoevento[4]+j*nuevoevento[3]+j*nuevoevento[6]

            h22 = h22+(j+1)*nuevoevento[5]
            h33 = h33-(j+1)*nuevoevento[4]+(j) * \
                nuevoevento[3]+(j+1)*nuevoevento[6]

        i += 1

    return areamin, epsmin, ayuda
