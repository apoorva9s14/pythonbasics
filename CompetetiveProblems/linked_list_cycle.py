from linked_list_python import LinkedList

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow, fast = slow.next, fast.next.next
        return True


s = Solution()
s.hasCycle(LinkedList(nodes=[3,2,0,-4]))