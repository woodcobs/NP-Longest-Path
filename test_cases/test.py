"""
Authors: Bradley Woodcock, Dylan Roth

This is a test program to test longest_path_exact.py.
"""

import random
import time

from longest_path_exact import main as findLongestPathMain


def main():
    # generate the number of vertices and edges
    numVertices, numEdges = input().split(" ")
    numVertices, numEdges = int(numVertices), int(numEdges)

    # generate the edges
    edges = []
    for _ in range(numEdges):
        node1 = str(random.randint(0, numVertices-1))
        node2 = str(random.randint(0, numVertices-1))

        while node1 == node2:
            node2 = str(random.randint(1, numVertices-1))

        u = node1
        v = node2
        w = str(random.randint(1, 10))
        edges.append((u, v, w))


    # if any nodes are missing an edge, add one
    for i in range(numVertices):
        if not any([edge[0] == str(i) or edge[1] == str(i) for edge in edges]):
            node1 = str(i)
            node2 = str(random.randint(0, numVertices-1))

            # make sure the node doesnt point to itself
            while node1 == node2:
                node2 = str(random.randint(1, numVertices-1))

            u = node1
            v = node2
            w = str(random.randint(1, 10))
            edges.append((u, v, w))

    # print the edges   
    start = time.time()
    findLongestPathMain(numVertices, numEdges, edges)
    end = time.time()
    print("Elapsed time with input", numVertices, numEdges, ":", end - start, "seconds")




    pass


if __name__ == "__main__":
    main()