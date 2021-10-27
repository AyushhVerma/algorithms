class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(root):
    # height of the binary tree which is the number of edges from the root to the deepest leaf node
    if not root:
        return -1
    return max(tree_height(root.left), tree_height(root.right)) + 1

def tree_sum(root):
    # sum of nodes' values
    total = 0
    children = [root]
    while children:
        root = children.pop(0)
        total += root.val
        if root.left:
            children.append(root.left)
        if root.right:
            children.append(root.right)
    return total

if __name__ == '__main__':
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node0.left = node1
    node2 = TreeNode(2)
    node0.right = node2
    node3 = TreeNode(3)
    node1.left = node3
    node4 = TreeNode(4)
    node1.right = node4
    node5 = TreeNode(5)
    node2.left = node5

    print(tree_height(node0), tree_sum(node0))
