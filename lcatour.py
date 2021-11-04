tour_index = 0
import math
def tour(root, depth, depths, nodes, last):
    def visit(node, depth):
        global tour_index
        depths.append(depth)
        nodes.append(node.index)
        last[node.index] = tour_index
        tour_index += 1

    visit(root, depth)

    for child in root.children:
        tour(child, depth+1, depths, nodes, last)
        visit(root, depth)
    
    return depths, nodes, last

class SparseTree:
    def __init__(self, arr):
        self.arr = arr
        self.k = math.floor(math.log2(len(arr)))
        self.logs = [0] * (len(arr) + 1)
        self.dp = [[0] * len(arr) for _ in range(self.k+1)]
        self.init()
    
    def init(self):
        n = len(self.arr)
        for i in range(2, n):
            self.logs[i] = self.logs[i//2] + 1
        
        for i in range(n):
            self.dp[0][i] = self.arr[i]
        
        for j in range(1, self.k+1):
            for i in range(n):
                if i + (1 << j) > n:
                    break
                self.dp[j][i] = min(self.dp[j-1][i], self.dp[j-1][i+(1<<(j-1))])
    
    def rmq(self, l, r):
        n = len(self.arr)
        l = max(0, l)
        r = min(n-1, r)
        p = self.logs[r - l + 1]
        return min(self.dp[p][l], self.dp[p][r-(1<<p)+1])

class TreeNode:
    def __init__(self, index):
        self.index = index
        self.children = []


def main():
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    root.children += [node1, node2]
    node1.children += [node3, node4]
    depths, nodes, last = tour(root, 0, [], [], [0] * 5)
    l_q, r_q = 4, 2
    l, r = min(last[l_q], last[r_q]), max(last[l_q], last[r_q])
    st = SparseTree(depths)
    idx = st.rmq(l, r)
    print(nodes[idx])


main()
