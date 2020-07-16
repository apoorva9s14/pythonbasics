"""
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""


class Solution:
    """Simple Recursion"""
    def tribonacci (self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)

class SolutionTail:
    """TailRecursion"""
    def tribonacci(self, n: int) -> int:
        def tailtrib(n,a=0,b=1,c=1):
            print("Calling tail with",n,a,b,c)
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1

            return tailtrib(n-1,b,a+b,a+b+c)
        return tailtrib(n)

# To write tail recursive functions
# use one more argument and accumulate the factorial value
# in second argument. When n reaches 0, return the accumulated value.


s = Solution()
print(s.tribonacci(3))


def fib (n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib(n - 1, b, a + b);


# Driver Code
n = 9;
print("fib(" + str(n) + ") = " + str(fib(n)))