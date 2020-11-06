# -*- coding: utf-8 -*-
"""
Created on Fri May 8 18:29:23 2020

@author: Matthis
"""

from math import sqrt

k = 3


#Fonctions 

def distance_euclidienne(ligne1,ligne2):
    distance=(ligne1[0]-ligne2[0])**2+(ligne1[1]-ligne2[1])**2+(ligne1[2]-ligne2[2])**2+(ligne1[3]-ligne2[3])**2
    return sqrt(distance)
    

def prediction(valeurs):
    distance = []
    for i in range(len(data)):
        if(valeurs!=data[i]):
            distance.append((distance_euclidienne(valeurs,data[i]),data[i][4]))
    distance.sort()
    compteur = [[0,'A'],[0,'B'],[0,'C'],[0,'D'],[0,'E'],[0,'F'],[0,'G'],[0,'H'],[0,'I'],[0,'J']]
    for i in range(k):
        for j in range(len(compteur)):
            if(distance[i][1]==compteur[j][1]) : 
                compteur[j][0]+=1
    compteur.sort()
    return compteur[len(compteur)-1][1]


def precision(datas):
    correcte = 0
    for i in range(len(datas)):
        if(prediction(datas[i]) == datas[i][4]) : 
            correcte += 1
    return correcte/len(datas)*100


def importerFichier(fichier):
    donnee=[]
    for line in fichier : 
        line = line.split('\n')
        line = line[0].split(';')
        for i in range(4):
            line[i]=float(line[i])
        donnee.append(line)
    return donnee

#Chargement des 3 csv
fichier = open(r'Data.csv','r')
data = importerFichier(fichier)
fichier.close()

fichier2 = open(r'preTest.csv','r')
preTest =importerFichier(fichier2)
fichier2.close()

fichier3 = open(r'finalTest.csv','r')
finalTest = importerFichier(fichier3)
fichier3.close()



#Classification du finalTest, le fichier contient 2000 lignes
fichierLabel = open(r'Villeneuve_Vermeulen.txt','w')
for i in range(len(finalTest)):
        fichierLabel.write(prediction(finalTest[i])+'\n')
fichierLabel.close()



#Précision de chaque jeu de données (Data et preTest)
precisionData=precision(data)
print("Précision pour data.csv : {} %".format(precisionData))
precisionpreTest=precision(preTest)
print("Précision pour preTest.csv : {} %".format(precisionpreTest))
