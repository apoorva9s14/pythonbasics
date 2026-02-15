
class Node:
    def __init__(self, data, prev_ptr=None, next_ptr=None):
        self.data = data
        self.prev_ptr = prev_ptr
        self.next_ptr = next_ptr

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def insert_node(self, node1, node2):
        """
        Insert node2 right after node1.
        """
        if node1 is None or node2 is None:
            return False

        old_nextptr = node1.next_ptr

        # link node1 -> node2
        node1.next_ptr = node2
        node2.prev_ptr = node1

        # link node2 -> old_next
        node2.next_ptr = old_nextptr
        if old_nextptr:
            old_nextptr.prev_ptr = node2
        else:
            # node1 was tail; node2 becomes new tail
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
            # clear removed node's links (optional)
            node.prev_ptr = None
            node.next_ptr = None
            return True

        # General case: we can traverse OR use node.prev_ptr directly.
        prev = node.prev_ptr
        next_node = node.next_ptr

        # Relink previous
        if prev:
            prev.next_ptr = next_node

        # Relink next
        if next_node:
            next_node.prev_ptr = prev
        else:
            # removed tail
            self.tail = prev

        # clear removed node's links (optional)
        node.prev_ptr = None
        node.next_ptr = None
        return True

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

dll.delete_node(n2)
dll.print_linked_list()   # 1 --> 3 --> 4 --> 5
dll
