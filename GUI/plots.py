from IMP.Classes import Node, DiGraph
from IMP.GraphAlgo import GraphAlgo
import matplotlib.pyplot as plt

g_algo = GraphAlgo()
file = "C:/Users/Israel/computer sience/OOP/Assignments/Ex3/Data/A5"
g_algo.load_from_json(file + '.json')
g_algo.save_to_json(file + "_edited.json")

G = g_algo.get_graph()

G.get_all_v()

LocData = [(node.loc[0], node.loc[1]) for node in G.get_all_v().values()]

LocData = list(map(list, zip(*LocData)))
x = LocData[0]
y = LocData[1]

plt.scatter(x, y, s = 70)
for src in G.get_all_v().keys():
    for dst in G.all_out_edges_of_node(src).keys():

        node = G.nodes[src]
        x = node.loc[0]
        y = node.loc[1]
        node = G.nodes[dst]
        dx = node.loc[0] - x
        dy = node.loc[1] - y

        plt.arrow(x, y, dx, dy, width = 0.00005, shape = 'full', color = 'g', length_includes_head = True)
        plt.annotate(str(G.edges[src][dst]), (x, y), (x + dx/2, y + dy/2), fontsize = 4)

plt.show()