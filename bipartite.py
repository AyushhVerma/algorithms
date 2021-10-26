def is_graph_bipartite(self) -> bool:
        seen: dict[int, int] = {}
        def dfs(at, color):
            q = [(at, color)]
            while q:
                node, color = q.pop()
                if node in seen:
                    if seen[node] != color:
                        return False
                    continue
                seen[node] = color
                for to in self.graph[node]:
                    q.append((to, -color))
            return True
        
        for i in range(self.nodes):
            if i not in seen:
                if dfs(i, 1) == False:
                    return False
        return True
