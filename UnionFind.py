class UnionFind:
    def __init__(self, nodes):
        self.nodes = nodes
        self.roots = [i for i in range(nodes)]
        self.size = [1 for _ in range(nodes)]

    def union(self, p, q):
        root1, root2 = self.find(p), self.find(q)
        if root1 == root2:
            return
        
        if self.size[root1] < self.size[root2]:
            self.roots[root2] = self.roots[root1]
            self.size[root1] += self.size[root2]
            self.size[root2] = 0
        else:
            self.roots[root1] = self.roots[root2]
            self.size[root2] += self.size[root1]
            self.size[root1] = 0
        
        return True
    
    @property
    def count_root(self):
        return sum(root[i] == i for i in range(self.nodes))
            
    def find(self, r):
        if r != self.roots[i]:
            self.roots[i] = self.find(self.roots[i])
        return self.roots[i]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
