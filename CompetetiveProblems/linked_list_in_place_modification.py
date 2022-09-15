"""
//
// Given a linked list
// input = 1 2 3 4 
// output = 1 4 2 3
//
// 1 2 3 9 5 6 7
//  1 7 2 6 3 5 9
1 2 3 4 5
1 7 2 6 3 5 4

"""
import math
class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
class DLL:
    def __init__(self,head=None) -> None:
        self.head = head
    def create_dll(self, inp_list=None):
        if inp_list:
            headNode = Node(data=inp_list[0])
        self.head = headNode
        prev = self.head
        for each in inp_list[1:]:
            prev.next = Node(each, prev=prev)
            prev = prev.next
    def printDLL(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def modify_dll(self):
        ## input = 1 2 3 4 
        ## output = 1 4 2 3
        prev = self.head
        
        stack = []
        while prev:
            stack.append(prev)
            prev = prev.next
        prev = self.head
        print("STACK", [each.data for each in stack], stack[math.ceil(len(stack)/2)-1].data)
        for each in stack[::-1][:math.ceil(len(stack)/2)]:
            if prev:
                temp = prev.next
                prev.next = each
                each.prev = prev
                each.next = temp
                prev = temp
                if len(stack)%2 == 0:
                    if each.data == stack[math.ceil(len(stack)/2)].data:
                        each.next = None
                else:
                    if each.data == stack[math.ceil(len(stack)/2)-1].data:
                        each.next = None
    def modify_dll_in_place(self):
        slow_ptr = 0
        fast_ptr = 0
        cur = self.head
        slow_next, fast_next = cur, cur
        while cur.next:
            slow_next = slow_next.next
            fast_next = fast_next.next.next
            if not fast_next or not fast_next.next:
                print(slow_next.data)
                return
            
            # if slow_next.data == fast_next.data:
            #     print(slow_next.prev.data)
            cur = cur.next
            





            



d = DLL()
d.create_dll([1,2, 3,4,5,6,7,8])
# 12348765
"""
1 1
2 3
3 5
4 
5
6

[1,2,3,4,5]
1 1
2 3
3 5
4 
"""
d.modify_dll_in_place()
# print(d.printDLL())
