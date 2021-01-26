#coding:utf-8
'''
Created on 15 ene. 2021

@author: 34669
'''
import random
from statistics import mode, variance








"""
RELLENAMOS LAS LISTAS
""" 

#Constructor
n=[]
m=[]
p=[]
q=[]
r=[]
listaMedias=[]
listaModas=[]




#Body
for i in range(1000):
    n.append(random.randrange(100))
    m.append(random.randrange(100))
    p.append(random.randrange(100))
    q.append(random.randrange(100))
    r.append(random.randrange(100))
    
"""
 INTRODUCIR EN TXT
 """

file = open("fichero.txt", "w")

file.write("Goles - tal - otro - e - u \n")
    
for i in range(1000):
    cadena = f"{str(n[i])} - {str(m[i])} - {str(p[i])} - {str(q[i])} - {str(r[i])}"
    file.write(cadena + "\n")

file.close();

#Function

def medias():
    
    sumatorioN=0
    sumatorioM=0
    sumatorioP=0
    sumatorioQ=0
    sumatorioR=0
    
    with open("fichero.txt") as archivo:
        a=0
        for line in archivo:
            if a == 0:
                a+=1
            else:
                lista = line.split(" - ")
                sumatorioN += int(lista[0])
                sumatorioM += int(lista[1])
                sumatorioP += int(lista[2])
                sumatorioQ += int(lista[3])
                sumatorioR += int(lista[4])
           
    mediaN = sumatorioN/len(n)
    mediaM = sumatorioM/len(m)
    mediaP = sumatorioP/len(p)
    mediaQ = sumatorioQ/len(q)
    mediaR = sumatorioR/len(r)

    listaMedias.append(mediaN)
    listaMedias.append(mediaM)
    listaMedias.append(mediaP)
    listaMedias.append(mediaQ)
    listaMedias.append(mediaR)

    print(" media de n: " + str(listaMedias[0]) +"\n media de m:" + str(listaMedias[1])+"\n media de p:" + str(listaMedias[2])+"\n media de q:" + str(listaMedias[3])+"\n media de r:" + str(listaMedias[4]))


def mostrar():
    with open("fichero.txt") as file:
        for line in file:
            print(line)
            
def modas():
    aN = []
    aM = []
    aP = []
    aQ = []
    aR = []
       
    with open("fichero.txt") as file:
        a = 0
        for line in file:
            if a == 0:
                a+=1
            else:
                lista = line.split(" - ")
                aN.append(lista[0])
                aM.append(lista[1])
                aP.append(lista[2])
                aQ.append(lista[3])
                aR.append(lista[4])
                
        modaN=mode(aN)
        modaM=mode(aM)
        modaP=mode(aP)
        modaQ=mode(aQ)
        modaR=mode(aR)
            
    #IMPRIMIR MODAS
    print(f"la moda de n es {modaN}")
    print(f"la moda de m es {modaM}")
    print(f"la moda de p es {modaP}")
    print(f"la moda de q es {modaQ}")
    print(f"la moda de r es {modaR}")

def maximos():
    aN = []
    aM = []
    aP = []
    aQ = []
    aR = []
       
    with open("fichero.txt") as file:
        a = 0
        for line in file:
            if a == 0:
                a+=1
            else:
                lista = line.split(" - ")
                aN.append(lista[0])
                aM.append(lista[1])
                aP.append(lista[2])
                aQ.append(lista[3])
                aR.append(lista[4])
        maxN = max(aN)
        maxM = max(aM)
        maxP = max(aP)
        maxQ = max(aQ)
        maxR = max(aR)
    
    print(f"el maximo de n es {maxN}")
    print(f"el maximo de m es {maxM}")
    print(f"el maximo de p es {maxP}")
    print(f"el maximo de q es {maxQ}")
    print(f"el maximo de r es {maxR}")

def minimos():
    aN = []
    aM = []
    aP = []
    aQ = []
    aR = []
       
    with open("fichero.txt") as file:
        a = 0
        for line in file:
            if a == 0:
                a+=1
            else:
                lista = line.split(" - ")
                aN.append(lista[0])
                aM.append(lista[1])
                aP.append(lista[2])
                aQ.append(lista[3])
                aR.append(lista[4])
        minN = min(aN)
        minM = min(aM)
        minP = min(aP)
        minQ = min(aQ)
        minR = min(aR)
    
    print(f"el minimo de n es {minN}")
    print(f"el minimo de m es {minM}")
    print(f"el minimo de p es {minP}")
    print(f"el minimo de q es {minQ}")
    print(f"el minimo de r es {minR}")

def varianzas():
    aN = []
    aM = []
    aP = []
    aQ = []
    aR = []
       
    with open("fichero.txt") as file:
        a = 0
        for line in file:
            if a == 0:
                a+=1
            else:
                lista = line.split(" - ")
                aN.append(int(lista[0]))
                aM.append(int(lista[1]))
                aP.append(int(lista[2]))
                aQ.append(int(lista[3]))
                aR.append(int(lista[4]))
                
        varN=variance(aN)
        varM=variance(aM)
        varP=variance(aP)
        varQ=variance(aQ)
        varR=variance(aR)
    
    print(f"la varianza de n es {varN}")
    print(f"la varianza de m es {varM}")
    print(f"la varianza de p es {varP}")
    print(f"la varianza de q es {varQ}")
    print(f"la varianza de r es {varR}")


