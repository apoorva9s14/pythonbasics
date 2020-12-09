"""
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
"""

class Solution:
    def reverseString(self, s):
        def helper(left, right):
            # print(s[left], s[right])
            if left < right:
                # print("Got IF")
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


s=Solution()
s.reverseString(["h", "e", "l", "l", "o"])