class UnionFind:
    def __init__(self, nodes):
        self.nodes = nodes
        self.roots = {}

    def union(self, p, q):
        root1, root2 = self.find(p), self.find(q)
        if root1 == root2:
            return
        self.roots[root2] = root1
        return True
    
    @property
    def count_root(self):
        return sum(root == node for node, root in self.roots.items())
            
    def find(self, r):
        if r != self.roots[i]:
            self.roots[i] = self.find(self.roots[i])
        return self.roots[i]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
