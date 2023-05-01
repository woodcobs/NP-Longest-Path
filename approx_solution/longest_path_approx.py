"""
Longest Path Problem (Approximation Solution)
Names: Bradley Woodcock, Dylan Roth
Date: 4/23/2023

This program will find the longest path in a graph. We will be using a Directed Weighted Graph.
The input will be the number of vertices, and the edges themselves.

Example Input:
    4 6
    0 2 500
    1 0 100
    2 0 100
    1 3 100
    3 1 100
    0 1 99
"""
import queue
import random

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
    ans = [str(v) for v in longestPath]
    print(" ".join(ans))

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

def approximateLongest(adjList):
    # Mark vertices visited to ensure a simple path
    visited = set()
    # Stack implementation
    q = queue.LifoQueue()
    # Choose a vertex near the middle of adjList
    middle = len(adjList) // 2
    q.put(middle)
    longestLen = 0

    # Run DFS
    while (q.empty() != True):
        v = q.get()
        if v not in visited:
            visited.add(v)
            # select arbitrary vertex from edge list WRONG
            nextV = random.choice(adjList[v])
            longestLen += nextV[1]
            q.put(nextV[0])
    return visited, longestLen
            


def main():

    # Input the number of vertices and edges
    numVertices, numEdges = map(int, input().split(" ")) 

    adjList = {}
    for i in range(numVertices):
        adjList[i] = []
    
    # input the edges
    for _ in range(numEdges):
        u, v, w = map(int, input().split(" "))
        if u not in adjList:
            adjList[u] = []
        adjList[u].append([v, w])
    
    # output the longest path HERE
    longestPath, longestLen = approximateLongest(adjList)

    print(longestLen)
    print(longestPath)


if __name__ == "__main__":
    main()