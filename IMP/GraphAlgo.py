import json
import math

from IMP.Classes import DiGraph, Path, TagHeap


def permutator(elements):
    if len(elements) <= 1:
        yield elements

    else:
        for perm in permutator(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


class GraphAlgo:

    def __init__(self, G: DiGraph = DiGraph()):
        self.graph = G

    def get_graph(self):
        return self.graph

    def save_to_json(self, file):
        with open(file, 'w') as f:
            json.dump(self.graph, indent=2, fp=f, default=lambda a: a.__dict__)

    def load_from_json(self, file):
        dict = {}

        with open(file, "r") as f:
            dict = json.load(f)

        for n in dict["Nodes"]:
            self.graph.add_node(int(n['id']), tuple(map(lambda x: float(x), n['pos'].split(','))))

        for e in dict["Edges"]:
            self.graph.add_edge(int(e['src']), int(e['dest']), float(e['w']))

    def isConnected(self):
        return self.DFS() and self.transpose().DFS()

    def transpose(self):
        g = DiGraph()

        for node in self.graph.nodes.values():
            g.add_node(node.key, node.loc)

            edges = self.graph.edges[node.key]

            for dst in edges.keys():
                g.add_edge(dst, node.key, edges[dst])

        return GraphAlgo(g)

    def clearTags(self):
        for node in self.graph.nodes.values():
            if node is not None:
                node.tag = 0

    def ArbitraryNode(self):
        return iter(self.graph.nodes).__next__()

    def DFS(self):
        if self.graph.v_size() < 2:
            return True

        self.clearTags()

        stack = [self.ArbitraryNode()]
        nodesReached = 0

        while len(stack) > 0:
            node = self.graph.nodes[stack.pop(0)]
            nodesReached += 1

            if node.tag != 2:
                edges = self.graph.edges[node.key]
                for dst in edges.keys():
                    if self.graph.nodes[dst].tag == 0:
                        stack.insert(0, dst)
                        self.graph.nodes[dst].tag = 1

            node.tag = 2

        return nodesReached == self.graph.v_size()

    def dijkstra(self, src, dst):
        if not (self.graph.nodes[src] and self.graph.nodes[dst]):
            return None

        self.clearTags()

        prevs = [node.key for node in self.graph.nodes.values()]
        dists = TagHeap(self.graph.v_size(), self.graph)
        dists.min = src
        dists.values[src] = 0
        finished = False

        while not finished:
            edges = self.graph.edges[dists.min]

            curr = dists.min
            change = False
            for edge in edges.keys():
                relaxed = dists.relax(dists.get(curr) + edges[edge], edge)
                change = change or relaxed

                if relaxed:
                    prevs[edge] = curr

            dists.update_chosen(curr)
            if dists.min == -1:
                break

            if not change:
                finished = True

        if dists.get(dst) == math.inf:
            return None

        if src == dst:
            path = Path(self.graph)
            path.add(src)
            return path, dists.values

        path = Path(self.graph)
        curr = dst
        while curr is not src:
            path.add(curr)
            curr = prevs[curr]
        path.add(src)

        return path, dists.values

    def shortest_path(self, src, dst):
        path, dists = self.dijkstra(src, dst)
        return dists, path

    def centerPoint(self):

        if self.graph.v_size() == 0:
            return None

        ind = self.graph.nodes[self.ArbitraryNode()].key
        minMax = math.inf

        if not self.isConnected():
            return tuple(ind, minMax)

        it = self.graph.get_all_v().keys()
        for node in it:

            path, dists = self.dijkstra(node, node)
            Max = max(dists)

            if Max < minMax:
                minMax = Max
                ind = node

        return ind, minMax

    def TSP(self, destinations):
        if len(destinations) < 2:
            return destinations

        # trying all possible options before giving up
        rout = Path()
        possible = True
        for perm in permutator(list(range(len(destinations)))):

            i = 0
            while i < len(perm) + 1:
                path, dists = self.dijkstra(destinations[perm[i]], destinations[perm[i + 1]])

                if path is not None and dists is not math.inf:
                    rout.remove(last=True)
                    rout.merge(path)
                else:
                    possible = False
                    break

                i += 2

        if possible:
            return tuple(rout.rout, rout.weight)
