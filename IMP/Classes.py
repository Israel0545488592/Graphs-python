import math


def ListToDict(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


class Node:
    def __init__(self, id, loc: tuple):
        self.key = id
        self.tag = 0
        self.loc = loc

    def __repr__(self):
        return "id: " + str(self.key) + ", loc: " + str(self.loc)


class DiGraph:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def add_node(self, id, pos: tuple = None):
        node = Node(id, pos)

        self.nodes[node.key] = node
        self.edges[node.key] = {}
        self.mc += 1

    def add_edge(self, src, dest, w):
        if src in self.nodes.keys() and dest in self.nodes.keys():
            self.edges[src][dest] = w
            self.mc += 1

    def remove_node(self, id):
        if id in self.nodes.keys():
            self.nodes.pop(id)
            self.edges.pop(id)
            self.mc += 1
            return True

        return False

    def remove_edge(self, src, dst):
        if src in self.edges:
            if dst in self.edges[src]:
                self.edges[src].pop(dst)
                self.mc += 1
                return True

        return False

    def __str__(self) -> str:
        return f"nodes: {self.nodes}\nedges: {self.edges}"

    def v_size(self):
        return len(self.nodes)

    def e_size(self):
        sum = 0
        for dsts in self.edges.values():
            sum += len(dsts)
        return sum

    def get_all_v(self):
        return self.nodes

    def all_out_edges_of_node(self, id):
        return self.edges[id]

    def all_in_edges_of_node(self, id):
        return {src: id for src in self.edges.keys() if id in self.edges[src]}

    def get_mc(self):
        return self.mc


class TagHeap:

    def __init__(self, size, G: DiGraph):
        self.graph = G
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

    def updateChosen(self, id):
        self.graph.nodes[id].tag = 1
        if self.min == id:

            Min = math.inf
            ind = -1
            for i in range(len(self.values)):
                if self.values[i] <= Min:
                    if self.graph.nodes[i].tag == 0:
                        Min = self.values[i]
                        ind = i

            self.min = ind


class Path:
    def __init__(self, G: DiGraph):
        self.graph = G
        self.rout = []
        self.weight = 0

    def getLeangth(self):
        return len(self.rout)

    def add(self, nod):
        self.rout.insert(0, nod)
        self.updateWeight()

    def updateWeight(self):
        l = len(self.rout)

        if l > 1:
            self.weight += self.graph.edges[1][0]

    def remove(self, last):
        if last:
            t = self.rout.pop(self.getLeangth() - 1)
        else:
            t = self.rout.pop(0)

        self.weight -= t.weight

    def merge(self, p):
        self.rout += p

    def __repr__(self):
        return self.rout.__repr__()
