class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            print("IN FOR LOOP",n)
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

s = Solution()
print(s.longestConsecutive([3,2,4]))