class Node:
    def __init__(self, val, key=-1):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(-1)  # dummy head
        self.MRU = None       # tail

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if self.MRU == node:
            self.MRU = node.prev if node.prev != self.head else None

        node.prev = None
        node.next = None

    def insert_mru(self, node):
        if self.MRU is None:
            self.head.next = node
            node.prev = self.head
            self.MRU = node
            return

        self.MRU.next = node
        node.prev = self.MRU
        self.MRU = node

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1

        if node != self.MRU:
            self.remove(node)
            self.insert_mru(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.val = value

            if node != self.MRU:
                self.remove(node)
                self.insert_mru(node)

            return

        if len(self.cache) == self.capacity:
            lru = self.head.next

            del self.cache[lru.key]

            self.head.next = lru.next

            if lru.next:
                lru.next.prev = self.head
            else:
                self.MRU = None

        node = Node(value, key)
        self.insert_mru(node)
        self.cache[key] = node