def startAt(start):
	#Nested function start
	def incrementBy(inc):
		return start + inc
		#Nested fn's return statement
	return incrementBy
	#Outer fn's return statement

f = startAt(10)
#Calling the outer function returns a value - which is a function object
g = startAt(100)

print(f(1), g(2))  #Call this function object again to get the desired value)
#11 102

'''
Closures are useful because they let you associate some data (the lexical environment) with a function that operates on that data. 
This is similar to OOP, where objects have some data (the object's properties) with one or more methods.

We can use a closure anywhere that you might normally use an object with only a single method.
Closures are factories for functions
'''
'''Closures in python are created by function calls. 
In the code above, the call to startAt() creates a binding for start that is referenced inside the function incrementBy(). 
Each call to startAt() creates a new instance of this function, but each instance has a link to a different binding of start. 
Each function call saves the value of start(each time)
Even after you delete the function that instance of function call is retained
del startAt
f(1) #prints 11
'''
'''
So, it looks like the call objects f and g retain their states at the time they were created. 
When we create f, the outer function startAt() uses the nested function incrementBy() as a return value.
f= <function startAt.<locals>.incrementBy at 0x0000000002CDB488>
Note that it's the function itself that is returned, not the return value of that function. (only function's pointer is returned)
The inner function is not called within the startAt() function. 
So, the startAt() is a function that returns a function when called. 
In that way, our program can have an external reference to the nested function, and the nested function retains its reference to the call object of the outer function. 
In that way, the call object for a particular invocation of the outer function continues to live, even after you delete the outer fn.

In summary, a closure is a function (object) that remembers its creation environment (enclosing scope).
here enclosing scope value is start's value.
'''
'''
In closure inner fn's name is invisible to the outside, in this case, incrementBy is not shown anywhere
f.__closure__[0].cell_contents
returns 10
so you can very well use lambda fn
def startAt(start):
	return lambda inc: start+inc
'''




def print_msg(msg):
    """This is the outer enclosing function"""
    x=5	
    def printer():
        """This is the nested function"""
        print(msg)
        print(x)		

    printer()
#printer()
# We execute the function
# Output: Hello
#print_msg("Hello")

x = 0
def f():
    def g(): 
        return x * 2
    return g


closure = f()
print(closure()) # 0
x = 2
#print(closure()) # 4
x=3
#print(closure())  #6
#In the following example, calling the closure g after changing x will also change the value of x within g, since g closes over x:

#Another Example

def multiply_by(factor):
    """Return a function that multiplies values by the given factor"""
    def multiply(value):
        """Multiply the given value by the factor already provided"""
        return value * factor
    return multiply
f = multiply_by(8)
print(f(10))