"""
Find Rotation Index in a sorted array.
Input: arr[] = {15, 18, 2, 3, 6, 12}
Output: 2

This array was rotated where element 2 is present, so index of 2 is 2
"""

def find_rotation_point(arr):
    n = len(arr)
    start = 0
    end = n
    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if arr[mid-1] > arr[mid] < arr[mid+1]:
            return mid
        if arr[mid] < arr[start]:
            end = mid - 1
        else:
            start = mid + 1
    return 0
print(find_rotation_point([15, 18, 2, 3, 6, 12]))