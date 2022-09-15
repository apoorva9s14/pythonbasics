

def find_elem_index_binary_search(l,elem):
    # [1,1,1,1]
    # [1,1]
    # [1,1]
    a = len(l)
    right_ptr = a - 1
    left_ptr = 0
    
    # [1,2,3,5]
    # [2,4]
    ref_ptr = None
    while left_ptr <= right_ptr:
        mid_ptr = (right_ptr+left_ptr)//2
        mid = l[mid_ptr]
        if elem < mid:
            right_ptr = mid_ptr - 1
        elif elem > mid:
            left_ptr = mid_ptr + 1
        else:
            ref_ptr = mid_ptr
            return ref_ptr
    if not ref_ptr:
        if elem > l[a-1]:
            ref_ptr = a-1
        if elem < l[0]:
            ref_ptr = 0
    return ref_ptr
print(find_elem_index_binary_search([1,2,3,4,5], -1))