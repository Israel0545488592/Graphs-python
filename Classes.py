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

class Path:
    def __init__(self):
        self.rout = []
        self.weight = 0

    def getLeangth(self):
        return len(self.rout)

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
        self.freeMemmory.insert(0, self.nodes.pop(id).key)
        self.size -=1

class Edges:
    def __init__(self):
        self.edges = []
        self.size = 0

    def addEdge(self, edge):
        self.edges[edge.src].insert(edge) #we need to figure out a data
                                          #structure for it
        self.size +=1

class Graph:
    def __init__(self):
        self.vertecies = Vertecies()
        self.edges = Edges()

