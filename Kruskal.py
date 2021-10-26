from UnionFind import UnionFind

class Edge:
    def __init__(self, *args) -> None:
        self.start, self.end, self.cost = args

class Graph:
    def __init__(self, nodes) -> None:
        self.graph: list[Edge] = []
        self.node: int = nodes
    
    def add_edge(self, start: int, end: int, cost: int) -> None:
        edge: Edge = Edge(start, end, cost)
        self.graph.append(edge)
    
    def kruskals_mst(self) -> int:
        uf: UnionFind = UnionFind(self.nodes)
        self.graph.sort(key=lambda x: x.cost)
        total_cost: int = 0
        for edge in self.graph:
            if uf.union(edge.start, edge.end):
                total_cost += edge.cost
        return total_cost

if __name__ == '__main__':
    graph: Graph = Graph(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)
    print(graph.kruskals_mst())
