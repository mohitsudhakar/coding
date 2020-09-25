"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def fn(root):
    if not root:
        return 0
    if root and not root.left and not root.right:
        return 1

    left = fn(root.left)
    right = fn(root.right)

    if root.val == root.left.val == root.right.val:
        return left + right + 1
    return left + right

if __name__ == '__main__':

    rt = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(fn(rt))