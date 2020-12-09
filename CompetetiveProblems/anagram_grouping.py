"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Approach 1: Categorize by Sorted String
Intuition

Two strings are anagrams if and only if their sorted strings are equal.
Time Complexity: O(NK \log K)O(NKlogK),
Space Complexity: O(NK)O(NK)
"""


import collections

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        print(ans)
        return ans.values()


"""
Approach 2: Categorize by Count
Intuition

Two strings are anagrams if and only if their character counts 
(respective number of occurrences of each character) are the same.
"""
class Solution2:
    def groupAnagrams(self,strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        print(ans)
        return ans.values()


s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
s.groupAnagrams(strs)

s = Solution2()
strs = ["eat","tea","tan","ate","nat","bat"]
s.groupAnagrams(strs)