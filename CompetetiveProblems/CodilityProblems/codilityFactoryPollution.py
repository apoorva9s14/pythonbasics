import bisect

def solution(A):
    # write your code in Python 3.6
    desired = sum(A)/2
    filter_count = 0

    while True:
        A.sort()
        print("sorted A", A)
        A[-1] = A[-1]/2
        filter_count+=1
        if sum(A) <= desired:
            break
    return filter_count
def mySubmittedSolution(A):
    # write your code in Python 3.6
    desired = sum(A)/2
    filter_count = 0
    A.sort()
    L = len(A)
    while True:
        # print("A11",A)
        A[-1] = A[-1]/2
        # print("A13",A)
        filter_count+=1
        if sum(A) <= desired:
            break
        if A[-1] < A[-2]:
            item = A[-1]
            lo , hi = 0 , L-1
            m = (lo+hi)//2
            # print("M", m, lo, hi)
            if item < A[m]:
                # print("A",A)
                hi = m-1
                ind = bisect.bisect_left(A,item,lo,hi)
                A = A[:ind+1]+[item]+A[m:-1]
                # print("L", A, ind, lo, hi, m, item)
            else:
                lo = m+1
                ind = bisect.bisect_right(A,item,lo,hi)
                A = A[:m]+[item]+A[ind+1:-1]
                # print("R", A, ind, lo, hi, m, item)
            # print(A)
    return filter_count

print(solution([5, 19, 8, 1]))
print(solution([10,10]))
print(solution([3, 0, 5]))
