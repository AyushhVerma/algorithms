class Graph:
    def __init__(self, nodes):
        if nodes is None:
            assert ValueError
        self.graph = [[] for _ in range(nodes)]
        self.nodes = nodes
    
    def add_edge(self, _from, to):
        self.graph[_from].append(to)
        self.graph[to].append(_from)

    def bridges(self):
        ids = [0] * self.nodes
        low_link = [0] * self.nodes
        visited = [False] * self.nodes
        bridges = []

        def dfs(at, parent, _id=1):
            low_link[at] = ids[at] = _id
            visited[at] = True
            for to in self.graph[at]:
                if to == parent:
                    continue
                if not visited[to]:
                    dfs(to, at, _id+1)
                    low_link[at] = min(low_link[at], low_link[to])
                    if ids[at] < low_link[to]:
                        bridges.append((at, to))
                else:
                    low_link[at] = min(low_link[at], ids[to])
        
        for i in range(self.nodes):
            if not visited[i]:
                dfs(i, None)
        
        return bridges
    
    def art_points(self):
        pass

if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 4)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)
    print(f"Bridges: {graph.bridges()}")
