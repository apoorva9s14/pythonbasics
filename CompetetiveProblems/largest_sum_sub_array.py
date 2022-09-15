"""
Find the largest sum possible of the contiguous subarray. 
"""


def find_largest_sum(nums):
    max_till_now = float('-inf')
    max_sum = 0
    for each in nums:
        max_sum += each
        if max_till_now < max_sum:
            max_till_now = max_sum
        if max_sum < 0:
            max_sum = 0
    return max_till_now

print(find_largest_sum([-2, -3, 4, -1, -2, 1, 5, -3]))