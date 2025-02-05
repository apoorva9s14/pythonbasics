from typing import List, Set

def find_all_subsets (nums: List[int]) -> List [List[int]]: 
    res = []
    backtrack (nums, [], set(), res)
    return res
def backtrack (nums: List[int], candidate: List[int], res: List[List[int]]) -> None:
    
    for i in range(nums):
        if i==0:
            candidate.append([])
        candidate.remove(nums[i-1])
        candidate.append(nums[i])



print(find_all_subsets([4,5,6]))