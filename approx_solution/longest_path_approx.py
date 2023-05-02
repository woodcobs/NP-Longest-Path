"""
Longest Path Problem (Approximation Solution)
Names: Bradley Woodcock, Dylan Roth
Date: 4/23/2023

This program will find the longest path in a graph. We will be using a Directed Weighted Graph.
The input will be the number of vertices, and the edges themselves.

Example Input:
4 6
0 1 500
1 2 100
2 3 100
1 3 100
0 2 100
3 0 99
"""

import random


def main(numVertices = None, numEdges = None, testEdges = None):

    # Input the number of vertices
    if not (numVertices and numEdges):
        numVertices, numEdges = map(int, input().split(" ")) 

    adjlist = {}

    for i in range(numVertices):
        adjlist[str(i)] = {}
        
    # input the edges
    if not testEdges:
        for _ in range(numEdges):
            u, v, w = input().split(" ")
            w = int(w)
            adjlist[u][v] = w
    else:
        for edge in testEdges:
            u, v, w = edge
            adjlist[u][v] = int(w)

    print(adjlist)
    # find the longest path from each vertex to every other vertex

    attempts = 1000
    longestLength = 0
    longestPath = None
    for _ in range(attempts):
        currLength, currPath = findLongestPath(adjlist)
        if currLength > longestLength:
            longestLength = currLength
            longestPath = currPath

    if longestLength and longestPath:
        print(longestLength)
        print(" ".join(longestPath))
    else:
        print("No path to all vertices found")

# Approximate Longest Path in a Directed and Weighted Graph using a Greedy Algorithm (Not Optimal)
def findLongestPath(adjList):
    # Randomly choose a starting vertex
    start = random.choice(list(adjList.keys()))
    # Initialize the path with the starting vertex
    path = [start]
    # Initialize the path length to 0
    pathLength = 0
    # Initialize the current vertex to the starting vertex
    curr = start
    # Initialize the visited set to the starting vertex
    visited = set([start])
    # Initialize the unvisited set to all the other vertices
    unvisited = set(adjList.keys())
    unvisited.remove(start)
    # While there are still unvisited vertices
    while len(unvisited) > 0:
        # Find the neighbor with the largest weight
        maxWeight = -99999
        maxNeighbor = None
        for nei, w in adjList[curr].items():
            if nei not in visited:
                if w > maxWeight:
                    maxWeight = w
                    maxNeighbor = nei
        # If there are no unvisited neighbors, break
        if maxNeighbor == None:
            break
        # Add the neighbor to the path
        path.append(maxNeighbor)
        # Add the weight of the neighbor to the path length
        pathLength += maxWeight
        # Add the neighbor to the visited set
        visited.add(maxNeighbor)
        # Remove the neighbor from the unvisited set
        unvisited.remove(maxNeighbor)
        # Update the current vertex to the neighbor
        curr = maxNeighbor
    # Return the path length and the path
    return pathLength, path

# def findLongestPath(adjList):

if __name__ == "__main__":
    main()