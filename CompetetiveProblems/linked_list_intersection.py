# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        hA = headA
        hB = headB
        
        while hA!=hB:
            hA = headB if not hA else hA.next
            hB = headA if not hB else hB.next
        
        return hA