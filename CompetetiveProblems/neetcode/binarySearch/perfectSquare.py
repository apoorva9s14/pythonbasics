class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k = (num // 4) + 1
        print(k)
        i = 0
        while i <= k:
            if i*i == num:
                return True
            i += 1
        return False

s = Solution()
print(s.isPerfectSquare(2000105819))