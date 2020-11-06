# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:05:30 2020

@author: Matthis
"""


from ortools.sat.python import cp_model

def Sudoku(grilleInitiale): #GrilleInitialecorrespond à une matrice 9x9, que l'on souhaite résoudre.

    #Création du modele    
    model=cp_model.CpModel()
    
    #Création des variables
    cell_size = 3
    line_size = cell_size**2
    line = range(line_size)
    cell = range(cell_size)
    
   
    # On remplit le tableau
    grille = {}
    for i in line:
        for j in line:
            grille[i, j] = model.NewIntVar(1, line_size, 'grid %i %i' % (i, j))
    
    
    
    #Contraintes
    for i in line:
        model.AddAllDifferent([grille[(i, j)] for j in line]) #Différents dans une colonne
    for j in line:
        model.AddAllDifferent([grille[(i, j)] for i in line])   #Idem avec les lignes
        
    for i in cell: #Pour chaque cellule, on vérifie avoir les 9 chiffres
        for j in cell:
            one_cell = [
                    grille[(i * cell_size + k,
                          j * cell_size + l)]
            for k in cell
            for l in cell
        ]
        model.AddAllDifferent(one_cell)
        for i in line:
            for j in line:
                if grilleInitiale[i][j]!=0:
                    model.Add(grille[(i, j)] == grilleInitiale[i][j])
    #Solvers
    solver=cp_model.CpSolver()
    status=solver.Solve(model)
    
    if status==cp_model.FEASIBLE:
       for i in line:
           print([int(solver.Value(grille[(i, j)])) for j in line])


#Exemple avec une grille de 17 cases données
Grille1=[
    [0, 6, 0, 0, 5, 0, 0, 2, 0],
    [0, 0, 0, 3, 0, 0, 0, 9, 0],
    [7, 0, 0, 6, 0, 0, 0, 1, 0],
    [0, 0, 6, 0, 3, 0, 4, 0, 0],
    [0, 0, 4, 0, 7, 0, 1, 0, 0],
    [0, 0, 5, 0, 9, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]       
type(Grille1)
Sudoku(Grille1)#Test avec 17 cases données

