from typing import List
# brute force
def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return[i,j]
    return []
print(pair_sum_sorted([-5, -2, 3, 4, 6],7))

# Two pointer approach
# left pointer at 0, right pointer at n-1
# sum up to values, when sum< target, increment left pointer
# when sum greater than target, decrement right pointer
def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    n=len(nums)
    l = 0
    r = n-1
    while l!=r:
        if nums[l]+nums[r]< target:
            l=l+1
        elif nums[l]+nums[r]>target:
            r=r-1
        elif nums[l]+nums[r]==target:
            return [l,r]
    return []
print(pair_sum_sorted([-5, -2, 3, 4, 6],7))