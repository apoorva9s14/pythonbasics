from typing import List


class Solution:
    def twoSumMySolution(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, v in enumerate(nums):
            if v in hashMap:
                hashMap[v]=[hashMap[v],i]
            hashMap[v] = i
        for i, _ in enumerate(nums):

            if target-nums[i] in hashMap:
                if type(hashMap[target-nums[i]]) == type([]):
                    l = hashMap[target-nums[i]]
                    for j in l:
                        if j!=i:
                            k=j
                else :
                    k=hashMap[target-nums[i]]
                if k == i:
                    continue
                return [i, k]
    def twoSumTwoPass(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []

s= Solution()
print(s.twoSumMySolution([2,7,11,15],9))