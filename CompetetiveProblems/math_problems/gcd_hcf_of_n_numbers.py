"""
GCD of two numbers is the largest number that divides both of them
Euclidean algorithm
GCD of (A,B) is GCD of (A%B, B) B is the smaller number
repeat this till B is zero.
Find all the prime factors of two numbers, their intersection is gcd

Approach to find prime factors:
1. divide the number by 2 to get all the even factors(in terms of 2)
2. Starting from 3 to sqrt(n), in steps of 2,
 find all factors and keep dividing by that factor number.
 Repeat till it becomes 1 or prime number
3. If it didnt result in 1 after step2. It is a prime number factor


To find all divisors of a number

"""


def gcd (a, b):
    """gcd using euclidean algorithm"""
    if a == 0:
        return b

    return gcd(b % a, a)


import math


# A function to print all prime factors of
# a given number n
def primeFactors (n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2,)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n, print i ad divide n
        while n % i == 0:
            print(i,)
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


import math


# method to print the divisors
def printDivisors (n):
    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):

        if (n % i == 0):

            # If divisors are equal, print only one
            if (n / i == i):
                print(i,)
            else:
                # Otherwise print both
                print(i, n / i,)

        i = i + 1



