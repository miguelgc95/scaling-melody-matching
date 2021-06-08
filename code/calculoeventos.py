# calculo eventos
# Va a haber un objeto Event para cada segmento de Q
# todos los eventos de un mismo segmento tienen el mismo i�ndice y el mismo pitch
# cada evento de cada segmento de Q tendra un epsilon concreto, con una tipologi�a asociada y se guardara la info necesaria para partes futuras del codigo

class Event():
    def __init__(self):
        self.eps = []  # esta lista tendra tantos elementos como eventos tenga dicha nota de Q con R. cada uno de estos elementos sera otra lista que guarda
        # el valor de epsilon en el indice 0, la topologia en el indice 1 y la nota de R con la que se produce el evento en el indice 2 y las
        # 4 alturas de los 6 rectangulos involucrados. el ultimo elemento es el numero del evento del que se trata
        self.index = 0
        self.pitch = 0


def get_epsilons(epsilon, notaactual, notasiguiente, R, maxeps, j):
    """funcion para obtener los eventos y la topologia"""
    n = 0
    for i in range(len(R)):
        # calculamos el valor de epsilon
        e = (R[i][1]-notaactual[1])/(j+1)

        if R[i][1] > notaactual[1] and e < maxeps:
            if j == 0:
                notaactualdesplazada = (
                    0, notaactual[1]+e*(j+1), notaactual[2])
                notasiguientedesplazada = (
                    notasiguiente[0]+e*(j+1), notasiguiente[1] + e*(j+2), notasiguiente[2])
            else:
                notaactualdesplazada = (
                    notaactual[0]+e*(j), notaactual[1]+e*(j+1), notaactual[2])
                notasiguientedesplazada = (
                    notasiguiente[0]+e*(j+1), notasiguiente[1] + e*(j+2), notasiguiente[2])

            # caculo de las 4 alturas existentes:
            # h1 es la altura del primer rectangulo que forman las 2 notas
            h1 = abs(notaactualdesplazada[2]-R[i][2])
            # h2 es la altura del rectanglo c3 que siempre desaparace en un evento
            h2 = abs(notasiguientedesplazada[2]-R[i][2])
            # h3 es la altura del rectangulo c2 que siempre aparace en un evento
            h3 = abs(notaactualdesplazada[2]-R[i+1][2])
            # h4 es la altura del rectangulo que forman las 2 siguientes notas de un evento
            h4 = abs(notasiguientedesplazada[2]-R[i+1][2])

            # caso 0: de c2,c3,c0 a c0,c2,c3
            #       antes del evento: c2 en aumento en la nota actual y un azul contenido en la nota siguiente
            #       Despues del evento: azul contenido en la nota actual y un c3 en disminucion en la nota siguiente
            if notaactualdesplazada[0] <= R[i][0] and R[i+1][1] <= notasiguientedesplazada[1]:
                epsilon.eps.append([e, 0, i, h1, h2, h3, h4, n])
            # caso 1: de c1,c3,c2 a c3,c2,c1
            #       antes del evento: rojo contenido en aumento en la nota actual y un c2 en aumento en la nota siguiente
            #       Despues del evento: c3 en disminucion en la nota actual y un rojo contenido en la nota siguiente
            elif R[i][0] <= notaactualdesplazada[0] and notasiguientedesplazada[1] < R[i+1][1]:
                epsilon.eps.append([e, 1, i, h1, h2, h3, h4, n])

            # caso 2: de c2,c3,c2 a c0,c2,c1
            #       antes del evento: c2 en aumento en la nota actual y un c2 en aumento en la nota siguiente
            #       Despues del evento: azul contenido en la nota actual y un rojo contenido en la nota siguiente
            elif notaactualdesplazada[0] < R[i][0] and notasiguientedesplazada[1] < R[i+1][1]:
                epsilon.eps.append([e, 2, i, h1, h2, h3, h4, n])
            # caso 3: de c1,c3,c0 a c3,c2,c3
            #       antes del evento: rojo contenido en aumento en la nota actual y un azul contenido en la nota siguiente
            #       Despues del evento: c3 en disminucion en la nota actual y un c3 en disminucion en la nota siguiente
            elif R[i][0] < notaactualdesplazada[0] and R[i+1][1] <= notasiguientedesplazada[1]:
                epsilon.eps.append([e, 3, i, h1, h2, h3, h4, n])
            n += 1


def display(q):
    for k in q:
        for l in k.eps:
            print(
                f"\nEl segmento {k.index} tiene un evento de epsilon={l[0]} del tipo {l[1]} con la nota {l[2]}")

# main


def calculaeventos_main(R, Q, maxeps):
    q = []  # esta variable es una lista de objetos events
    for j in range(len(Q)-1):
        epsilon = Event()
        get_epsilons(epsilon, Q[j], Q[j+1], R, maxeps, j)
        epsilon.index = j
        epsilon.pitch = Q[j][2]
        q.append(epsilon)

    # la ultima nota posee un "evento especial" que hay que tratar a parte
    # este ultimo rectangulo sera siempre un c3(rectangulo en disminucion)
    epsilon = Event()
    epsilon.eps.append([maxeps, "final", "final", 0])
    epsilon.index = j+1
    epsilon.pitch = -1
    q.append(epsilon)

    # display(q)
    return q
