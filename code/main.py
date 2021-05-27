#Main code

import auxiliar_functions
import area_inicial
import calculoeventos
import actualizacionarea
import dataframe
import pandas as pd


#(R,Q,maxeps)=auxiliar_functions.generate_melodies()
result=[]
tq=pd.read_csv(r"C:\Users\Mike\OneDrive\Documentos\TFG\Documentación teórica\TONAS_0 para trastear\TONAS\Deblas\11-D_TPabon.csv", names=["inicio", "duración", "tono", "nidea"]).drop([0], axis=0)

aux=float(tq.iloc[0,0])
for i in range(len(tq)):#recorremos cada nota de lo que va a ser la Q y forzamos comienzo en instante cero y asegurarmos que los datos se tratan como floats y no como str
    
    if type(tq.iloc[i,0])==str:
        tq.iloc[i,0]=float(tq.iloc[i,0])
    if type(tq.iloc[i,1])==str:
        tq.iloc[i,1]=float(tq.iloc[i,1])
    if type(tq.iloc[i,2])==str:
        tq.iloc[i,2]=float(tq.iloc[i,2])
    tq.iloc[i,0]=tq.iloc[i,0]-aux
           
Q=auxiliar_functions.prepare_melody(tq)#función para convertir formato de panadas.dataframe a list
    
tr=dataframe.dframe() #cargamos en una lista cada una de las canciones de la base de datos

for i in range(len(tr)):#recorremos cada canción del dataframe
    flag=0
    R=auxiliar_functions.prepare_melody(tr[i])#en cada iteración va a ir cambiando la referencia
    
    if Q[-1][1]>R[-1][1]:#en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
        P=Q[:]
        Q=R[:]
        R=P[:]
        flag=1
        
        
    maxeps=(R[-1][1]-Q[-1][1])/len(Q)
    Q[-1][1]=R[-1][1]
    (areainicial,h11,h22,h33)=area_inicial.initial_area(R,Q)
    q=calculoeventos.calculaeventos_main(R,Q,maxeps)
    h=auxiliar_functions.heap(q)
    areamin,epsmin, ayuda=actualizacionarea.actualizar(h,q,areainicial,h11,h22,h33,maxeps)
    result.append([areamin, epsmin])#guardamos en una lista la info de cada una de las referencias
    
    if flag==1:#como hemos machacado el valor de Q necesitamos recuperarlo
        Q=P[:]
        
    # print(f"el área minima se produce para un epsilon de {epsmin} y vale {areamin}")
    #auxiliar_functions.dibuja(R, Q, i)
    # auxiliar_functions.secuencia(R,Q,q)
    # areas=auxiliar_functions.comprueba_area(R,Q,q)
    
    # for i,j in zip(areas,ayuda): 
    #     print(i-j[0])
    #     print(f"evento tipo {j[1]}")
print(result)