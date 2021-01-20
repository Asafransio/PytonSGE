#coding:utf-8
'''
Created on 15 ene. 2021

@author: 34669
'''
import random









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

file.write("Goles          - tal           - otro           - e           - u \n")
    
for i in range(1000):
    cadena = f"{str(n[i])}            - {str(m[i])}            - {str(p[i])}            - {str(q[i])}            - {str(r[i])}"
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
    #N
    nAux = 0
    for i in n:
        j = n.count(i)
        if j > nAux:
            nAux = j
        
    modaN = []
    
    for i in n:
        j = n.count(i)
        if j == nAux and i not in modaN:
            modaN.append(i)
            
    #M
    mAux = 0
    for i in m:
        j = m.count(i)
        if j > mAux:
            mAux = j
        
    modaM = []
    
    for i in m:
        j = m.count(i)
        if j == mAux and i not in modaM:
            modaM.append(i)
    
    #P
    pAux = 0
    for i in p:
        j = p.count(i)
        if j > pAux:
            pAux = j
        
    modaP = []
    
    for i in p:
        j = p.count(i)
        if j == pAux and i not in modaP:
            modaP.append(i)
            
    #Q
    qAux = 0
    for i in q:
        j = q.count(i)
        if j > qAux:
            qAux = j
        
    modaQ = []
    
    for i in q:
        j = q.count(i)
        if j == qAux and i not in modaQ:
            modaQ.append(i)
            
    #R
    rAux = 0
    for i in r:
        j = r.count(i)
        if j > rAux:
            rAux = j
        
    modaR = []
    
    for i in r:
        j = r.count(i)
        if j == rAux and i not in modaR:
            modaR.append(i)
            
    #IMPRIMIR MODAS
    print(f"la moda de n es {modaN}")
    print(f"la moda de m es {modaM}")
    print(f"la moda de p es {modaP}")
    print(f"la moda de q es {modaQ}")
    print(f"la moda de r es {modaR}")

def maximos():
    maxN = max(n)
    maxM = max(m)
    maxP = max(p)
    maxQ = max(q)
    maxR = max(r)
    
    print(f"el maximo de n es {maxN}")
    print(f"el maximo de m es {maxM}")
    print(f"el maximo de p es {maxP}")
    print(f"el maximo de q es {maxQ}")
    print(f"el maximo de r es {maxR}")

def minimos():
    minN = min(n)
    minM = min(m)
    minP = min(p)
    minQ = min(q)
    minR = min(r)
    
    print(f"el minimo de n es {minN}")
    print(f"el minimo de m es {minM}")
    print(f"el minimo de p es {minP}")
    print(f"el minimo de q es {minQ}")
    print(f"el minimo de r es {minR}")

def varianzas():
    #N
    sumVarN = 0
    for i in n:
        n0 = n[i] - listaMedias[0]
        n1= n0*n0
        sumVarN+=n1
        
    varN = sumVarN/(len(n)-1)
    
    #M
    sumVarM= 0
    for i in m:
        m0 = m[i] - listaMedias[1]
        m1 = m0*m0
        sumVarM += m1
        
    varM = sumVarM/(len(m)-1)
    
    #P
    sumVarP = 0
    for i in p:
        p0 = p[i] - listaMedias[2]
        p1= p0*p0
        sumVarP += p1
        
    varP = sumVarP/(len(p)-1)
    
    #Q
    sumVarQ = 0
    for i in q:
        q0 = q[i] - listaMedias[3]
        q1 = q0*q0
        sumVarQ += q1
        
    varQ = sumVarQ/(len(q)-1)
    
    #R
    sumVarR = 0
    for i in r:
        r0 = r[i] - listaMedias[4]
        r1 = r0*r0
        sumVarR += r1
        
    varR = sumVarR/(len(r)-1)
    
    print(f"la varianza de n es {varN}")
    print(f"la varianza de m es {varM}")
    print(f"la varianza de p es {varP}")
    print(f"la varianza de q es {varQ}")
    print(f"la varianza de r es {varR}")


