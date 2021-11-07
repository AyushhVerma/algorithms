class ArticulationPoints:
    def __init__(self, nodes) -> None:
        self.graph = [[] for _ in range(nodes)]
        self.nodes = nodes
        self.root_out_node_count = 0
    
    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)
    
    def is_articulation_point(self):
        visited = [False] * self.nodes
        low_link = [0] * self.nodes
        ids = [0] * self.nodes
        is_art_point = [False] * self.nodes

        def dfs(root, at, parent, node_id):
            if parent == root:
                self.root_out_node_count += 1
            visited[at] = True
            low_link[at] = ids[at] = node_id
            for to in list(self.graph[at]):
                if parent == to:
                    continue
                if not visited[to]:
                    dfs(root, to, at, node_id+1)
                    low_link[at] = min(low_link[at], low_link[to])
                    if ids[at] <= low_link[to]:
                        is_art_point[at] = True
                else:
                    low_link[at] = min(low_link[at], ids[to])

        
        for i in range(self.nodes):
            if not visited[i]:
                self.root_out_node_count = 0
                dfs(i, i, -1, 0)
                is_art_point[i] = self.root_out_node_count > 1
        
        return is_art_point


def main():
    graph = ArticulationPoints(9)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(2, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 7)
    graph.add_edge(7, 8)
    graph.add_edge(8, 5)
    print(graph.is_articulation_point())

main()
