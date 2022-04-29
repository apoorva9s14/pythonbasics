# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         nums.sort()
#         if not nums:
#             return False
#         prev = nums[0]
#         for i in nums[1:]:
#             if i == prev:
#                 return True
#             prev = i
#         return False

class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashSet = set()
        for i in nums:
            if i not in hashSet:
                hashSet.add(i)
            else:
                return True
        return False
s = Solution()
print(s.containsDuplicate([1,2,3,1]))