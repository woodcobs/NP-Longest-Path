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
import queue

# Approximation Function for Longest Simple Path in a Directed and Weighted Graph
def findApproxLongestPath(adjList, numVertices):
    paths = []
    for v in adjList.keys():
        currPath, currLength = DFS(adjList, v)
        paths.append([currPath, currLength])
    maxLen = -9999999999999
    maxPath = None
    for p, l in paths:
        if len(p) == numVertices and l > maxLen:
            maxLen = l
            maxPath = p
    longestPath = []
    
    print(maxLen)
    print(" ".join(maxPath))


def DFS(adjList, s):
    visited = []
    pathLength = 0
    q = queue.LifoQueue()
    q.put(s)
    while q.empty() != True:
        v = q.get()
        if v not in visited and adjList.get(v):
            visited.append(v)
            print(adjList[v])
            pathLength += int(adjList[v][1])
            for nei in adjList[v]:
                q.put(nei)
    return visited, pathLength


def main():

    # Input the number of vertices and edges
    numVertices, numEdges = map(int, input().split(" ")) 

    adjList = {}
    for i in range(numVertices):
        adjList[str(i)] = {}
    
    # input the edges
    for _ in range(numEdges):
        u, v, w = map(int, input().split(" "))
        u = str(u)
        adjList[u] = ([str(v), str(w)])
    
    # output the longest path HERE
    findApproxLongestPath(adjList, numVertices)


if __name__ == "__main__":
    main()