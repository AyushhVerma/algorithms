class Graph:
    def __init__(self, nodes):
        self.graph = [[] for _ in range(nodes)]
        self.nodes = nodes
        self.visited = [False] * self.nodes
        
    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)

    def dfs(self, start, stack=[]):
        stack.append(start)
        self.visited[start] = True
        for to in self.graph[start]:
            if not self.visited[to]:
                self.dfs(to, stack)
        return stack
