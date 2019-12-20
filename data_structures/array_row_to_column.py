"""
task is to convert all rows to columns and columns to rows
Input:
First line contains 2 space separated integers, N - total rows, M - total columns.
Each of the next N lines will contain M space separated integers.

Output:
Print M lines each containing N space separated integers.
"""

n, m = list(map(int, input().split()))
custom_array = []


for i in range(n):
    row = list(map(int, input().split()))
    custom_array.append(row)

# print(custom_array)


def row_column_traversal(inp_array):
    out_array = []
    for index in range(m):
        column_array = []
        for row in inp_array:
            column_array.append(row[index])
        out_array.append(column_array)
    return out_array


# print(row_column_traversal(custom_array))
for item in row_column_traversal(custom_array):
    print(" ".join(list(map(str, item))))
