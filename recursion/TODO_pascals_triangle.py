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

        def my_recursion(index_id):
            if index_id == 4:
                import pdb
                pdb.set_trace()
            rec_list = []
            for ind in range(index_id):
                # f(4,1) f(4,2) f(4,3) f(4,4)
                y = ind + 1
                x = index_id
                if x == y:
                    rec_list.append(1)
                elif y == 1:
                    rec_list.append(1)
                else:
                    rec_list.append(f(x, y))
            return rec_list

        def f(i, j):
            # f(4, 2)
            if j == 0 or j==1:
                return 1
            if i == 1 and j == 1:
                return 1
            if i == 2 and j == 1:
                return 1
            if i == 2 and j == 2:
                return 1
            #x = 3, y = 1
            x = i - 1
            y = j - 1
            if y == 0:
                return 1
            res = output_list[i-1][ j-1] + output_list[i-1][ j]
            return res

        for id in range(numRows):
            rec_new_list = my_recursion(id+1)
            output_list.append(rec_new_list)
            # my_recursion(index_id)
            # f(i, j) = f(i−1, j−1)+f(i−1, j)
            # f(1, 1) = 1 f(2,1) = 1 f(2, 2) = 1 f(3, 2) =
mys = Solution()
mys.generate(5)
