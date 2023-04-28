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
def findApproxLongestPath(adjList):
    paths = []
    #longestLen = -99999
    for v in adjList.keys():
        #visited, pathLength = DFS(adjList, v)
        #paths.append(visited)
        paths.append(DFS(adjList, v))
        #longestLen = max(longestLen, pathLength)
    longestLen = max([len(p) for p in paths])
    # longestLen = pathLength
    longestPath = []
    for p in paths:
        if len(p) == longestLen:
            longestPath = p
            break
    print(longestLen)
    print(" ".join(longestPath))


def DFS(adjList, s):
    visited = []
    #pathLength = 0
    q = queue.LifoQueue()
    q.put(s)
    while q.empty() != True:
        v = q.get()
        if v not in visited:
            visited.append(v)
            #pathLength += adjList[v][1]
            for nei, _ in adjList[v]:
                q.put(nei)
    return visited #, pathLength


def main():

    # Input the number of vertices and edges
    numVertices, numEdges = map(int, input().split(" ")) 

    adjList = {}
    for i in range(numVertices):
        adjList[i] = []
    
    # input the edges
    for _ in range(numEdges):
        u, v, w = map(int, input().split(" "))
        adjList[u].append([v, w])
    
    # output the longest path HERE
    findApproxLongestPath(adjList)


if __name__ == "__main__":
    main()