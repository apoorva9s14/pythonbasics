"""
Given a list
Return the sorted list in ascending order
"""


def selection_sort(inp_list):
    sorted_list = []
    arr_counter = len(inp_list)
    target_list = []

    while arr_counter:
        target = find_min_value_in_list(inp_list[0:arr_counter+1])
        target_list.append(target)
        inp_list.remove(target)
        arr_counter -= 1

    return target_list


def find_min_value_in_list(nums):
    target = nums[0]
    for i in nums:
        if i < target:
            target = i
    return target


# TestCases
# For find_min_value_in_list
my_list = [10, 3, 5, 7, 9]
print(find_min_value_in_list(my_list))
# => 3

# For selection_sort
my_list = [10, 3, 5, 7, 9]
print(selection_sort(my_list))
# => [3, 5, 7, 9, 10]

my_list = [64, 25, 12, 22, 11]
print(selection_sort(my_list))
# => [11, 12, 22, 25, 64]