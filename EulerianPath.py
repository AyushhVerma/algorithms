class Edge:
    def __init__(self, start, end):
        self.start, self.end = start, end


class Graph:
    """
    Eulerian directed path
    """
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[] for _ in range(nodes)]
        self.out_degree = [0] * nodes
        self.in_degree = [0] * nodes
        self.path = []
        
    def add_directed_edge(self, start, end):
        self.graph[start].append(Edge(start, end))

    def setup(self):
        for node in self.graph:
            for edge in node:
                self.out_degree[edge.start] += 1
                self.in_degree[edge.end] += 1

    def eulerian_path_exists(self):
        if self.nodes == 0:
            return False
        self.setup()
        start_nodes = end_nodes = 0
        for i in range(self.nodes):
            if abs(self.out_degree[i] - self.in_degree[i]) > 1:
                return False
            elif self.out_degree[i] - self.in_degree[i] == 1:
                start_nodes += 1
            elif self.in_degree[i] - self.out_degree[i] == 1:
                end_nodes += 1
        return (end_nodes == 0 and start_nodes == 0) or (start_nodes == 1 and end_nodes == 1)
    
    def get_start_node(self):
        start = 0
        for i in range(self.nodes):
            if self.out_degree[i] - self.in_degree[i] > 1:
                return i
            if self.out_degree[i] > 0:
                start = i
            return start

    def eulerian_path(self):
        if not self.eulerian_path_exists():
            return
        
        def dfs(at):
            while self.out_degree[at] != 0:
                self.out_degree[at] -= 1
                next_edge = self.graph[at][self.out_degree[at]]
                dfs(next_edge.end)
            self.path.insert(0, at)
        dfs(self.get_start_node())
        return self.path if len(self.path) == self.nodes + 1 else None

if __name__ == '__main__':
    graph = Graph(5)
    graph.add_directed_edge(0, 1)
    graph.add_directed_edge(1, 2)
    graph.add_directed_edge(2, 1)
    graph.add_directed_edge(1, 3)
    graph.add_directed_edge(3, 4)
    print(graph.eulerian_path())
