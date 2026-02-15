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
        
    def delete_node(self,node):
        if self.head is None or node is None:
            return False
        if node==self.head:# Removing the head node is easier as we just have to change the pointer to head
            self.head = node.next_ptr
            return
        prev = self.head
        cur = prev.next_ptr
        while cur:
            if cur == node:
                prev.next_ptr = cur.next_ptr
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

    def remove_nth_last_node_linked_list(self,n):
        if not self.head:
            return 
        cur,slow = self.head, self.head
        fast_ptr, slow_ptr= 0, 0
        while cur:
            if fast_ptr >= n:
                slow_ptr=slow_ptr+1
                slow = slow.next_ptr
            cur = cur.next_ptr
            fast_ptr=fast_ptr+1
        self.delete_node(slow)

n = Node(1,None)
n2 = Node(2,None)
n3 = Node(3,None)
n4 = Node(4,None)
n5 = Node(5,None)
l = LinkedList(n)
l.add_node(n,n2)
l.add_node(n2,n3)
l.add_node(n2,n4)
l.add_node(n2,n5)
l.print_linked_list()
l.remove_nth_last_node_linked_list(4)
l.print_linked_list()

