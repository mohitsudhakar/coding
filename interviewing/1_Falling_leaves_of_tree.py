"""
Given a tree print the falling leaves of tree
    a
   / \
  b   c
 / \
d   e

Print out [ [d,e,c], [b], [a] ]
"""
import collections


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getDistFromBottom(root, distFromBottom, nodesDistance):
    if not root:
        return 0
    if root and not root.left and not root.right:
        nodesDistance[1].append(root.val)
        return 1

    left = getDistFromBottom(root.left, distFromBottom, nodesDistance)
    right = getDistFromBottom(root.right, distFromBottom, nodesDistance)

    distFromBottom = 1 + max(left, right)
    nodesDistance[distFromBottom].append(root.val)
    return distFromBottom


def printFallingLeaves(root):
    nodesDistance = collections.defaultdict(list)
    getDistFromBottom(root, 0, nodesDistance)
    result = []
    for dist in nodesDistance:
        result.append(nodesDistance[dist])
    return result

if __name__ == '__main__':

    tree_root = Node('a', Node('b', Node('d'), Node('e')), Node('c'))
    res = printFallingLeaves(tree_root)
    print(res)