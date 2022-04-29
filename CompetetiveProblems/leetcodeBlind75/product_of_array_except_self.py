# Use of Prefix product and postfix product
# Postfix product comes from the end, i.e., from reverse
# product except self is prefix product * postfix product

from sys import prefix


class Solution:
    def productExceptSelf(self, nums):
        outList = []
        n = len(nums)
        prefixProduct = 1
        for each in nums:
            outList.append(prefixProduct)
            prefixProduct = each*prefixProduct
        print(outList)
        postfixProduct = 1
        for ind,val in enumerate(nums[::-1]):
            outList[n-ind-1] = outList[n-ind-1]*postfixProduct
            postfixProduct = val * postfixProduct
        return outList


s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))
        