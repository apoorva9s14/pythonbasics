"""
given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)
"""

class Solution:
    def rotateString(self, s: str, goal: str):
        s_dict = {}
        for i in range(len(s)):
            if i == len(s)-1:
                s_dict[s[i]] = s[0]
            else:
                s_dict[s[i]] = s[i+1]
        goal_dict = {}
        for i in range(len(goal)):
            if i == len(goal)-1:
                goal_dict[goal[i]] = goal[0]
            else:
                goal_dict[goal[i]] = goal[i+1]
        for each in s_dict:
            if goal_dict[each] != s_dict[each]:
                return "false"
        return "true"
        
s = Solution()
print(s.rotateString("abcde", "abced"))



