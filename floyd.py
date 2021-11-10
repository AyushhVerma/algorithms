class Graph:
    def __init__(self, nodes):
        self.dp = [[0 if i == j else float('inf') for i in range(nodes)] for j in range(nodes)]
        self.nodes = nodes

    def add_edge(self, start, end, cost):
        self.dp[start][end] = cost
    
    def all_pair_shortest_path_floyd_warshall(self):
        for k in range(self.nodes):
            for i in range(self.nodes):
                for j in range(self.nodes):
                    if self.dp[i][j] > self.dp[i][k] + self.dp[k][j]:
                        self.dp[i][j] = self.dp[i][k] + self.dp[k][j]
        return self.dp
