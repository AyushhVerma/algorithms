    def lazy_prims_mst(self, start: int) -> tuple[int, list[Edge]]:
        # O(E log(E))
        pq: list[Edge] = []
        heapify(pq)
        total_cost = 0
        visited: list[bool] = [False] * self.nodes
        edges: list[int] = []
        
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
