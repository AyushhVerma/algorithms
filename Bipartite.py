from heapq import heappop, heappush, heapify

class Edge:
    def __init__(self, *args):
        self.start, self.end, self.cost = args
    
    def __lt__(self, other):
        return self.cost < other.cost


class Graph:
    def __init__(self, nodes):
        self.graph = [[] for _ in range(nodes)]
        self.nodes = nodes
    
    def add_edge(self, start, end, cost):
        self.graph[start].append(Edge(start, end, cost))
        self.graph[end].append(Edge(end, start, cost))
    
    def lazy_prims_mst(self, start):
        # O(E log(E))
        pq = []
        heapify(pq)
        total_cost = 0
        visited = [False] * self.nodes
        edges = []
        
        def add_edges(nodeIndex):
            visited[nodeIndex] = True
            for edge in self.graph[nodeIndex]:
                if not visited[edge.end]:
                    heappush(pq, edge)
        
        add_edges(start)

        while pq and len(edges) != self.nodes - 1:
            edge = heappop(pq)
            nodeIndex = edge.end
            if visited[nodeIndex]:
                continue
            total_cost += edge.cost
            edges.append(edge)
            add_edges(nodeIndex)
        
        if len(edges) != self.nodes - 1:
            return
        
        return total_cost, edges

if __name__ == '__main__':
    graph: Graph = Graph(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)
    print(graph.lazy_prims_mst(0))
