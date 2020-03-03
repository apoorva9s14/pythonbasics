#Difference between functions and generator

def g():
    print('inside generator')
    yield 1
    
g()
#The function call does not print 'inside generator'
#When the generator function is called, the function code is not executed
#Instead the function call returns a generator object

def f():
     print('inside function')
     return 1
f()
#Function call prints 'inside function' and 1
#as the code in the function body gets executed with the function call

