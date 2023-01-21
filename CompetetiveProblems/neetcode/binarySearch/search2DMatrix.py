class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.n = len(matrix[0])
        m = len(matrix)
        left = 0
        right = m - 1
        while left <= right:    # search till all the elements are searched
            pivot = (left + right) // 2    # place the pivot at the middle
            pivot_item = matrix[pivot][0]

            if target == pivot_item:    # Found the element
                return True

            elif target > pivot_item:    # if target is to the right
                
                left = pivot + 1

            else:    # if target is to the left
                right = pivot - 1
        return self.binary_search(matrix[right], target)
    def binary_search(self, nums, target):
        left = 0
        right = self.n - 1
        while left <= right:    # search till all the elements are searched

            pivot = (left + right) // 2    # place the pivot at the middle
            pivot_item = nums[pivot]
            if target == pivot_item:    # Found the element
                return True

            elif target > pivot_item:    # if target is to the right
                
                left = pivot + 1

            else:    # if target is to the left
                right = pivot - 1
        return False
