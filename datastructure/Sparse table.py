import math


class SparseTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.k = math.floor(math.log2(self.n))
        self.logs = [None] + [0] * self.n
        self.dp = [[0] * self.n for _ in range(self.k+1)]
        self.preprocessed = False
    
    def preprocess(self):
        for i in range(2, self.n+1):
            self.logs[i] = self.logs[i//2] + 1
        
        for i in range(self.n):
            self.dp[0][i] = self.arr[i]
        
        for j in range(1, self.k):
            for i in range(self.n):
                if i + (1 << j) > self.n:
                    break
                self.dp[j][i] = min(self.dp[j-1][i], self.dp[j-1][i+(1<<(j-1))])
    
    def min_query(self, l, r):
        """overlapping function minimum query"""
        l = max(0, l)
        r = min(self.n-1, r)
        if not self.preprocessed:
            self.preprocessed = True
            self.preprocess()
        
        p = self.logs[r - l + 1]
        return min(self.dp[p][l], self.dp[p][r-(1<<p)+1])


def main():
    arr = [0, 7, 5, 8, 1, 2, -5, 3]
    st = SparseTree(arr)
    print(st.min_query(2, 7))


main()
