"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution(object):
    def spiralOrder(self, matrix):
        out_list = []
        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        k, l = 0, 0
        a = matrix
        while (k < m and l < n):

            # Print the first row from
            # the remaining rows
            for i in range(l, n):
                print("l,n:", l, n)
                out_list.append(a[k][i])

            k += 1

            # Print the last column from
            # the remaining columns
            for i in range(k, m):
                print("k,m:", k, m)
                out_list.append(a[i][n - 1])

            n -= 1

            # Print the last row from
            # the remaining rows
            if (k < m):

                for i in range(n - 1, (l - 1), -1):
                    out_list.append(a[m - 1][i])

                m -= 1

            # Print the first column from
            # the remaining columns
            if (l < n):
                for i in range(m - 1, k - 1, -1):
                    out_list.append(a[i][l])

                l += 1
        return out_list



s=Solution()
s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


def spiralPrint (m, n, a):
    k = 0
    l = 0

    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")

        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")

            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")

            l += 1


# Driver Code
a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

R = 3
C = 6

# Function Call
spiralPrint(R, C, a)

print(s.spiralOrder(a))