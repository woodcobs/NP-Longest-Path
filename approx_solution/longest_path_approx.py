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
import queue
import random

# Approximation Function for Longest Simple Path in a Directed and Weighted Graph
# def findApproxLongestPath(adjList):
#     paths = []
#     #longestLen = -99999
#     for v in adjList.keys():
#         #visited, pathLength = DFS(adjList, v)
#         #paths.append(visited)
#         paths.append(DFS(adjList, v))
#         #longestLen = max(longestLen, pathLength)
#     longestLen = max([len(p) for p in paths])
#     # longestLen = pathLength
#     longestPath = []
#     for p in paths:
#         if len(p) == longestLen:
#             longestPath = p
#             break
#     print(longestLen)
#     ans = [str(v) for v in longestPath]
#     print(" ".join(ans))

# def DFS(adjList, s):
#     visited = []
#     #pathLength = 0
#     q = queue.LifoQueue()
#     q.put(s)
#     while q.empty() != True:
#         v = q.get()
#         if v not in visited:
#             visited.append(v)
#             #pathLength += adjList[v][1]
#             for nei, _ in adjList[v]:
#                 q.put(nei)
#     return visited #, pathLength


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

def findLongestPath(adjList):
    start = random.choice(list(adjList.keys()))
    path = [start]
    pathLength = 0
    curr = start

    visited = set([start])
    unvisited = set(adjList.keys())
    unvisited.remove(start)

    while len(unvisited) > 0:
        maxWeight = -99999
        maxNeighbor = None
        for nei, w in adjList[curr].items():
            if nei not in visited:
                if w > maxWeight:
                    maxWeight = w
                    maxNeighbor = nei
        if maxNeighbor == None:
            break

        path.append(maxNeighbor)
        pathLength += maxWeight
        visited.add(maxNeighbor)
        unvisited.remove(maxNeighbor)
        curr = maxNeighbor

    return pathLength, path


if __name__ == "__main__":
    main()