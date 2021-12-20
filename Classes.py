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

    def get(self, key):
        if key < 0 or key > len(self.nodes):
            return None

        return self.nodes[key]

    def getItr(self):
        return iter(self.nodes)

    def getFirst(self):
        i = 0
        while i < len(self.nodes):
            if self.nodes[i] is not None:
                return self.nodes[i]

        return None

class Edges:
    def __init__(self):
        self.edges = []
        self.size = 0

    def addEdge(self, edge):
        self.edges[edge.src].add(edge)
        self.size +=1

    def rmeove(self, src, dst):
        if len(self.edges) >= src:
            return

        return self.edges[src].remove(dst)

    def getItr(self):
        return iter(self.edges)

    def getItr(self, src):
        if self.edges[src] is None:
            return None

        return iter(self.edges[src])

class Graph:
    def __init__(self):
        self.vertecies = Vertecies()
        self.edges = Edges()

    def add(self, node):
        self.vertecies.addNode(node)

    def getNode(self, key):
        return self.vertecies.g

    def connect(self, src, dst, w):
        Edges.addEdge(Edge(src, dst, w))

    def NodeNum(self):
        return self.vertecies.size

    def EdgeNum(self):
        return self.edges.size

    def remove(self, id):
        return self.vertecies.removeNode(id)

    def disConnect(self, src, dst):
        self.edges.rmeove(src, dst)

    def getNodesItr(self):
        return self.vertecies.getItr()

    def getEdgesOf(self, src):
        return self.edges.getItr(src)

    def getEdgesItr(self):
        return self.edges.getItr()

    def isConnected(self):
        return self.DFS() and self.transpose().DFS()

    def transpose(self):
        g = Graph()
        it = self.getNodesItr()

        for node in it:
            g.add(node)

        it = self.getEdgesItr()
        for edge in it:
            g.connect(edge.src, edge.dst, edge.weight)

    def DFS(self):
        if self.NodeNum() < 2:
            return True

        stack = [self.vertecies.getFirst()]
        nodesReached = 0

        while len(stack) > 0:
            node = stack.pop(0)
            nodesReached +=1

            if node.tag != 1:
                it = self.getEdgesOf(node.key)
                for edge in it:
                    stack.insert(0, self.getNode(edge.dst))

            node.tag = 1

        return nodesReached == self.NodeNum()




