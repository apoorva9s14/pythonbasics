def quickSort(inp_arr):
    if len(inp_arr) < 2:
        return inp_arr
    pivot = inp_arr[0]
    left_arr, right_arr = [], []
    for elem in inp_arr[1:]:
        if elem > pivot:
            right_arr.append(elem)
        else:
            left_arr.append(elem)
    out_arr = quickSort(left_arr)+[pivot]+quickSort(right_arr)
    return out_arr
print(quickSort([-1,3,2,1,4,-5]))