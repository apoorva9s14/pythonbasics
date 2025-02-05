from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    triplets=[]
    for i in range(len(nums)):
     print(nums[:i]+nums[i+1:])
     op = pair_sum_sorted(nums[:i]+nums[i+1:], 0-nums[i])
     print(op)
     if op:
        l=[nums[i]]
        l.extend(op)
        triplets.append(l)
    return triplets

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    n=len(nums)
    l = 0
    r = n-1
    while l<r:
        if nums[l]+nums[r]< target:
            l=l+1
        elif nums[l]+nums[r]>target:
            r=r-1
        elif nums[l]+nums[r]==target:
            return [nums[l],nums[r]]
    return []
print(triplet_sum([0,-1,2,-3,1]))