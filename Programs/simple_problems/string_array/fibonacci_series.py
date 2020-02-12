# Fibonacci with generator

def fib_with_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b