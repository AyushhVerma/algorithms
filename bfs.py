class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[] for _ in range(nodes)]
        self.visited = [False] * nodes

    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)
    
    def bfs(self, start):
        q = [start]
        nodes = []
        while q:
            node = q.pop(0)
            nodes.append(node)
            self.visited[node] = True
            for to in self.graph[node]:
                if not self.visited[to]:
                    q.append(to)
        return nodes
