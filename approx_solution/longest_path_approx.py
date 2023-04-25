"""
Longest Path Problem (Approximation Solution)
Names: Bradley Woodcock, Dylan Roth
Date: 4/23/2023

This program will find the longest path in a graph. We will be using a Directed Weighted Graph.
The input will be the number of vertices, and the edges themselves.

Example Input:
    4 6
    a c 500
    b a 100
    c a 100
    b d 100
    d b 100
    a b 99
"""
import itertools

# Approximation Function for Longest Simple Path in a Directed and Weighted Graph
def findApproxLongestPath(adj_list):
    pass

def main():

    # Input the number of vertices and edges
    numVertices, numEdges = map(int, input().split(" ")) 

    adjlist = {}
    for i in range(numVertices):
        adjlist[i] = {}
    
    # input the edges
    for i in range(numEdges):
        u, v, w = map(int, input().split())
        adjlist[u][v] = w
    


    pass
if __name__ == "__main__":
    main()