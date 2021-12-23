import json
import math

from Classes import GraphInterface, Path, TagHeap


class GraphAlgoInterface:

    def __init__(self, G: GraphInterface):
        self.graph = G

    def save_to_json(self, file):
        with open(file, 'w') as f:
            json.dump(self.graph, indent=2, fp=f, default=lambda a: a.__dict__)

    def load_from_json(self, file):
        dict = {}

        with open(file, "r") as f:
            dict = json.load(f)

        for n in dict["nodes"].values():
            self.graph.add_node(n["id"], (n['pos']['x'], n['pos']['y']))

        for src, out in dict["edges"].items():
            for dest, w in out.items():
                print(src, dest, w)
                self.graph.add_edge(int(src), int(dest), w)

    def isConnected(self):
        return self.DFS() and self.transpose().DFS()

    def transpose(self):
        g = GraphInterface()

        for node in self.graph.nodes:
            g.add_node(node)

            edges = self.graph.edges[node.key]

            for dst in edges.keys():
                g.add_edge(node.key, dst, edges[dst])

    def clearTags(self):
        for node in self.graph.nodes:
            if node is not None:
                node.tag = 0

    def DFS(self):
        if self.graph.v_size() < 2:
            return True

        self.clearTags()

        stack = [iter(self.graph.nodes).__next__()]
        nodesReached = 0

        while len(stack) > 0:
            node = stack.pop(0)
            nodesReached += 1

            if node.tag != 1:
                edges = self.graph.edges[node.key]
                for edge in edges.keys:
                    stack.insert(0, self.graph.nodes[edge])

            node.tag = 1

        return nodesReached == self.graph.v_size()

    def dijkstra(self, src, dst):
        if not (self.graph.nodes[src] & self.graph.nodes[dst]):
            return None

        if src == dst:
            return Path()

        self.clearTags()

        prevs = [node.key for node in self.graph.nodes.values()]
        dists = TagHeap(self.graph.v_size())
        dists.min = src
        dists[src] = 0
        finished = False

        while not finished:
            edges = self.graph.edges[dists.min]

            for edge in edges.keys:
                change = not dists.relax(dists.get(edge), dists.getMin() + edges[edge])
                finished = finished or change

                if change:
                    prevs[edge] = dists.min

        if dists[dst] == math.inf:
            return None

        path = Path()
        curr = dst
        while curr is not src:
            path.add(curr)
            curr = prevs[curr]
        path.add(src)

        return path

    def shortest_path(self, src, dst):
        return self.dijkstra(src, dst)
