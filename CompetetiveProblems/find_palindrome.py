import collections
class Solution:

    def isPossible(self, S):
        forCounter = False
        oddFlagCounter = 0
        evenCount = 0
        #counterL = collections.Counter(inp_str)
        counterL = {}
        for each in S:
            counterL[each] = S.count(each)
            
        for i in counterL:
            if counterL[i] % 2 == 0:
                evenCount += 1
                continue
            else:
                oddFlagCounter += 1
        if oddFlagCounter == 1 or evenCount == len(counterL):
            return "Yes"
        return "No"
s = Solution()
print(s.isPossible("meayl"))