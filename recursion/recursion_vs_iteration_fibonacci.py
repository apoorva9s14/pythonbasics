"""
Fibonacci series -
Recursive vs Iterative
"""

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


# print("Recursive Fibonacci", fib_recursive(6))


def fib_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# print("Iterative Fibonacci", fib_iterative(6))


class FibMemoised:
    memo = {0: 0, 1: 1}

    def fibm (self, n):
        print(FibMemoised.memo)
        if n == 1 or n== 0:
            return n
        if not FibMemoised.memo.get(n):
            FibMemoised.memo[n] = self.fibm(n-1) + self.fibm(n-2)
        return FibMemoised.memo[n] 

mem_fib = FibMemoised()
print("Memoized Fibonacci", mem_fib.fibm(6))


def fib_multiples_recursive(n):
    if n == 0:
        return 0
    else:
        return fib_multiples_recursive(n-1) + 3
        #  HINT--> Multiplication as recursive addition


# print("Recursive Multiplication", fib_multiples_recursive(12))


def sum_of_first_n_integers_recursive(n):
    if n == 0:
        return 0
    else:
        return sum_of_first_n_integers_recursive(n-1) + n


# print("Recursive Sum", sum_of_first_n_integers_recursive(4))
