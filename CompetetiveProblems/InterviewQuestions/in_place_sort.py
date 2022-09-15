"""
1. Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

2. Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you       can see ordered from top to bottom.
https://assets.leetcode.com/uploads/2021/02/14/tree.jpg
"""

# l = [1,1,0,2,1,2,0,0,2]

# [0,0,0,1,1,1,2,2,2]
# [0,0,0,1,1,1,2,2,2]
# [0,0,0,1,1,1,2,2,2]
# 0 - 2
# 2 - 2
# 0 - 4
# 0 - 5
# [1,1,1,2,0,2,0,0,2]
# [1,1,1,2,2,2,0,0,0]
# [0,0,0,1,1,1,2,2,2]

# [0,1,2,0,0,0]


# def sort_objects(l):
#     n = len(l)
#     left_ptr = 0
#     right_ptr = n-3
#     swap_ptr = 0
#     cur_ptr = 0
#     while cur_ptr <= right_ptr:
#         if l[cur_ptr] == 0:
#             cur_ptr += 1
#             continue
#         else:
#             swap_ptr = cur_ptr
#             swap_val = l[cur_ptr]
#             while l[swap_ptr-1] != 0:
#                 swap_ptr += 1
#             l[swap_ptr] = swap_val
#             l[cur_ptr] = 0
#             cur_ptr += 1
        
#     return l
    
# def sort_objects_new(l):
#     n = len(l)
    
#     right_ptr = n-1
#     left_ptr = right_ptr - 3
#     swap_ptr = 0
#     cur_ptr = right_ptr
    
#     while left_ptr<cur_ptr<=right_ptr:
#         if l[cur_ptr] == 2:
#             cur_ptr -= 1
#             continue
#         else:
#             swap_ptr = cur_ptr
#             while l[swap_ptr -1] != 2:
#                 swap_ptr -= 1
#             l[swap_ptr] = l[cur_ptr]
#             l[cur_ptr] = 2
#             cur_ptr -= 1
            
#     return l
print(sort_objects_new(sort_objects([1,1,1,2,0,2,0,0,2])))  
