import collections

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def __len__(self):
        return self._size

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self._size += 1

    def remove(self, node):
        if self._size == 0:
            return
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        del node
        self._size -= 1

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}          # dict { key: Node }
        self.node_freq = {}     # dict { key: freq }
        self.freq_hash = collections.defaultdict(DLL)     # dict { freq: DLL }
        self.minfreq = 0

    def get(self, key):
        if key in self.hash:
            node = self.hash[key]
            freq = self.node_freq[key]
            dll = self.freq_hash[freq]
            dll.remove(node)
            if freq == self.minfreq and dll._size == 0:
                self.minfreq += 1

            self.node_freq[key] += 1
            freq = self.node_freq[key]
            new_dll = self.freq_hash[freq]
            new_dll.add(node)

            return node.val
        return -1

    def put(self, key, val):
        freq = 0
        if key in self.hash:
            node = self.hash[key]
            freq = self.node_freq[key]
            dll = self.freq_hash[freq]
            dll.remove(node)
        node = Node(key, val)
        self.node_freq[key] = freq+1
        new_dll = self.freq_hash[freq+1]
        new_dll.add(node)
        self.hash[key] = node
        if len(self.hash) > self.capacity:
            # find and remove head node from DLL of least freq
            min_dll = self.freq_hash[self.minfreq]
            node = min_dll.head.next
            min_dll.remove(node)
            del self.hash[node.key]
            del self.node_freq[node.key]


if __name__ == '__main__':

    cache = LFUCache(3)
    cache.put(1,1)
    cache.put(2,4)
    cache.put(3,9)
    cache.get(1)
    cache.get(2)
    cache.put(4,16)
    assert cache.get(3) == -1
