

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count(root):
    if not root:
        return 0
    return count(root.left) + count(root.right) + 1

def lca(root, p, q):
    if not root:
        return None
    if root.val == p.val or root.val == q.val:
        return root
    
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    if left: return left
    if right: return right
    return None

def maxDepthNode(root, depth):
    if not root:
        return None, 0
    if root and not root.left and not root.right:
        return root, depth

    left, ld = maxDepthNode(root.left, depth+1)
    right, rd = maxDepthNode(root.right, depth+1)

    if left and right:
        if ld > rd:
            return left, ld
        else:
            return right, rd
    if left:
        return left,ld
    return right, ld

if __name__ == '__main__':

    rt = Node(0, Node(1), Node(2, Node(3, Node(4), Node(5)), Node(6)))
    ct = count(rt)
    print(ct)
    node, depth = maxDepthNode(rt, 0)
    print(node.val, depth)