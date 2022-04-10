from queue import PriorityQueue
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        if not q.empty():
            val, node = q.get()
            head = ListNode(node)
        while head:
            val, node = q.get()
            head.next = node
            node = node.next
            if node:
                q.put((node))
        return head.next

s = Solution()
secondNode = ListNode(2,next=None)
firstNode = ListNode(5,next=secondNode)

fourthNode = ListNode(1,next=None)
thridNode = ListNode(8,next=fourthNode)


print(s.mergeKLists([firstNode,secondNode,thridNode, fourthNode]).val)
print(s.mergeKLists([firstNode,secondNode,thridNode, fourthNode]).next.val)
print(s.mergeKLists([firstNode,secondNode,thridNode, fourthNode]).next.next.val)
print(s.mergeKLists([firstNode,secondNode,thridNode, fourthNode]).next.next.next.val)
print(s.mergeKLists([firstNode,secondNode,thridNode, fourthNode]).next.next.next.next.val)
print(s.mergeKLists([firstNode,secondNode,thridNode, fourthNode]).next.next.next.next.next.val)
print(s.mergeKLists([firstNode,secondNode,thridNode, fourthNode]).next.next.next.next.next.next.val)



