## Lomutos algorithm
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

# Hoares Algorithm
class Sort:
    def _quicksort(self, array: list, low: int, high: int) -> None:
        if low < high:
            pivot = self._partition(array, low, high)
            print("LOW", array, low, pivot)
            self._quicksort(array, low, pivot)
            print("HIGH", array, pivot + 1, high)
            self._quicksort(array, pivot + 1, high)

    def _partition(self, array: list, low: int, high: int) -> int:
        pivot = array[(high + low) // 2]
        i = low
        j = high

        while True:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            array[i], array[j] = array[j], array[i]

    def sort(self, array: list) -> list:
        self._quicksort(array, 0, len(array) - 1)
        return array

# Driver Code
s = Sort()
print(s.sort([3,2,4,6,7,1,5]))

## Reference - https://csanim.com/tutorials/hoares-quicksort-algorithm-python-animated-visualization-code