from linkedListReversal import Solution, Node, printList

class ReorderSolution(Solution):
    def reorderList(self, head):
        
        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next       
        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None # Split the list into two halves
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp        
        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next    ## You can map two values to temp variables
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 # You can move two pointers to the next step at one go



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
    s= ReorderSolution()
    head = s.reorderList(head)

    print("Reversed Linked List:", end="")
    printList(head)