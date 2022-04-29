class Solution:
    def maxArea(self, height) -> int:
        right_ptr = len(height) - 1
        max_area = 0
        left_ptr = 0
        while left_ptr < right_ptr:
            print(height.index(height[left_ptr]),min(height[left_ptr],height[right_ptr]), right_ptr)
            cur_area = (min(height[left_ptr],height[right_ptr])) * (right_ptr - left_ptr)
            max_area = max(max_area, cur_area)
            if height[left_ptr] < height[right_ptr]:
                
                left_ptr += 1
            elif height[right_ptr] <= height[left_ptr]:
                right_ptr -= 1
                
        return max_area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))