# este archivo pretende sustituir al main del programa, ya que tiene la misma funcionalidad, pero solo se pueden comparar canciones2 a 2
import auxiliar_functions
import area_inicial
import calculoeventos
import actualizacionarea
import pandas as pd

tr = []
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\POR MI\código\TFG v5 - fusion de v3 y v4\11-D_TPabon.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\01-D_AMairena.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\02-D_ChanoLobato.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\03-D_Chocolate.csv",
          names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\04-D_JAlmaden.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\05-D_JHeredia.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\06-D_MSimon.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\07-D_MVargas.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\08-D_Naranjito.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\09-D_PdeLucia.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\10-D_TalegondeCordoba.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\11-D_TPabon.csv",
          names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\12-D_Turronero.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\16-D_JMerce.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\18-D_DiegoClavel.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
# tr.append(pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\21-D_RafaelRomeroElGallina.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0))
for x in tr:
    aux = round(float(x.iloc[0, 0]), 4)
    for i in range(len(x)):

        if type(x.iloc[i, 0]) == str:
            x.iloc[i, 0] = float(x.iloc[i, 0])
        if type(x.iloc[i, 1]) == str:
            x.iloc[i, 1] = float(x.iloc[i, 1])
        if type(x.iloc[i, 2]) == str:
            x.iloc[i, 2] = float(x.iloc[i, 2])
        x.iloc[i, 0] = (x.iloc[i, 0]-aux)

Q = auxiliar_functions.prepare_melody(tr[1])
R = auxiliar_functions.prepare_melody(tr[0])

if Q[-1][1] > R[-1][1]:  # en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
    P = Q[:]
    Q = R[:]
    R = P[:]

maxeps = (R[-1][1]-Q[-1][1])/len(Q)
Q[-1][1] = R[-1][1]
(areainicial, h11, h22, h33) = area_inicial.initial_area(R, Q)
q = calculoeventos.calculaeventos_main(R, Q, maxeps)
h = auxiliar_functions.heap(q)
areamin, epsmin, ayuda = actualizacionarea.actualizar(
    h, q, areainicial, h11, h22, h33, maxeps)
result = [areamin, epsmin]
# auxiliar_functions.dibuja(R,Q,0)
areas = auxiliar_functions.comprueba_area(R, Q, q)
# print(result)

for i, j in zip(areas, ayuda):
    print(i-j[0])
    print(f"evento tipo {j[1]}")

# print(len(areas),len(R),len(Q))
