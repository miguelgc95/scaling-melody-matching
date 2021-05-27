#calculo del area entre 2 melodias dadas. Devuelve las areas y las alturas 
#de cada tipo de rectangulo

def initial_area(R,Q):
    n=len(R)
    i=j=0
    c0, h0 = [], []
    c1, h1 = [], []
    c2, h2 = [], []
    c3, h3 = [], []

    while i<n:
        #caso inicial(hay que tratarlo a parte)
        if i==0 and j==0:
            if R[i][1]<=Q[j][1]:
                h0.append(abs(R[i][2]-Q[j][2]))
                c0.append(h0[-1]*(R[i][1]-R[i][0]))
                i+=1
                # print(h1,h2,h3,0)
            else:
               h=abs(R[i][2]-Q[j][2])
               h2.append((j+1)*h)
               # h2.append(j*h)
               c2.append(h*(Q[j][1]-Q[j][0]))
               j+=1
               # print(h1,h2,h3,1)
        
        #caso especial en el que 2 notas empiezan a la vez y no es el inicio
        elif R[i][0]==Q[j][0] and (i!=0 or j!=0):
            if R[i][1]<=Q[j][1]:
                h=abs(R[i][2]-Q[j][2])
                # h3.append((j-1)*h)
                h3.append(j*h)
                # h3.append((j+1)*h)
                c3.append(h*(R[i][1]-Q[j][0]))
                i+=1
                #print(h1,h2,h3,4)
            else:
               h1.append(abs(R[i][2]-Q[j][2]))
               c1.append(h1[-1]*(Q[j][1]-Q[j][0]))
               j+=1
               # print(h1,h2,h3,3)
        #caso habitual    
        elif R[i][1]<=Q[j][1]:#acaba antes la azul(R)?
            if R[i][0]>Q[j][0]:#azul contenido en rojo
               h0.append(abs(R[i][2]-Q[j][2]))
               c0.append(h0[-1]*(R[i][1]-R[i][0]))
               i+=1
               # print(h1,h2,h3,4)
            else:#rectangulo en disminucion
                h=abs(R[i][2]-Q[j][2])
                # h3.append((j-1)*h)
                h3.append(j*h)
                # h3.append((j+1)*h)
                c3.append(h*(R[i][1]-Q[j][0]))
                i+=1
                # print(h1,h2,h3,5)
        else:
            if Q[j][0]>=R[i][0]: #empieza despues la roja?
                h1.append(abs(R[i][2]-Q[j][2]))
                c1.append(h1[-1]*(Q[j][1]-Q[j][0]))
                j+=1
                # print(h1,h2,h3,6)
            else:#rectangulo en aumento
                h=abs(R[i][2]-Q[j][2])
                h2.append((j+1)*h)
                # h2.append(j*h)
                c2.append(h*(Q[j][1]-R[i][0]))
                j+=1
                # print(h1,h2,h3,7)
                
        
    #Calculo del área inicial:
    c00=sum(c0)
    c11=sum(c1)
    c22=sum(c2)
    c33=sum(c3)
    areainicial=c00+c11+c22+c33
    
    h11=sum(h1)
    h22=sum(h2)
    h33=sum(h3)
    
    return (areainicial,h11,h22,h33)