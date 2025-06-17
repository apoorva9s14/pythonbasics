# Python program to find maximum product subarray
 
# Returns the product of max product subarray.
# Assumes that the given array always has a subarray
# with product more than 1
def maxsubarrayproduct(arr):
    max_ending, max_product = 1, 1
    for a in arr:
        max_ending = max(abs(max_ending), abs(max_ending*a))
        max_product = max(max_product, max_ending)
        print(a, max_ending, max_product)
    return max_product

print(maxsubarrayproduct([1, -2, -3, 0, -7, -8, -2]))
