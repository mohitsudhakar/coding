"""
This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should
first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

0   3   7   -7  0   5   -1  5
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def printList(self):
        node = self
        while node:
            print(node.val)
            node = node.next

def removeConsecutiveWithZeroSum(head):

    inodes = {}
    i = 0
    node = head
    while node:
        inodes[i] = node
        i += 1
        node = node.next
    inodes[i] = None

    cumm = 0
    dic = {0:0}
    i = 0
    rem = []
    node = head
    while node:
        cumm += node.val
        if cumm in dic:
            print(cumm)
            old = dic[cumm]
            # remove from old to i
            rem.append((old, i))
        dic[cumm] = i
        node = node.next
        i += 1

    print(rem)
    for from_i, to_i in rem:
        if from_i == 0:
            head = inodes[to_i+1]
        else:
            inodes[from_i].next = inodes[to_i+1]

    return head


if __name__ == '__main__':

    node = Node(2, Node(3, Node(4, Node(-7, Node(5, Node(-6, Node(6)))))))

    node = removeConsecutiveWithZeroSum(node)

    node.printList()

