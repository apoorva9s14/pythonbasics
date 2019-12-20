"""
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output_list = []
        for i in range(numRows):
            if i == 0:
                output_list.append([1])
            if i == 1:
                output_list.append([1, 1])
            res = self.pascalgenerator(i)

    def pascalgenerator(self,i):
        ref = i + 1
        pascal_list = []
        for j in range(i):
            if j == 0:
                pascal_list.append(1)
            if ref == j:
                pascal_list.append(1)


mys = Solution()
mys.generate(5)
