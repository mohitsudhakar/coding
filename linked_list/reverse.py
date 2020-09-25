
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse(head):
    """
    1->2->3->4

    """
    prev = None
    node = head
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    head = prev
    return head

def printLL(head):
    node = head
    while node:
        print(node.val)
        node = node.next

if __name__ == '__main__':

    ll = Node(1, Node(2, Node(3, Node(4))))
    ll = reverse(ll)
    printLL(ll)
