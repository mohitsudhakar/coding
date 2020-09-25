"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns
the node at index.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class XORLinkedList:
    def __init__(self):
        self.head = self.tail = None


if __name__ == '__main__':

    ll = XORLinkedList()
