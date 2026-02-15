class Node:
    def __init__(self, data, prev_ptr=None, next_ptr=None):
        self.data = data
        self.prev_ptr = prev_ptr
        self.next_ptr = next_ptr

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def insert_node(self,node1,node2):
        if node1 is None or node2 is None:
            return False
        old_nextptr = node1.next_ptr
        # link node1 -> node2
        node1.next_ptr=node2
        node2.prev_ptr=node1
        # link node2 -> old_next
        node2.next_ptr=old_nextptr
        if old_nextptr:
            old_nextptr.prev_ptr = node2
        else:
            self.tail = node2
        return True
        
    def delete_node(self, node):
        if self.head is None or node is None:
            return False

        # Removing head
        if node == self.head:
            next_node = node.next_ptr
            self.head = next_node
            if next_node:
                next_node.prev_ptr = None
            else:
                # list becomes empty
                self.tail = None
            return
        prev = self.head
        cur = prev.next_ptr
        while cur:
            if cur == node:
                prev.next_ptr = cur.next_ptr
                
                if cur.next_ptr:
                    cur.next_ptr.prev_ptr = prev
                else:
                    self.tail = prev
                    return
            prev = cur
            cur = cur.next_ptr
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

    def print_reverse(self):
        cur = self.tail
        if cur is None:
            print("(empty)")
            return
        vals = []
        while cur:
            vals.append(str(cur.data))
            cur = cur.prev_ptr
        print(" <-- ".join(vals))
    
    def reverse_linked_list(self):
        if self.head is None:
            return
        prev = None
        cur = self.head
        while cur:
            old_nxt = cur.next_ptr
            cur.next_ptr = prev
            cur.prev_ptr = old_nxt
            cur = old_nxt
            prev = cur



# --------- Example usage: manual nodes + insert_node ----------
# Start with just head = n1
n1 = Node(1)
dll = DoublyLinkedList(head=n1, tail=n1)

n2 = Node(2)
dll.insert_node(n1, n2)   # 1 -> 2

n3 = Node(3)
dll.insert_node(n2, n3)   # 1 -> 2 -> 3

n4 = Node(4)
dll.insert_node(n3, n4)   # 1 -> 2 -> 3 -> 4

n5 = Node(5)
dll.insert_node(n4, n5)   # 1 -> 2 -> 3 -> 4 -> 5

dll.print_linked_list()   # 1 --> 2 --> 3 --> 4 --> 5
dll.print_reverse()       # 5 <-- 4 <-- 3 <-- 2 <-- 1

dll.reverse_linked_list()
dll.print_linked_list()
dll.delete_node(n2)
dll.print_linked_list()   # 1 --> 3 --> 4 --> 5
dll
