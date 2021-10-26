class Edge:
    def __init__(self, _from, to, capacity):
        self.residual = ...
        self._from = _from
        self.to = to
        self.capacity = capacity
        self.flow = 0

    def remaining_capacity(self):
        return self.capacity - self.flow

    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.capacity -= bottleneck

class Graph:
    def __init__(self, nodes, source, sink):
        self.graph = [[] for _ in range(nodes)]
        self.nodes = nodes
        self.visited_token = 0
        self.source = source
        self.sink = sink
    
    def add_edge(self, _from, to, capacity):
        edge1 = Edge(_from, to, capacity)
        edge1.residual = Edge(to, _from, 0)
        self.graph[_from].append(edge1)

    def f_f_e_k_m_f(self):
        visited = [None] * self.nodes
        maximum_flow = 0

        def bfs():
            queue = [self.source]
            visited[self.source] = self.visited_token
            prev = [None] * self.nodes
            
            while queue:
                node = queue.pop(0)
                if node == self.sink:
                    break
                for edge in self.graph[node]:
                    cap = edge.remaining_capacity()
                    if visited[edge.to] != self.visited_token and cap > 0:
                        visited[edge.to] = self.visited_token
                        queue.append(edge.to)
                        prev[edge.to] = edge
            
            bottleneck = float('INF')
            
            curr = prev[self.sink]
            if curr == None:
                return 0
            
            while curr:
                bottleneck = min(bottleneck, curr.remaining_capacity())
                curr = prev[curr._from] 
            curr = prev[self.sink]
            while curr:
                curr.augment(bottleneck)
                curr = prev[curr._from]
            return bottleneck
        
        while True:
            flow = bfs()
            if flow == 0:
                return maximum_flow
            self.visited_token += 1
            maximum_flow += flow

if __name__ == '__main__':
    graph = Graph(6, 0, 5)
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
    print(graph.f_f_e_k_m_f())
