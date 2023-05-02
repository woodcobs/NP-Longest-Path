"""
Longest Path Problem (Approximation Solution)
Names: Bradley Woodcock, Dylan Roth
Date: 4/23/2023

This program will find the longest path in a graph. We will be using a Directed Weighted Graph.
The input will be the number of vertices and edges, and the edges themselves.

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


def main(numVertices = None, numEdges = None):
    # Input
    # Get the number of vertices and edges
    if not (numVertices and numEdges):
        numVertices, numEdges = map(int, input().split(" ")) 

    # Create Adjacency List
    adjlist = {}
    for i in range(numVertices):
        adjlist[str(i)] = {}
    for _ in range(numEdges):
        u, v, w = input().split(" ")
        w = int(w)
        adjlist[u][v] = w

    # Approximate the longest path over X attempts
    attempts = 100000
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


# Approximate Longest Path in a weighted Digraph using Greedy Algorithm
def findLongestPath(adjList):
    # Create a path list beginning with random starting vertex
    start = random.choice(list(adjList.keys()))
    path = [start]
    # Set initial path length to 0
    pathLength = 0
    # Set current vertex to start vertex
    currV = start
    # Initialize the visited set with starting vertex
    visited = set([start])
    # Initialize unvisited set to all vertices but starting vertex
    unvisited = set(adjList.keys())
    unvisited.remove(start)
    # While there are still unvisited vertices
    while len(unvisited) > 0:
        # Greedy choice: the neighbor with the largest weight
        maxWeight = -99999
        maxNeighbor = None
        for nei, w in adjList[currV].items():
            if nei not in visited:
                if w > maxWeight:
                    maxWeight = w
                    maxNeighbor = nei
        # If no more unvisited neighbors, then finish
        if maxNeighbor == None:
            break
        # Add current neighbor to path
        path.append(maxNeighbor)
        # Add the weight of current neighbor to the path length
        pathLength += maxWeight
        # Mark current neighbor as visited
        visited.add(maxNeighbor)
        # Remove current neighbor from unvisited
        unvisited.remove(maxNeighbor)
        # Update the current vertex to the current max neighbor
        currV = maxNeighbor
    
    # Return the path and its length
    return pathLength, path


if __name__ == "__main__":
    main()