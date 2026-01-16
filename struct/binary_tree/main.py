class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# In Order DFS: Left, Root, Right


def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data, end=' ')
    in_order_dfs(node.right)

# Pre Order DFS: Root, Left, Right


def pre_order_dfs(node):
    if node is None:
        return
    print(node.data, end=' ')
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

# Post Order DFS: Left, Right, Root


def post_order_dfs(node):
    if node is None:
        return
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)
    print(node.data, end=' ')
