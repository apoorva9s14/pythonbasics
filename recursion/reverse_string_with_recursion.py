"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
import re


class Solution(object):
    def reverse_string(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        ref_len = len(s)
        for i in range(0, len(s)):
            regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
            pop_element = s.pop()
            if regex.search(pop_element) == "$":
                s.insert(ref_len - len(s), pop_element)
                continue
            # print("pop elem, ", pop_element, i)
            s.insert(i, pop_element)
            # print(s)
        return s


mysol = Solution()
print(mysol.reverse_string(["h", "$", "E", "l", "L", "o"]))
print(mysol.reverse_string(["h", "E"]))
