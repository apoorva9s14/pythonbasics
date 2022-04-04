# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solutionFindMissingElement(A):
    # write your code in Python 3.6
    n = len(A)
    return (((n+1)*(n+2))/2) - sum(A)

def solution(A):
    # write your code in Python 3.6
    minSum = len(A)
    for i in range(minSum-1):
        sum_i = abs (sum(A[:i+1]) - sum(A[i+1:]))
        if sum_i < minSum:
            minSum = sum_i
    return minSum
print(solution([3,1,2,4,3]))
# See the difference between solution and optimisedSolution
# The If checks make a lot of difference for time complexity