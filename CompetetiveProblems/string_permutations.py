''' Find all possible permutations of a string'''
def permutations(string, step = 0):
    if step == len(string):
        # we've gotten to the end, print the permutation
        print("END", "".join(string))
    for i in range(step, len(string)):
        print("INSIDE FOR", step)
        # copy the string (store as array)
        string_copy = [c for c in string]
         # swap the current index with the step
        string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
         # recurse on the portion of the stringthat has not been swapped yet
        print("String Copy is",string_copy,step+1)
        permutations(string_copy, step + 1)
print(permutations ('one'))