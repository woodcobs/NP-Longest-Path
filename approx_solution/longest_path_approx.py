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
    path_list = DFS(0, adj_list)
    longestLength = max(len(p) for p in path_list)
    max_path = [p for p in path_list if len(p) == longestLength]

    return longestLength, max_path

def DFS(v, adj_list, visited=None, path=None):
    if visited is None: visited = []
    if path is None: path = [v]

    visited.append(v)

    paths = []
    for p in adj_list[v]:
        if p not in visited:
            p_path = path + [p]
            paths.append(tuple(p_path))
            paths.extend(DFS(p, adj_list, visited[:], p_path))
    return paths


def main():

    # Input the number of vertices and edges
    numVertices, numEdges = map(int, input().split(" ")) 

    adj_list = {}
    for i in range(numVertices):
        adj_list[i] = {}
    
    # input the edges
    for i in range(numEdges):
        u, v, w = map(int, input().split(" "))
        adj_list[u][v] = w
    
    # output the longest path HERE
    longestLength, longestPath = findApproxLongestPath(adj_list)
    print(longestLength)
    print(" ".join(longestPath))


    pass
if __name__ == "__main__":
    main()