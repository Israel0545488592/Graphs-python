import numpy as np

from IMP.GraphAlgo import GraphAlgo
from IMP.Classes import DiGraph, Node

def generateGraph(n, fileName):
    G = DiGraph()

    # generating nodes
    for i in range(n):
        G.add_node(i, (1, 1, 1))

    # making sure the graph is connected by making a cycle that go throw all nodes
    for i in range(n -1):
        G.add_edge(i, i + 1, np.random.random())

    # closing the cycle
    G.add_edge(n -1, 0, np.random.random())

    # making some random edges
    for i in range(n -1):
        for j in range(20):
            dst = np.random.randint(0, n)
            if dst != i and dst != i + 1:
                G.add_edge(i, j, np.random.random())

    al = GraphAlgo(G)
    al.save_to_json("C:/Users/Israel/computer sience/OOP/Assignments/Ex3/Data/" + fileName + ".json")


if __name__ == '__main__':
    generateGraph(1000, "1000NODES")
    generateGraph(10000, "10000NODES")
    generateGraph(100000, "100000NODES")
