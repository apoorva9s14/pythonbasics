"""
Given an array of distinct integers and a sum value.
Find count of triplets with sum smaller than given sum value.
Expected Time Complexity is O(n2).

Input : arr[] = {-2, 0, 1, 3}
        sum = 2.
Output : 2
Explanation :  Below are triplets with sum less than 2
               (-2, 0, 1) and (-2, 0, 3)
"""


import itertools
class Solution(object):
    @staticmethod
    def generate_combinations_with_itertools(input_array, count_comb):
        """Given an input_array,generate combinations with count_comb"""
        comb_output = []
        for combination in itertools.combinations(input_array, count_comb):
            comb_output.append(combination)
        return comb_output

    @staticmethod
    def generate_combinations(input_array, count_comb):
        """Given an input_array,generate combinations with count_comb
        without using itertools module"""
        #TODO Implement
        pass

    @staticmethod
    def count_combinations_with_condition(input_array, count_val=3, **kwargs):
        if kwargs.get("condition_type") == "sum":
            sum_value = kwargs.get("sum_value")
        else:
            return
        combs_list = Solution.generate_combinations_with_itertools(input_array, count_val)
        output_list = []
        for item in combs_list:
            if sum(item) < sum_value:
                output_list.append(item)
        return output_list

    @staticmethod
    def sum_of_list(input_array):
        sum_val = 0
        for i in input_array:
            sum_val += i
        return sum_val


mysol = Solution()
print(mysol.count_combinations_with_condition([5, 1, 3, 4, 7],
                                              condition_type="sum",
                                              sum_value=12))
