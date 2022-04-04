# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N == 1:
        return A[0]
    arr_Map = {}
    for i in range(N):
        if A[i] in A[:i]+A[i+1:]:
            if arr_Map.get(A[i]):
                arr_Map[A[i]] += 1
            else:
               arr_Map[A[i]] = 1 
        else:
            return A[i]
    for each in arr_Map:
        if arr_Map[each]%2 == 1:
            return each

def optimisedSolution(A):
    # Defining HashMap in C++
    Hash=dict()
  
    # Putting all elements into the HashMap
    for i in range(len(A)):
        Hash[A[i]]=Hash.get(A[i],0) + 1;
     
    # Iterate through HashMap to check an element
    # occurring odd number of times and return it
    for i in Hash:
 
        if(Hash[i]% 2 != 0):
            return i
    return -1
print(solution([1, 1, 2, 2, 2, 2, 1]))

# See the difference between solution and optimisedSolution
# The If checks make a lot of difference for time complexity