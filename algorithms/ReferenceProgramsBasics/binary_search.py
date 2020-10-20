"""
Given a list and an item
Return the item pivotition in the list
"""


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:    # search till all the elements are searched

        pivot = (left + right) // 2    # place the pivot at the middle
        pivot_item = nums[pivot]

        if target == pivot_item:    # Found the element
            return pivot

        elif target > pivot_item:    # if target is to the right
            left = pivot + 1

            # shift the left partition to the next
            # item after pivot

        else:    # if target is to the left
            right = pivot - 1

            # shift the right partition to the previous
            # item before pivot
    return None


# TestCases
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 9))
# => 4

print(binary_search(my_list, -1))
# => None