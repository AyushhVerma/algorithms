class UnionFind:
    def __init__(self, nodes):
        self.nodes = nodes
        self.roots = [i for i in range(nodes)]
        self.size = [1 for _ in range(nodes)]

    def union(self, p, q):
        root1, root2 = self.find(p), self.find(q)
        if root1 == root2:
            return
        
        if self.roots[root1] < self.roots[root2]:
            self.roots[root2] = self.roots[root1]
            self.size[root1] += self.size[root2]
            self.size[root2] = 0
        else:
            self.roots[root1] = self.roots[root2]
            self.size[root2] += self.size[root1]
            self.size[root1] = 0
        
        return True
            
    def find(self, r):
        root = r
        
        while root != self.roots[root]:
            root = self.roots[root]

        while r != root:
            new = r
            self.roots[r] = root
            r = new

        return root

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
