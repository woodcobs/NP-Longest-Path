"""
Authors: Bradley Woodcock, Dylan Roth

This is a test program to test longest_path_exact.py.
"""

import random

from longest_path_exact import findLongestPath


def main():
    # generate the number of vertices and edges
    numVertices, numEdges = input().split(" ")
    numVertices, numEdges = int(numVertices), int(numEdges)

    # generate the edges
    edges = []
    for _ in range(numEdges):
        u = str(random.randint(1, numVertices-1))
        v = str(random.randint(1, numVertices-1))
        w = str(random.randint(1, 10))
        edges.append((u, v, w))

    for edge in edges:
        print(" ".join(edge))    

    longestLength, longestPath = findLongestPath(edges)
    print(longestLength, longestPath)

    pass


if __name__ == "__main__":
    main()