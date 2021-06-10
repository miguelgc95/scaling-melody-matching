import pandas as pd
from code.modules.auxiliar_functions import prepare_melody


def create_query(query_path):
    """Generar y preparar melodia de consulta apartir de un archivo .csv"""
    query = pd.read_csv(query_path, names=["inicio", "duración",
                                           "tono", "nidea"]).drop([0], axis=0)

    time_where_query_starts = float(query.iloc[0, 0])

    # cambiar formato de string a float y desplazar la cancion para forzar que empiece en cero
    for i in range(len(query)):
        if type(query.iloc[i, 0]) == str:
            query.iloc[i, 0] = float(query.iloc[i, 0])
        if type(query.iloc[i, 1]) == str:
            query.iloc[i, 1] = float(query.iloc[i, 1])
        if type(query.iloc[i, 2]) == str:
            query.iloc[i, 2] = float(query.iloc[i, 2])
        query.iloc[i, 0] = (query.iloc[i, 0]-time_where_query_starts)

    return prepare_melody(query)
