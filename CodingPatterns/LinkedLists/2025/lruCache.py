# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = []
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         for i in range(len(self.cache)):
#             if self.cache[i][0] == key:
#                 tmp = self.cache.pop(i)
#                 self.cache.append(tmp)
#                 return tmp[1]
#         return -1

#     def put(self, key: int, value: int) -> None:
#         for i in range(len(self.cache)):
#             if self.cache[i][0] == key:
#                 tmp = self.cache.pop(i)
#                 tmp[1] = value
#                 self.cache.append(tmp)
#                 return

#         if self.capacity == len(self.cache):
#             self.cache.pop(0)
            
#         self.cache.append([key, value])

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.lrucache_keys=dict()
#         self.lrucache=[None]*self.capacity

#     def get(self, key: int) -> int:
#         if key in self.lrucache_keys:
#             if len(self.lrucache) == self.capacity:
#                 self.lrucache.remove(self.lrucache[0])
#             self.lrucache.append(key)
                
#         return self.lrucache_keys.get(key,-1)

#     def put(self, key: int, value: int) -> None:
#         if key in self.lrucache_keys:
#             self.lrucache_keys[key]=value
#         else:
#             if len(self.lrucache) < self.capacity:
#                 self.lrucache_keys[key]=value
#             else:
#                 self.lrucache.remove(self.lrucache[0])
#             self.lrucache.append(key)
from collections import OrderedDict
class LRUCacheOrderedDict:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache = OrderedDict()
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    def put(self,key,value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used item
            self.cache.popitem(last=False)

        self.cache[key] = value
    
lru = LRUCacheOrderedDict(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # returns 1
lru.put(3, 3)      # evicts key 2
print(lru.get(2))  # returns -1 (not found)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")
    def remove(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                # If it's the head node
                if curr.prev is None:
                    self.head = curr.next
                    if self.head:
                        self.head.prev = None
                else:
                    if curr.next:
                        curr.next.prev = curr.prev
                return True  # Successfully removed
            curr = curr.next
        return False

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCacheDoublyLinkedList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from list."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add(self, node):
        """Add node right after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove LRU from tail
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
