"""Find factorial of a number"""


# --------------------------------------------------------------------
# Recursive Approach

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(5))
# factorial is not tail recursive, convert to tail recursive

# A tail recursive function


def tail_factorial(n):
    a = 1

    def tail_factor(n, a):
        if n == 0:
            return 1
        return tail_factor(n-1, n*a)
    return tail_factor


print(tail_factorial(5))


# def factTR (n, a):
#     if (n == 0):
#         return a
#
#     return factTR(n - 1, n * a)
#
#
# # A wrapper over factTR
# def fact (n):
#     return factTR(n, 1)


# -------------------------------------------------------------------
# Iterative Approach

def iterative_factorial(n):
    iter_fact = 1
    for i in range(1, n+1):
        iter_fact = iter_fact * i
    return iter_fact


print(iterative_factorial(5))