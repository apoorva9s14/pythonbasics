"""
Input  : s = "geeks"
Output : [["g", "e", "e", "k", "s"],
          ["g", "ee", "k", "s"]]
"""


class Solution(object):
    @staticmethod
    def is_palindrome(s):
        # TODO not an optimal solution
        rev_s = ""
        for i in range(len(s)-1,-1,-1):
            rev_s = rev_s + s[i]
        if not rev_s or len(rev_s) == 1:
            return False
        if rev_s == s:
            return True
        else:
            return False

    @staticmethod
    def find_palindromes(input_string):
        """
        finding all possible palindromes in a string
        Logic: starting from each character, step through all possible subcharacters
        and check if they are palindromes
        """
        palindromes_list = []
        len_range = len(input_string)
        for s in range(len_range):    # item loop
            for i in range(s, len_range + 1):    # step loop
                if Solution.is_palindrome(input_string[s:s+i]):
                    # print(input_string[s:s+i])
                    palindromes_list.append(input_string[s:s+i])
        return palindromes_list


mysol = Solution()
print(mysol.is_palindrome("hello"))
print(mysol.is_palindrome("heh"))
print(mysol.find_palindromes("tenet"))
print(mysol.find_palindromes("geek"))
print(mysol.find_palindromes("nitin"))
# t+0 1step
# t+e 2steps
# t+e+n