import json
import math


def ListToDict(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


class TagHeap:

    def __init__(self, size):
        self.min = -1
        self.values = [math.inf] * size

    def getMin(self):
        if self.min == -1:
            return None
        else:
            return self.values[self.min]

    def get(self, ind):
        return self.values[ind]

    def relax(self, val, ind):

        if self.values[ind] > val:
            self.values[ind] = val

            if val < self.getMin():
                self.min = val

            return True

        return False


class Node:
    def __init__(self, id, loc : tuple):
        self.key = id
        self.tag = 0
        self.loc = loc


class Path:
    def __init__(self):
        self.rout = []
        self.weight = 0

    def getLeangth(self):
        return len(self.rout)

    def add(self, edge):
        self.rout.insert(0, edge)
        self.weight += edge.weight

    def remove(self):
        t = self.rout.pop(0)
        self.weight -= t.weight


class GraphInterface:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def add_node(self, node):
        self.nodes[node.key] = node
        self.edges[node.key] = {}
        self.mc +=1

    def add_edge(self, src, dest, w):
        if src in self.nodes.keys() and dest in self.nodes.keys():
            self.edges[src][dest] = w
            self.mc += 1

    def remove_node(self, id):
        if id in self.nodes.keys():
            self.nodes.pop(id)
            self.edges.pop(id)
            self.mc +=1
            return True

        return False

    def remove_edge(self, src, dst):
        if src in self.edges:
            if dst in self.edges[src]:
                self.edges[src].pop(dst)
                self.mc +=1
                return True

        return False

    def __str__(self) -> str:
        return f"nodes: {self.nodes}\nedges: {self.edges}"

    def v_size(self):
        return len(self.nodes)

    def e_size(self):
        sum = 0
        for dsts in self.edges:
            sum += len(dsts)
        return sum

    def get_all_v(self):
        return self.nodes

    def all_out_edges_of_node(self, id):
        return self.edges[id]

    def all_in_edges_of_node(self, id):
        {src : src[id] for src in self.edges if id in src}

    def get_mc(self):
        return self.mc
