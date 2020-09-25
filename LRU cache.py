class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        ans = -1
        if key in self.hash:
            node = self.hash[key]
            self.ll_remove(node)
            self.ll_add(node)
            ans = node.val
        print(ans)
        return ans

    def put(self, key, val):
        if key in self.hash:
            node = self.hash[key]
            self.ll_remove(node)
        node = Node(key, val)
        self.ll_add(node)
        self.hash[key] = node
        if len(self.hash) > self.capacity:
            node = self.head.next
            self.ll_remove(node)
            del self.hash[node.key]

    def ll_add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def ll_remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        del node

if __name__ == '__main__':

    cache = LRUCache(3)
    cache.put(1,1)
    cache.put(2,2)
    cache.get(1)
    cache.put(3,3)
    cache.put(4,4)
    cache.get(2)
    cache.get(1)
    cache.put(5,5)
    cache.put(6,6)
    cache.get(3)