import json
import math


def ListToDict(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


class TagHeap:

    def __init__(self, leangth):
        self.min = -1
        self.values = [math.inf] * leangth

    def getMin(self):
        if self.min == -1:
            return None
        else:
            return self.values[self.min]

    def relax(self, val, ind):
        if self.values[ind] > val:
            self.values[ind] = val
            if val < self.getMin():
                self.min = val


class Geolocation:
    def __init__(self, x, y, z):
        self.x = x; self.y = y; self.z = z


class Node:
    def __init__(self, id, loc):
        self.key = id
        self.tag = 0
        self.geolocation = loc


class Edge:
    def __init__(self, src, dst, w):
        self.src = src
        self.dst = dst
        self.weight = w
        self.tag = dst


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


class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}

    def add(self, node):
        self.nodes[node.key] = node
        self.edges[node.key] = {}

    def connect(self, src, dest, w):
        if src in self.nodes.keys() and dest in self.nodes.keys():
            self.edges[src][dest] = w

    def save_to_json(self, file):
        with open(file, 'w') as f:
            json.dump(self, indent=2, fp=f, default=lambda a: a.__dict__)

    def load_from_json(self, file):
        dict = {}

        with open(file, "r") as f:
            dict = json.load(f)

        for n in dict["nodes"].values():
            self.add_node(n["id"], (n['pos']['x'], n['pos']['y']))

        for src, out in dict["edges"].items():
            for dest, w in out.items():
                print(src, dest, w)
                self.connect(int(src), int(dest), w)

    def __str__(self) -> str:
        return f"nodes: {self.nodes}\nedges: {self.edges}"

    def NodeIter(self):
        return iter(self.nodes)

    def NodeNum(self):
        return len(self.nodes)

    def isConnected(self):
        return self.DFS() and self.transpose().DFS()

    def transpose(self):
        g = Graph()
        it = self.getNodesItr()

        for node in it:
            g.add(node)

            edges = self.edges[node.key]

            for dst in edges.keys():
                g.connect(node.key, dst, edges[dst])

    def DFS(self):
        if self.NodeNum() < 2:
            return True

        self.cleerTags()

        stack = [iter(self.nodes).__next__()]
        nodesReached = 0

        while len(stack) > 0:
            node = stack.pop(0)
            nodesReached +=1

            if node.tag != 1:
                edges = self.edges[node.key]
                for edge in edges.keys:
                    stack.insert(0, self.nodes[edge])

            node.tag = 1

        return nodesReached == self.NodeNum()

    def clearTags(self):
        it = self.getNodesItr()
        for node in it:
            if node is not None:
                node.tag = 0