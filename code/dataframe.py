# script que  carga los archivos automaticamnte

import pandas as pd
import glob


def dframe():
    tr = []
    # el metodo .drop para quitar la primera columna/fila?

    for f in glob.glob("*.csv"):
        ff = pd.read_csv(
            f, names=["inicio", "duracion", "tono", "nidea"]).drop([0], axis=0)
        tr.append(ff)

    # el siguiente bucle es para 2 cosas, tratar los datos como floats(por algun motivo a veces lo trata como str) y paraque las melodi�as empiecen desde el segundo cero
    for x in tr:  # recorremos cada cancion
        aux = float(x.iloc[0, 0])
        for i in range(len(x)):  # recorremos cada nota de la canción. con este bucle forzamos el comienzo del la primera nota en el instante cero y además conseguimos asegurar que siempre trate los datos como float(pq si no a veces los trata como str)

            if type(x.iloc[i, 0]) == str:
                x.iloc[i, 0] = float(x.iloc[i, 0])
            if type(x.iloc[i, 1]) == str:
                x.iloc[i, 1] = float(x.iloc[i, 1])
            if type(x.iloc[i, 2]) == str:
                x.iloc[i, 2] = float(x.iloc[i, 2])
            x.iloc[i, 0] = x.iloc[i, 0]-aux
    return tr
