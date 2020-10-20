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


# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         output_list = []
#         for i in range(numRows):
#             print("OT_LIST", output_list)
#             if i == 0:
#                 output_list.append([1])
#             elif i == 1:
#                 output_list.append([1, 1])
#             else:
#                 output_list.append(self.pascalgenerator(output_list[i-1]))
#         return output_list
#
#     def pascalgenerator(self,inp_list):
#         print("INP_LIST", inp_list)
#         pascal_list = []
#         inp_range = len(inp_list)
#         for j in range(inp_range):
#             if j == 0:
#                 pascal_list.append(1)
#             # elif j==inp_range - 1:
#             #     pascal_list.append([j]+inp_range[j-1])
#             else:
#                 pascal_list.append(inp_list[j]+inp_list[j-1])
#         pascal_list.append(1)
#         return pascal_list

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            output_list = []
        elif numRows == 1:
            output_list = [[1]]
        else:
            output_list = [[1],[1, 1]]
            append = output_list.append
            i = 2
            while i < numRows:
                pascal_list = [1]
                j = 1
                pascal_append = pascal_list.append
                while j < i:
                    pascal_append(output_list[i-1][j] + output_list[i-1][j - 1])
                    j = j + 1
                pascal_append(1)
                append(pascal_list)
                # append(self.pascalgenerator(output_list[i-1],i))
                i += 1
        return output_list

    def pascalgenerator(self,inp_list,inp_range):
        # print("INP_LIST", inp_list)
        pascal_list = [1]
        j = 1
        pascal_append = pascal_list.append
        while j < inp_range:
            # if j == 0:
            #     append(1)
            # elif j==inp_range - 1:
            #     pascal_list.append([j]+inp_range[j-1])
            # else:
            pascal_append(inp_list[j]+inp_list[j-1])
            j = j+1
        pascal_append(1)
        return pascal_list
mys = Solution()
print(mys.generate(5))
