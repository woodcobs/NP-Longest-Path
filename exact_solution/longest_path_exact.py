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
    a c 500
    b a 100
    c a 100
    b d 100
    d b 100
    a b 99
"""
import itertools
def findLongestPath(adjlist, start):
        maxLength = 0
        path = None

        # find all permutations of the vertices
        permutations = itertools.permutations(adjlist.keys())

        # find the longest path from each permutation
        for permutation in permutations:
            currLength = 0
            for i in range(len(permutation)-1):
                if adjlist.get(permutation[i]):
                    if adjlist.get(permutation[i]).get(permutation[i+1]):
                        currLength += adjlist.get(permutation[i]).get(permutation[i+1])
                else:
                    currLength = 0
                    break
            if currLength > maxLength:
                maxLength = currLength
                path = permutation
        return maxLength, path
            

def main():

    # Input the number of vertices
    numVertices, numEdges = map(int, input().split(" ")) 

    adjlist = {}

    start = 'a'
    for _ in range(numVertices):
        adjlist[start] = {}
        start = chr(ord(start) + 1)
    # input the edges
    for i in range(numEdges):
        u, v, w = input().split(" ")
        w = int(w)
        adjlist[u][v] = w

    # find the longest path from each vertex to every other vertex
    for i in range(numVertices):
        longestLength, longestPath = findLongestPath(adjlist, i)
        
    print("The longest path is: ", longestPath, " with a length of: ", longestLength)


if __name__ == "__main__":
    main()
