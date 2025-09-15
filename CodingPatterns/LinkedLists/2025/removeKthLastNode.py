# Python code for the deleting a node from end
# in two traversal

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def deleteNthNodeFromEnd(head, k):
    fast, slow = head, head
    for i in range(k):
        fast = fast.next
    while fast.next != None:
        slow = slow.next
    slow.next = slow.next.next
    head = slow
    
    
    return slow

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = deleteNthNodeFromEnd(head, 4)

    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()