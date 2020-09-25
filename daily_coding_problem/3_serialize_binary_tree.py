"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree
into a string, and deserialize(s), which deserializes the string back into the tree.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # consider storing in arr
    # if root is at index i
    # then left child is at 2i+1, 2i+2
    # level order traversal
    if not root:
        return []
    q = [root]
    arr = []
    while q:
        level = []
        while q:
            top = q.pop(0)
            if top:
                level.append(top)
                arr.append(str(top.val))
            else:
                arr.append("None")
        for node in level:
            q.append(node.left)
            q.append(node.right)

    return " ".join(arr)

def deserialize(arr):
    if not arr:
        return None

    arr = arr.split(" ")

    root = TreeNode(arr[0])
    i = 0
    q = [root]
    while i < len(arr) and q:
        node = q.pop(0)
        if 2*i+1 < len(arr):
            left = arr[2*i+1]
            if left != "None":
                node.left = TreeNode(left)
                q.append(node.left)
        if 2*i+2 < len(arr):
            right = arr[2*i+2]
            if right != "None":
                node.right = TreeNode(right)
                q.append(node.right)
        i += 1

    return root

if __name__ == '__main__':

    node = TreeNode('root', TreeNode('left', TreeNode('left.left'), None), TreeNode('right', None, TreeNode('right.right')))

    assert deserialize(serialize(node)).left.left.val == 'left.left'
    assert deserialize(serialize(node)).left.val == 'left'
    assert deserialize(serialize(node)).right.right.val == 'right.right'