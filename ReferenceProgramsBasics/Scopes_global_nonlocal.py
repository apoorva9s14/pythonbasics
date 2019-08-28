#1. To explain the order of looking up of symbol tables. LEGB.Local--Enclosed--Global--Builtin
#2. Significance of nonlocal

len=10 #Global

def f():

	len=100  #Local
	print(len)
f()
print(len)

'''Output is
100
10
'''
print(len([1,2,3])) #Built-in
#Here trying to use built-in type throws error, because one global variable is already defined with the same name.
#There is a conflict b/w global and built-in.

#Gives Error - TypeError: 'int' object is not callable

'''
def method():

    def method2():
        # In nested method, reference nonlocal variable.
        nonlocal value #By declaring this, we say that this value has the scope for its parent function as well
        value = 100

    # Set local.
    value = 10
    method2()

    # Local variable reflects nonlocal change.
    print(value)
print(value)

# Call method.
method()
met()
'''



def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

'''O/p
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam

Reason - 1st print - as spam us defined as testspam, even after calling local fn, the local fn has local varaible defined, so it doesnt have an effect on the outer print statement
2nd print- doing non-local prints the nonlocal value as the loop is just outside the loop where nonlocal is defined
3rd print - though u made it global inside the fn's print fn it has local scope, so nonlocal is printed
4th print - once u come out of the fn, it will take the value given in the global fn
'''