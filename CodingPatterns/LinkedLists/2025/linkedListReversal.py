# Definition for singly-linked list.
class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None
class Solution:
    def reverseList(self, head):
        cur_node = head
        prev_node = None
        while cur_node:
            
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node=next_node
        return prev_node

def printList(node):
    while node is not None:
        print(f" {node.data}", end="")
        node = node.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    printList(head)
    s= Solution()
    head = s.reverseList(head)

    print("Reversed Linked List:", end="")
    printList(head)