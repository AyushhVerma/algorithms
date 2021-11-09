class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [None] * (4 * self.n)
        self.build(1, 0, self.n-1)
    
    def build(self, tree_index, low, high):
        if low == high:
            self.tree[tree_index] = self.arr[high]
        else:
            mid = (low + high) // 2
            self.build(2*tree_index, low, mid)
            self.build(2*tree_index+1, mid+1, high)
            # self.tree[tree_index] = max(self.tree[2*tree_index], self.tree[2*tree_index+1])
            # self.tree[tree_index] = min(self.tree[2*tree_index], self.tree[2*tree_index+1])
            self.tree[tree_index] = self.tree[2*tree_index] + self.tree[2*tree_index+1]
    
    def update(self, tree_index, low, high, arr_idx, value):
        if low == high:
            self.tree[tree_index] = value
        else:
            mid = (low + high) // 2
            if arr_idx <= mid:
                self.update(2*tree_index, low, mid, arr_idx, value)
            else:
                self.update(2*tree_index+1, mid+1, high, arr_idx, value)
            self.tree[tree_index] = max(self.tree[2*tree_index], self.tree[2*tree_index+1])
            self.tree[tree_index] = min(self.tree[2*tree_index], self.tree[2*tree_index+1])
            self.tree[tree_index] = self.tree[2*tree_index] + self.tree[2*tree_index+1]
    
    def query(self, tree_index, low, high, i, j):
        if i > j:
            # return float('-inf')
            # return float('inf')
            return 0
        if i == low and j == high:
            return self.tree[tree_index]
        mid = (low + high) // 2
        # return max(self.sum_query(2*tree_index, low, mid, i, min(j, mid)), self.sum_query(2*tree_index+1, mid+1, high, max(i, mid+1), j))
        # return min(self.sum_query(2*tree_index, low, mid, i, min(j, mid)), self.sum_query(2*tree_index+1, mid+1, high, max(i, mid+1), j))
        return self.sum_query(2*tree_index, low, mid, i, min(j, mid)) + self.sum_query(2*tree_index+1, mid+1, high, max(i, mid+1), j)


def main():
    arr = [1, 2, 3, 4, 0]
    n = len(arr)
    st = SegmentTree(arr)
    st.update(1, 0, n-1, n-1, 10)
    print(st.sum_query(1, 0, n-1, 2, n-1))


main()
