"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""


def AnagramGroups(strs):
    sorted_list = []
    for i in range(strs):
        st="".join(sorted(strs[i]))
        sorted_list[i] =st
    