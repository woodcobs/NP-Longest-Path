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
    4 6
    0 2 500
    1 0 100
    2 0 100
    1 3 100
    3 1 100
    0 1 99


    4 6
0 2 500
1 0 100
2 0 100
1 3 100
3 1 100
0 1 99
"""
import itertools
import time



def findLongestPath(adjlist):
        maxLength = 0
        path = None

        # find all permutations of the vertices
        permutations = itertools.permutations(adjlist.keys())

        # find the longest path from each permutation
        for permutation in permutations:
            currLength = 0
            currPath = []
            currPath.append(permutation[0])
            for i in range(len(permutation)-1):
                if adjlist.get(permutation[i]) and adjlist.get(permutation[i]).get(permutation[i+1]):
                        currLength += adjlist[permutation[i]][permutation[i+1]]   
                        currPath.append(permutation[i + 1])
                else:
                     break
            if currLength > maxLength:
                maxLength = currLength
                path = currPath.copy()
        return maxLength, path
            

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

    # find the longest path from each vertex to every other vertex
    start = time.time()
   
    longestLength, longestPath = findLongestPath(adjlist)
    if longestLength and longestPath:
        print(longestLength)
        print(" ".join(longestPath))
    else:
        print("No path to all vertices found")
    end = time.time()
    #print("Elapsed time with input", numVertices, numEdges, ":", end - start, "seconds")


if __name__ == "__main__":
    main()

