# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 12:20:49 2020

@author: Matt
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 

G=nx.Graph()

for i in range(9):
    G.add_node(i)
    
G.add_edges_from([(0,1),(0,4),(0,5),
                  (1,0),(1,2),(1,6),
                 (2,1),(2,3),(2,7),
                 (3,2),(3,4),(3,8),
                 (4,0),(4,3),(4,9),
                 (5,0),(5,7),(5,8),
                 (6,1),(6,8),(6,9),
                 (7,2),(7,5),(7,9),
                 (8,3),(8,5),(8,6),
                 (9,4),(9,6),(9,7)])

def random_coloring(graph,n_colors):
    coloring = {}
    for node in graph.nodes():
        coloring[node] = np.random.randint(0,n_colors)
    return coloring

colors = ['red','blue','green','orange']

def draw_coloring(G,coloring,colors):
    fig = plt.figure()
    n_colors = len(colors)

    pos = nx.spring_layout(G)
    for i in range(n_colors):
        nx.draw_networkx_nodes(G,pos,[x for x in G.nodes() if coloring[x]==i],width=8,node_color=colors[i],label=True)
        nx.draw_networkx_labels(G, pos, labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=None, bbox=None, horizontalalignment='center', verticalalignment='center', ax=None)
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
        
    plt.axis('off')
    plt.show() 
    return fig




nx.draw(G,with_labels=True)

draw_coloring(G,random_coloring(G,4),colors)


from ortools.sat.python import cp_model

def SecondImposter(x):
    #Creates model
    
    model=cp_model.CpModel()
    #Creates variables
    num_vals=10
    y=model.NewIntVar(1,num_vals-1,'y')

    
    #Creates the constraints
    model.Add(y!=x)

    if x==1:
        model.Add(y!=2)
        model.Add(y!=6)
    if x==4:
        model.Add(y!=3)
        model.Add(y!=9)
    if x==5:
        model.Add(y!=7)
        model.Add(y!=8)
    
    
    #Creates a solver and solves the model
    solver=cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter([y])
    status=solver.SearchForAllSolutions(model, solution_printer)
    
        
class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count
        


def PossibleImposter():
    print("if 1 is imposter, the other imposter could be")
    print()
    SecondImposter(1)
    print()
    print("if 4 is imposter, the other imposter could be")
    print()
    SecondImposter(4)
    print()
    print("if 5 is imposter, the other imposter could be")
    print()
    SecondImposter(5)
    print()
    print("So there are 15 set of possible imposters:")
    print()
    print("1:3  1:4  1:5  1:7  1:8  1:9  4:2  4:5  4:6  4:7  4:8  5:2  5:3  5:6  5:9")
    print("Each set has 1 chance out of 18 of being the right set of imposters, exept  1:4  1:5  and  4:5  they have 1 chance out of 9")
    

    
    
    
    
    
    
PossibleImposter()