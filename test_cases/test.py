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
    edgesDict = {}
    for _ in range(numEdges):
        u = str(random.randint(0, numVertices-1))
        v = str(random.randint(0, numVertices-1))
        w = str(random.randint(1, 10))
        # make sure node isnt making a loop and that the edge doesnt already exist
        while (str(u) == str(v)) or ((str(u) + str(v)) in edgesDict):
            u = str(random.randint(0, numVertices-1))
            v = str(random.randint(0, numVertices-1))
        edgesDict[str(u) + str(v)] = True
        
        edges.append((u, v, w))


    
    for edge in edges:
        print(edge[0], edge[1], edge[2])
    # print the edges   
    start = time.time()
    findLongestPathMain(numVertices, numEdges, edges)
    end = time.time()
    print("Elapsed time with input", numVertices, numEdges, ":", end - start, "seconds")




    pass


if __name__ == "__main__":
    main()