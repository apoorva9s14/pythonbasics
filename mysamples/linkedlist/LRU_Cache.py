class Node:
    def __init__(self,data,next_ptr):
        self.data = data
        self.next_ptr = next_ptr


class LinkedList:
    def __init__(self,head):
        self.head = head
    
    def add_node(self,node1,node2):
        old_nextptr = node1.next_ptr
        node1.next_ptr=node2
        node2.next_ptr=old_nextptr
    
    def add_node_at_end(self,node1):
        cur = self.head
        if not cur:
            self.head=node1
            return
        while cur:
            if not cur.next_ptr:
                cur.next_ptr=node1
                node1.next_ptr=None
    def add_node_at_the_beginning(self,node1):
        cur = self.head
        if not cur:
            self.head=node1
            return
        node1.next_ptr=cur
        self.head=node1
           
    def delete_node(self,node):
        if self.head is None or node is None:
            return False
        if node==self.head:# Removing the head node is easier as we just have to change the pointer to head
            self.head = node.next_ptr
            return
        prev = self.head
        cur = prev.next_ptr
        while cur:
            if cur.data == node.data:
                import pdb; pdb.set_trace()
                prev.next_ptr = cur.next_ptr
                return
            prev = cur
            cur = cur.next_ptr
    def pop(self):
        if self.head is None:
            return False
        cur = self.head
        while cur:
            prev=cur
            cur = cur.next_ptr
        prev.next_ptr = None
        return prev.data
        
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next_ptr
    def print_linked_list(self):
        if self.head is None:
            print("(empty)")
            return
        print(" --> ".join(str(node.data) for node in self))

class LRUCache:
    def __init__(self,size):
        self.lru_cache = LinkedList(None)
        self.size = size
        self.cache = {}
    def get(self,item):
        if item in self.cache:
            self.lru_cache.delete_node(Node(item,None))
            self.lru_cache.print_linked_list()
            self.lru_cache.add_node_at_the_beginning(Node(item,None))
            return self.cache.get(item)
    def put(self, item):
        #evict scenario
        if len(self.cache)>= self.size:
            data = self.lru_cache.pop()
            if data in self.cache:
                self.cache.pop(data)
        key_item = list(item.keys())[0]
        if key_item in self.cache:
            self.lru_cache.delete_node(Node(key_item,None))
        self.lru_cache.add_node_at_the_beginning(Node(key_item,None))
        self.cache.update(item)
    def print_linked_list_lru_cache(self):
        ll =self.lru_cache
        head =ll.head
        if head is None:
            print("(empty)")
            return
        print(" --> ".join(str(node.data) for node in ll))
    def print_lru_cache(self):
        print(self.cache)

lru_cache_size = 5
l = LRUCache(lru_cache_size)
l.put({1:1})
l.put({2:2})
l.put({3:3})
l.put({4:4})
l.put({5:5})
l.get(1)
l.put({6:6})

l.print_linked_list_lru_cache()
l.print_lru_cache()

