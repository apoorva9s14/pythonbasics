

def MySubmittedSolution(A):
    # write your code in Python 3.6
    N = len(A)
    shadow_table = [False for i in range(N+1)]
    shadow_table[0] = True
    consecutive_on = 0
    ons = 0
    for index in A:
        shadow_table[index] = True
        if shadow_table[index-1] == True and consecutive_on==index-1:
            ons += 1
            while consecutive_on < N-1 and shadow_table[consecutive_on+1]:
                consecutive_on += 1
    return ons


def solution(A):
    rightMostVal = -1
    count = 0
    N = len(A)
    for i in range(N):
        if A[i] > rightMostVal:
            rightMostVal = A[i]
        if rightMostVal == i+1:
            count += 1
    return count

A = [2,1,3,5,4]
print(solution(A))

B = [5,2,3,1,4]
print(solution(B))