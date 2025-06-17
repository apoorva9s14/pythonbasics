"""
Find the longest chain of consecutive numbers in an array. Two numbers are consecutive if
they have a difference of 1.
Example:
Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
Output: 4
Explanation: The longest chain of consecutive numbers is 5, 6, 7, 8.
"""
from typing import List

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    # time complexity is O(n)+O(n)
    if not nums:
        return 0
    nums_set = set(nums)
    max_chain_value = 0
    for i in nums_set:
        print(i)
        if i-1 not in nums_set:
            chain_value = 1
            j = i
            while j+1 in nums_set:
                print(j+1)
                chain_value +=1
                j=j+1
        max_chain_value=max(max_chain_value,chain_value)
        # print(i, max_chain_value)
    return max_chain_value

print(longest_chain_of_consecutive_numbers([1, 6, 2, 5, 8, 7, 10, 3]))