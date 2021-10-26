class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = len(graph)
        self.visited_token = 1
    
    def ford_fulkerson_max_flow(self, source, sink):
        max_flow = 0
        self.visited_token = 1
        visited = [0] * self.nodes

        def dfs(node, sink, flow):
            if node == sink:
                return flow
            cap = self.graph[node]
            visited[node] = self.visited_token
            for i in range(self.nodes):
                if visited[i] != self.visited_token and cap[i] > 0:
                    flow = min(flow, cap[i])
                    dfs_flow = dfs(i, sink, flow)
                    if dfs_flow > 0:
                        self.graph[node][i] -= dfs_flow
                        self.graph[i][node] += dfs_flow
                        return dfs_flow
            return 0
        
        while True:
            flow = dfs(source, sink, float('inf'))
            max_flow += flow
            self.visited_token += 1
            if flow == 0:
                return max_flow

if __name__ == '__main__':
    graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
    graph = Graph(graph)
    print(graph.ford_fulkerson_max_flow(0, 5))
