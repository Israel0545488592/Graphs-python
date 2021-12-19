import math

class TagMap:
    def __init__(self):
        self.values = []
        self.freeMemory = [0]

    def get(self, tag):
        if tag < 0 or tag > len(self.values):
            return None
        return self.values

    def add(self, val):
        val.tag = self.freeMemmory[0]
        self.freeMemmory.pop(0)
        if len(self.freeMemmory) == 0:
            self.freeMemmory.insert(0, len(self.values))
            self.nodes.append(val)
        else:
            self.values.insert(val.tag, val)

    def remove(self, tag):
        t = self.values[tag]
        self.values[tag] = None
        self.freeMemmory.insert(0, t.tag)

        return t

class DistMap( TagMap):

    def __init__(self, leangth):
        self.min = -1
        self.values = [math.inf] * leangth

    def getMin(self):
        if self.min == -1:
            return  None
        else:
            return self.values[self.min]

    def relax(self, val, ind):
        if self.values[ind] > val:
            self.values[ind] = val
            if val < self.getMin():
                self.min = val

class Geolocation:
    def __init__(self, x, y, z):
        self.x = x; self.y = y, self.z = z;

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
        self.tag = 0

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


class Vertecies:
    def __init__(self):
        self.nodes = []
        self.freeMemmory = [0]
        self.size = 0

    def addNode(self, node):
        m = "node " + node.key

        node.key = self.freeMemmory[0]
        self.freeMemmory.pop(0)
        if len(self.freeMemmory) == 0:
            self.freeMemmory.insert(0, len(self.nodes))

        self.nodes.append(node)
        print(m + "is now " + node.key)

        self.size +=1

    def removeNode(self, id):
        t = self.values[id]
        self.values[id] = None
        self.freeMemmory.insert(0, t)
        self.size -=1

class Edges:
    def __init__(self):
        self.edges = []
        self.size = 0

    def addEdge(self, edge):
        self.edges[edge.src].add(edge)
        self.size +=1

    def rmeove(self, edge):
        self.edges[edge.src].remove(edge.dst)

class Graph:
    def __init__(self):
        self.vertecies = Vertecies()
        self.edges = Edges()

    def add(self, node):
        self.vertecies.addNode(node)

    def connect(self, src, dst, w):
        Edges.addEdge(Edge(src, src, dst))

