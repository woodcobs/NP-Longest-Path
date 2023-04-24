"""
Longest Path Problem (Approximation Solution)
Names: Bradley Woodcock, Dylan Roth
Date: 10/10/2019

This program will find the longest path in a graph. We will be using a Directed Weighted Graph.
The input will be the number of vertices, and the edges themselves.

Example Input:


"""
import itertools

def main():

    # Input the number of vertices
    numVertices = map(int, input().split()) 
    numEdges = numVertices - 1

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