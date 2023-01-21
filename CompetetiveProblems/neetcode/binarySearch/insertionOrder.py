class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:    # search till all the elements are searched

            pivot = (left + right) // 2    # place the pivot at the middle
            pivot_item = nums[pivot]
            if target == pivot_item:
                return pivot
            elif target > pivot_item:    # if target is to the right
                left = pivot + 1
            else:    # if target is to the left
                right = pivot - 1
        
        return right + 1
        
s = Solution()
print(s.searchInsert([1,3,5,6],0))