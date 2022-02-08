class BIT:
    """construction can be done in O(n)"""
    def __init__(self, n):
        self.n = n
        self.ft = [0 for i in range(0, n)]

    def update(self, i, val):
        """update data in index i in O(log n)"""
        while i < self.n:
            self.ft[i] += val
            i += i & (-i)

    def query(self, i): 
        """query cumulative data from index 0 to i in O(log n)"""
        res = 0
        while i > 0:
            res += self.ft[i]
            i -= i & (-i)
        return res
