class Graph:
    def __init__(self, nodes):
        self.dp = [[0 if i == j else float('inf') for i in range(nodes)] for j in range(nodes)]
        self.nodes = nodes

    def add_edge(self, _from, to, cost):
        self.dp[_from][to] = cost
    
    def all_pair_shortest_path_floyd_warshall(self):
        for k in range(self.nodes):
            for i in range(self.nodes):
                for j in range(self.nodes):
                    if self.dp[i][j] > self.dp[i][k] + self.dp[k][j]:
                        self.dp[i][j] = self.dp[i][k] + self.dp[k][j]
        return self.dp

    def reconstruct(self):
        ...

if __name__ == '__main__':
    graph = Graph(7)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 5)
    graph.add_edge(0, 6, 10)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 4, 11)
    graph.add_edge(2, 6, 2)
    graph.add_edge(6, 5, 11)
    graph.add_edge(4, 5, 1)
    graph.add_edge(5, 4, -2)
