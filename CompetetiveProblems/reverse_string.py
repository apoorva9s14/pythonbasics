class Solution:
    def reverseString(self, s):
        def helper(left, right):
            # print(s[left], s[right])
            if left < right:
                # print("Got IF")
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
        print(s)


s=Solution()
s.reverseString(["h", "e", "l", "l", "o"])
