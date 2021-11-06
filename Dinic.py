class Edge:
    def __init__(self, _from, to, capacity):
        self._from, self.to, self.capacity, self.flow = _from, to, capacity, 0

    def remaining_capacity(self):
        return self.capacity - self.flow

    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.flow -= bottleneck


class Graph:
    def __init__(self, nodes, source, sink):
        self.graph = [[] for _ in range(nodes)]
        self.nodes = nodes
        self.source = source
        self.sink = sink
        self.level = ...

    def add_edge(self, *args):
        edge = Edge(*args)
        edge.residual = Edge(args[1], args[0], 0)
        self.graph[args[0]].append(edge)

    def dinic(self):
        if self.nodes <= 1:
            return 0
        
        INF = float('INF')
        mx_fl = 0

        def dfs(at, next_edge, flow):
            if at == self.sink:
                return flow
            num_edges = len(self.graph[at])
            while next_edge[at] < num_edges:
                edge = self.graph[at][next_edge[at]]
                cap = edge.remaining_capacity()
                if cap > 0 and self.level[edge.to] == self.level[at] + 1:
                    bottleneck = dfs(edge.to, next_edge, min(flow, cap))
                    if bottleneck > 0:
                        edge.augment(bottleneck)
                        return bottleneck
                next_edge[at] += 1
            return 0

        def bfs():
            self.level = [-1] * self.nodes
            self.level[self.source] = 0
            q = [self.source]
            while q:
                node = q.pop(0)
                for edge in self.graph[node]:
                    cap = edge.remaining_capacity()
                    if cap > 0 and self.level[edge.to] == -1:
                        self.level[edge.to] = self.level[node] + 1
                        q.append(edge.to)
            return self.level[self.sink] != -1

        while bfs():
            next_edge = [0] * self.nodes
            f = dfs(self.source, next_edge, INF)
            while f != 0:
                mx_fl += f
                f = dfs(self.source, next_edge, INF)
        return mx_fl


if __name__ == '__main__':
    graph = Graph(1, 0, 0)
    graph.add_edge(0, 1, 16)
    graph.add_edge(0, 2, 13)
    graph.add_edge(1, 2, 10)
    graph.add_edge(2, 1, 4)
    graph.add_edge(1, 3, 12)
    graph.add_edge(3, 5, 20)
    graph.add_edge(4, 3, 7)
    graph.add_edge(4, 5, 4)
    graph.add_edge(2, 4, 14)
    graph.add_edge(3, 2, 9)
    print(graph.dinic())
