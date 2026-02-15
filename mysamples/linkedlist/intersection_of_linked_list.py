class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self,head):
        self.head = head
    
    def add_node(self,node1,node2):
        old_nextptr = node1.next
        node1.next=node2
        node2.next=old_nextptr
        
    def delete_node(self,node):
        if self.head is None or node is None:
            return False
        if node==self.head:# Removing the head node is easier as we just have to change the pointer to head
            self.head = node.next
            return
        prev = self.head
        cur = prev.next
        while cur:
            if cur == node:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next
    def print_linked_list(self):
        if self.head is None:
            print("(empty)")
            return
        print(" --> ".join(str(node.data) for node in self))

def return_intersection_of_linked_lists_bruteforce(l, l1):
    h = l.head
    
    while h:
        h1 = l1.head
        while h1:
            if h.data == h1.data:
                return h.data
            h1 = h1.next
        h = h.next
    return

def return_intersection_of_linked_lists(l, l1):
    h, h1 = l.head, l1.head
    while h != h1:
        h = h.next if h else l1.head
        h1 = h1.next if h1 else l.head
    if h:
        return h.data

n = Node(1,None)
n2 = Node(2,None)
n3 = Node(3,None)
n4 = Node(4,None)
n5 = Node(5,None)
n6 = Node(6,None)
n7 = Node(7,None)
n8 = Node(8,None)

l = LinkedList(n)
l.add_node(n,n2)
l.add_node(n2,n3)
l.add_node(n2,n4)
l.add_node(n2,n5)
l.print_linked_list()

l1 = LinkedList(n6)
l1.add_node(n6,n7)
l1.add_node(n7,n8)
# l1.add_node(n5,n3)
l1.print_linked_list()
print(return_intersection_of_linked_lists_bruteforce(l,l1))
print(return_intersection_of_linked_lists(l,l1))
