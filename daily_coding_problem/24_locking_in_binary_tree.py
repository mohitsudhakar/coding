"""
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its
descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false.
Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false.
Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program, so there is no need for actual
locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""

def check_children(root):
    if not root:
        return True

    if root.locked:
        return False

    return check_children(root.left) and check_children(root.right)

class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False
        self.num_descendants_locked = 0

    def is_locked(self):
        return self.locked

    def check(self):
        # if check_children(self):
        #     return False
        if self.num_descendants_locked > 0:
            return False

        parent = self.parent
        while parent:
            if parent.locked:
                return False
            parent = parent.parent
        return True

    def lock(self):
        # O(m+h), m is number of children, h is height
        # Worst case O(n) n is number of nodes
        # With num_descendants_locked
            # O(h) worst case
        # need to check children and ancestors for locked nodes
        if self.check():
            self.locked = True
            # update num_descendants_locked for parents
            parent = self.parent
            while parent:
                parent.num_descendants_locked += 1
                parent = parent.parent
            return True
        return False

    def unlock(self):
        # O(m+h), m is number of children, h is height
        # need to check children and ancestors for locked nodes
        if self.check():
            self.locked = False
            # update num_descendants_locked for parents
            parent = self.parent
            while parent:
                parent.num_descendants_locked -= 1
                parent = parent.parent
            return True
        return False