"""
Given an array arr[] of n integers and a target value, the task is to find whether there is a pair of 
elements in the array whose sum is equal to target. 
Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: true
Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.
"""


from typing import List


class SolutionMyWay:
    # Two pass solution My Way
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,j in enumerate(nums):
            if j not in d:
                d[j]=i
            else:
                d[j]=[d[j],i]
        for i in nums:
            if target-i in d:
                if type(d[target-i]) == type([]):
                    return d[target-i]
                elif i==target-i:
                    continue
                return [d[i], d[target-i]]
            
class SolutionBookWay:
    "Two pass solution given in the book"
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,j in enumerate(nums):
                d[j]=i
            
        for i,j in enumerate(nums):
            complement=target - j
            if complement in d and d[complement]!=i:
                return [i,d[complement]]
        return []
class Solution:
    "One pass solution given in the book"
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,j in enumerate(nums):
            if target-j in d and d[target-j]!=i:
                return [i, d[target-j]]
            d[j]=i
        return []
s= Solution()
print(s.pairSumUnsorted([2,7,11,15],9))