# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:45:07 2020

@author: Matt
"""



# Number of vertices in the graph and INF as the max value
V = 14
INF = 99999

def floydWarshall(graph): 
	dist = list(map(lambda i : list(map(lambda j : j , i)) , graph) )

	for k in range(V): 
		for i in range(V): 
			for j in range(V): 
				dist[i][j] = min(dist[i][j] , dist[i][k]+ dist[k][j] ) 
	return printSolution(dist) 


# A function to print the solution 
def printSolution(dist): 
    l=""
    l+= ("\nShortest paths beween each nodes/vertices: " )
    for i in range(V): 
        l+=("\n")
        for j in range(V): 
            if(dist[i][j] == INF): 
                l+= ("%7s" %("INF")) 
            else: 
                l+= ("%7d" %(dist[i][j]))
            if j == V-1: 
                l+= ("") 
    l+="\n"
    return l


graphImpostor = [[0,9.5,INF,INF,INF,7.5,INF,0,8,INF,3.5,6,5.5,4], 
			[9.5,0,7,6,0,7,INF,INF,INF,INF,INF,INF,INF,INF], 
			[INF, 7, 0, 6, 0, INF, 8, INF,10,INF,INF,INF,INF,INF], 
			[INF, 6, 6, 0, 5, 0, 0,INF,INF,INF,INF,INF,INF,INF],
            [INF, 0, 0, 5, 0, INF, INF,INF,INF,INF,INF,INF,INF,INF],
            [7.5, 7, INF, 0, INF, 0, 0,INF,INF,INF,INF,INF,INF,INF],
            [INF, INF, 8, 0, INF, 0, 0,INF,7,INF,INF,INF,INF,INF],
            [0,INF,INF,INF,INF,INF,INF,0,6.5,INF,3.5,6,6.5,4],
            [8,INF,10,INF,INF,INF,7,6.5,0,6,6.5,INF,INF,INF],
            [INF,INF,INF,INF,INF,INF,INF,INF,6,0,4.5,INF,INF,INF],
            [INF,INF,INF,INF,INF,INF,INF,3.5,6.5,4.5,0,9.5,10,0],
            [6,INF,INF,INF,INF,INF,INF,6,INF,INF,9.5,0,4.5,6],
            [5.5,INF,INF,INF,INF,INF,INF,6.5,INF,INF,10,4.5,0,0],
            [4,INF,INF,INF,INF,INF,INF,4,INF,INF,0,6,0,0]
		] 


graphCrew = [[0,9.5,INF,INF,INF,7.5,INF,7.5,8,INF,INF,INF,5.5,INF], 
			[9.5,0,7,6,6,7,INF,INF,INF,INF,INF,INF,INF,INF], 
			[INF, 7, 0, 6, 6, INF, 8, INF,10,INF,INF,INF,INF,INF], 
			[INF, 6, 6, 0, 5, INF, INF,INF,INF,INF,INF,INF,INF,INF],
            [INF, 6, 6, 5, 0, INF, INF,INF,INF,INF,INF,INF,INF,INF],
            [7.5, 7, INF, INF, INF, 0, INF,INF,INF,INF,INF,INF,INF,INF],
            [INF, INF, 8, INF, INF, INF, 0,INF,7,INF,INF,INF,INF,INF],
            [7.5,INF,INF,INF,INF,INF,INF,0,6.5,INF,INF,INF,INF,INF],
            [8,INF,10,INF,INF,INF,7,6.5,0,6,6.5,INF,INF,INF],
            [INF,INF,INF,INF,INF,INF,INF,INF,6,0,4.5,INF,INF,INF],
            [INF,INF,INF,INF,INF,INF,INF,INF,6.5,4.5,0,9.5,10,7.5],
            [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,9.5,0,4.5,6],
            [5.5,INF,INF,INF,INF,INF,INF,INF,INF,INF,10,4.5,0,6.5],
            [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,7.5,6,6.5,0]
		] 


print("\n\nImpostor's floyd:\n\n"+floydWarshall(graphImpostor))
print("\n\nCrewmate's floyd:\n\n"+floydWarshall(graphCrew))


