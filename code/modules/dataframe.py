# script que carga los archivos automaticamnte

import pandas as pd
import glob


def dframe(exclude):

    if exclude == 'exclude_pabon&mairena':
        references_array = exclude_pabon_and_mairena()

    if exclude == 'all_deblas':
        references_array = all_deblas()

    if exclude == 'all_martinetes':
        references_array = all_martinetes()

    # el siguiente bucle es para 2 cosas, tratar los datos como floats(por algun motivo a veces lo trata como str) y paraque las melodi�as empiecen desde el segundo cero
    for reference in references_array:  # recorremos cada cancion
        start_time = float(reference.iloc[0, 0])
        for i in range(len(reference)):  # recorremos cada nota de la canción. con este bucle forzamos el comienzo del la primera nota en el instante cero y además conseguimos asegurar que siempre trate los datos como float(pq si no a veces los trata como str)
            if type(reference.iloc[i, 0]) == str:
                reference.iloc[i, 0] = float(reference.iloc[i, 0])
            if type(reference.iloc[i, 1]) == str:
                reference.iloc[i, 1] = float(reference.iloc[i, 1])
            if type(reference.iloc[i, 2]) == str:
                reference.iloc[i, 2] = float(reference.iloc[i, 2])
            reference.iloc[i, 0] = reference.iloc[i, 0]-start_time
    return references_array


def exclude_pabon_and_mairena():
    references_array = []
    # el metodo .drop para quitar la primera columna/fila?
    for path_name in glob.glob("./DB_files/deblas/*.csv"):
        if ('TPabon' not in path_name) and ('AMairena' not in path_name):
            references_array.append(pd.read_csv(
                path_name, names=["inicio", "duracion", "tono", path_name]).drop([0], axis=0))
    return references_array


def all_deblas():
    references_array = []
    # el metodo .drop para quitar la primera columna/fila?
    for path_name in glob.glob("./DB_files/deblas/*.csv"):
        references_array.append(pd.read_csv(
            path_name, names=["inicio", "duracion", "tono", path_name]).drop([0], axis=0))
    return references_array


def all_martinetes():
    references_array = []
    # el metodo .drop para quitar la primera columna/fila?
    for path_name in glob.glob("./DB_files/martinetes/*.csv"):
        references_array.append(pd.read_csv(
            path_name, names=["inicio", "duracion", "tono", path_name]).drop([0], axis=0))
    return references_array
