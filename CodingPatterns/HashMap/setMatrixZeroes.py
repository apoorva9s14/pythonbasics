from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        First iteration, track rows and columns with 0 and add them to the set
        Second iteration, check if the current item's row and column
        matches with that of the items in the sets, set that item to 0
        """
        m= len(matrix)
        n = len(matrix[0])
        rows_set = set()
        columns_set = set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows_set.add(r)
                    columns_set.add(c)
        for r in range(m):
            for c in range(n):
                if r in rows_set or c in columns_set:
                    matrix[r][c]=0
        return
    def setZeroesInPlace(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        To modify in-place and not use extra sets to hold the rows and columns
        use the first row and the first column as markers to track 0s
        For rows, use the first column to set which row has 0s
        For columns, use the first row to set which column has 0s
        """
        m= len(matrix)
        n = len(matrix[0])
        first_row_zero = False
        first_column_zero = False
        for r in range(m):
            for c in range(n):
                if matrix[0][c]==0:
                    first_row_zero = True
        for r in range(m):
            for c in range(n):
                if matrix[r][0]==0:
                    first_column_zero = True
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c]=0

        """
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0
        if first_column_zero:
            for r in range(m):
                matrix[r][0] = 0
        """
        return

matrix = [[1,2,3,4,5],[6,0,6,9,10],[11,12,13,14,15],[16,17,18,19,0]]
s= Solution()
print(s.setZeroesInPlace(matrix))
print(matrix)
        