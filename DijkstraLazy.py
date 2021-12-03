from heapq import heapify, heappush, heappop


class Edge:
    def __init__(self, *args):
        self._from, self.to, self.cost = args

class Graph:
    def __init__(self, nodes):
        self.graph = [[] for _ in range(nodes)]
        self.nodes = nodes

    def add_edge(self, *args):
        edge = Edge(*args)
        self.graph[args[0]].append(edge)
    
    def reconstruct_path(self, start, end):
        path = []
        dist, prev = self.dijkstra_eager_adjacency_list(start)
        if dist[end] == float('inf'):
            return path
        while end:
            path.append(end)
            end = prev[end]
        return path[::-1]
    
    def dijkstra_eager_adjacency_list(self, start):
        visited = [False] * self.nodes
        prev = [None] * self.nodes
        dist = [float('inf')] * self.nodes
        dist[0] = 0
        pq = [(0, start)]
        heapify(pq)

        while pq:
            min_value, index = heappop(pq)
            visited[index] = True
            if dist[index] < min_value:
                continue
            for edge in self.graph[index]:
                if visited[edge.to]:
                    continue
                new_dist = dist[index] + edge.cost
                if new_dist < dist[edge.to]:
                    prev[edge.to] = index
                    dist[edge.to] = new_dist
                    heappush(pq, (dist[edge.to], edge.to))
    
        return dist, prev

if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 1, 2)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 4, 3)
    path = graph.reconstruct_path(0, 4)
    print(path)
