########## VERY SLOW ##############
# class Solution:
#     def twoSum(self, nums, target: int):
#         for i in nums:
#             if target-i in nums[:nums.index(i)] + nums[nums.index(i)+1:]:
#                 if i == target-i :
#                     ind = nums.index(i)
#                     return ind , (nums[:ind]+nums[ind+1:]).index(i) + 1
#                 return nums.index(i), nums.index(target-i)
class Solution:
    def twoSum(self, nums, target: int):
        for ind, i in enumerate(nums):
            if target-i in nums[:ind] + nums[ind+1:]:
                if i == target-i :
                    return ind , (nums[:ind]+nums[ind+1:]).index(i) + 1
                return ind, nums.index(target-i)

s = Solution()
print(s.twoSum([3,2,4],6))