class Tree:
    def __init__(self, nodes) -> None:
        """
        [[]] -> # of nodes provided
        collections.defaultdict(list) -> # of nodes not provided
        """
        self.tree = [[] for _ in range(nodes)]
        self.nodes = nodes
    
    def add_node(self, _from, to):
        self.tree[_from].append(to)
        self.tree[to].append(_from)
    
    def find_center_s(self):
        degrees = [0] * self.nodes
        leaves = []

        for i in range(self.nodes):
            degrees[i] = len(self.tree[i])
            if degrees[i] <= 1:
                leaves.append(i)
                degrees[i] = 0
        processed_nodes = len(leaves)

        while processed_nodes < self.nodes:
            new_leaves = []
            for node in leaves:
                for neighbor in self.tree[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        new_leaves.append(neighbor)
                degrees[node] = 0
            processed_nodes += len(new_leaves)
            leaves = new_leaves
        return leaves

if __name__ == '__main__':
    graph = Tree(9)
    graph.add_node(0, 1)
    graph.add_node(2, 1)
    graph.add_node(2, 3)
    graph.add_node(3, 4)
    graph.add_node(5, 3)
    graph.add_node(2, 6)
    graph.add_node(6, 7)
    graph.add_node(6, 8)
    print(f"List of centers: {graph.find_center_s()}")
