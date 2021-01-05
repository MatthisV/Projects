# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:32:47 2020

@author: Matt
"""
class Graph:
 
    # Constructor
    def __init__(self, edges, N):
 
        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
def HamiltonianPaths(g, v, visited, path, N):
 
    # if all the vertices are visited, then hamiltonian path exists
    if len(path) == N:
        # print hamiltonian path
        print(path)
        return
 
    # Check if every edge starting from vertex v leads to a solution or not
    for w in g.adjList[v]:
 
        # process only unvisited vertices as hamiltonian
        # path visits each vertex exactly once
        if not visited[w]:
            visited[w] = True
            path.append(w)
 
            # check if adding vertex w to the path leads to solution or not
            HamiltonianPaths(g, w, visited, path, N)
 
            # Backtrack
            visited[w] = False
            path.pop()
 
 
if __name__ == '__main__':
 
    # List of graph edges as per above diagram
    edges = [(0, 1), (0, 5), (0, 7), (0, 8), (0, 12),
             (1, 2), (1, 3), (1, 4),(1, 5), (2, 3), (2, 4),(2, 6), (2, 8),
             (3, 4),(6, 8),(8, 7),(8, 9),(8, 10),(9, 10),
             (10, 11),(10, 12),(10, 13),(11, 12),(11, 13),(12, 13)]
 

    # Set number of vertices in the graph
    N = 14
 
    # create a graph from edges
    g = Graph(edges, N)
 
    # starting node, modify it to see every possible Hamiltonian Paths (start=[5,6,7,9,11,12,13])
    start = 7
 
    # add starting node to the path
    path = [start]
 
    # mark start node as visited
    visited = [False] * N
    visited[start] = True
 
    HamiltonianPaths(g, start, visited, path, N)

    """
CAFET 0
UPPER 1
LOWER 2
SECURITY 3
REACT 4
MEDBAY 5
ELEC 6
ADMIN 7
STORAGE 8
COMM 9
SHIELD 10
O2 11
WEAPONS 12
NAV 13

[13, 11, 12, 10, 9, 8, 6, 2, 3, 4, 1, 5, 0, 7] 85
[13, 11, 12, 10, 9, 8, 7, 0, 5, 1, 3, 4, 2, 6] 84.5

[12, 11, 13, 10, 9, 8, 6, 2, 4, 3, 1, 5, 0, 7] 82.5
[12, 11, 13, 10, 9, 8, 7, 0, 5, 1, 3, 4, 2, 6] 82

[11, 12, 13, 10, 9, 8, 6, 2, 4, 3, 1, 5, 0, 7] 83
[11, 12, 13, 10, 9, 8, 7, 0, 5, 1, 3, 4, 2, 6] 82.5

[9, 10, 13, 11, 12, 0, 5, 1, 4, 3, 2, 6, 8, 7] 81
[9, 10, 13, 11, 12, 0, 7, 8, 6, 2, 3, 4, 1, 5] 81

[7, 8, 6, 2, 4, 3, 1, 5, 0, 12, 11, 13, 10, 9] 81
[7, 0, 12, 11, 13, 10, 9, 8, 6, 2, 4, 3, 1, 5] 80.5

Possible start: 5,6,7,9,11,12,13
"""