"""
Longest Path Problem (Exact Solution)
Names: Bradley Woodcock, Dylan Roth
Date: 10/10/2019

This program will find the longest path in a graph. We will be using a Directed Weighted Graph.
The input will be the number of vertices, and the edges themselves. This will be a brute-force solution.
We will find the longest path in the entire graph by finding the longest path from each vertex to every other vertex.
This will be done by using a backtracking function that will find the longest path from a given vertex to every other vertex.
We will use itertools to generate all possible permutations of the vertices, and then we will find the longest path from each permutation.

Example Input:
    8 10
    0 1 500
    1 2 100
    1 3 100
    1 4 100
    1 5 100
    2 6 99
    3 6 99
    4 6 99
    5 6 99
    6 7 1000
"""
import itertools
def findLongestPath(adjlist, start):
        longestPath = 0

        # find all permutations of the vertices
        permutations = itertools.permutations(adjlist.keys())

        # find the longest path from each permutation
        for permutation in permutations:
             print(permutation)
        return 0
            

def main():

    # Input the number of vertices
    numVertices, numEdges = input().split(" ")
    numVertices, numEdges = int(numVertices), int(numEdges)

    adjlist = {}
    for i in range(numVertices):
        adjlist[i] = {}
    
    # input the edges
    for i in range(numEdges):
        u, v, w = [int(x) for x in input().split(" ")]
        v, v, w = int(u), int(v), int(w)
        adjlist[u][v] = w

    # find the longest path from each vertex to every other vertex
    longestPath = 0
    for i in range(numVertices):
        longestPath = max(longestPath, findLongestPath(adjlist, i))
    return longestPath


if __name__ == "__main__":
    main()

