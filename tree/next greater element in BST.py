class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root
        self.found = False

    def getNextGreater(self, root, val, res):

        if not root:
            return

        self.getNextGreater(root.left, val,res)

        if self.found:
            res.append(root.val)
            return
        if root.val == val:
            self.found = True

        self.getNextGreater(root.right, val,res)

if __name__ == '__main__':

    root = Node(15, Node(10, Node(8), Node(12)), Node(20, Node(17), Node(25)))
    tree = Tree(root)
    res = []
    found = False
    tree.getNextGreater(root, 8,res)
    print(res[0])