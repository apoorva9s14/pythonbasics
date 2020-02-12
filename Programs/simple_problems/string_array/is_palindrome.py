class Solution(object):
    def is_palindrome(self, s):
        """
        :type s: List[str]
        :rtype: True or False
        """
        # TODO this is the solution based on lists
        # TODO Not an optimal solution, chances of failure
        old_str = "".join(s)
        for i in range(0, len(s)):
            pop_element = s.pop()
            # print("pop elem, ", pop_element, i)
            s.insert(i, pop_element)
            # print(s)
        if "".join(s) == old_str:
            return True
        else:
            return False


mysol = Solution()
print(mysol.is_palindrome(["h", "E", "l", "L", "o"]))
print(mysol.is_palindrome(["h", "E", "h"]))
