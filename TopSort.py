from collections import deque

class Graph:
    def __init__(self, nodes):
        self.graph = [[] for _ in range(nodes)]
        self.nodes = nodes
    
    def add_edge(self, _from, to):
        self.graph[_from].append(to)

    def topo_sort(self):
        """dfs based topoSort"""
        stack = deque()
        visited = [False] * self.nodes

        def dfs(at):
            visited[at] = True
            for to in self.graph[at]:
                if not visited[to]:
                    dfs(to)
            stack.appendleft(at)

        for i in range(self.nodes):
            if not visited[i]:
                dfs(i)
        
        return stack
    
    def kahns_algo(self):
        """bfs based topoSort"""
        ...

if __name__ == '__main__':
    graph = Graph(6)
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    print(graph.topo_sort())
