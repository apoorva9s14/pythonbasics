# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if K == 0:
        return A
    if len(A) == 1:
        return A
    arrLen = len(A)
    newA = [None]*arrLen
    for j in range(arrLen):
        if j+K >= arrLen:
            print(j,K)
            newA[j+K-arrLen-(arrLen*(K//arrLen))] = A[j]
        else:
            newA[j+K] = A[j]
    return newA

print(solution([1, 1, 2, 3, 5], 42))