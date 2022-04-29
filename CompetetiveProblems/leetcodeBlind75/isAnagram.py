from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sList = [None]*26
        # tList = [None]*26
        s1 = Counter(s)
        t1 = Counter(t)
        return s1 == t1


s = Solution()
print(s.isAnagram("anagram", "nagarama"))