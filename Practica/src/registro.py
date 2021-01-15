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
        for line in archivo:
            lista = line.split(" - ")
            sumatorioN += int(lista[0])
            sumatorioM += int(lista[1])
            sumatorioP += int(lista[2])
            sumatorioQ += int(lista[3])
            sumatorioR += int(lista[4])
           
    mediaN = sumatorioN/1000
    mediaM = sumatorioM/1000
    mediaP = sumatorioP/1000
    mediaQ = sumatorioQ/1000
    mediaR = sumatorioR/1000

    listaMedias = [mediaN, mediaM, mediaP, mediaQ, mediaR]

    print("media de goles: " + str(listaMedias[0]) +"\n media de tiros a puerta:" + str(listaMedias[1])+"\n media de medias:" + str(listaMedias[2])+"\n media de algo:" + str(listaMedias[3])+"\n media de bajas:" + str(listaMedias[4]))


def mostrar():
    with open("fichero.txt") as file:
        for line in file:
            print(line)





