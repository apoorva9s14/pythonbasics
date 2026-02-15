
def fib_recursion(n):
    if n <= 1:    ## base conditon
        return n
    return fib_recursion(n-1) + fib_recursion(n-2) ## recursive condition


n = 10
# for _ in range(n):
#        print(fib_recursion(_))

# def factorial_recursion(n):
#     if n<=1:return 1
#     return n*factorial_recursion(n-1)
# for _ in range(n):
#        print(factorial_recursion(_))
def factorial_tail_recursion(n, a=1):
 
    if (n <= 1):
        print("20",a)
        return a
 
    return factorial_tail_recursion(n - 1, n * a)
for _ in range(n):
       print(factorial_tail_recursion(_))