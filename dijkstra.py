    def dijkstra_eager_adjacency_list(self, start) -> tuple[int, list[int]]:
        visited: list[bool] = [False] * self.nodes
        prev: list[int] = [None] * self.nodes
        dist: list[int] = [float('inf')] * self.nodes
        
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
