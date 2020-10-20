#decorator is a function that takes another function and extends the behavior of the latter function 
#without explicitly modifying it.
#Writing decorator_fn-smart_divide
#Pass the fn_tobe_decorated(any variable func) to the decorator function(smart_divide).
def smart_divide(func):#Only the function which has to be decorated is passed here.
    def inner(a,b): #Using inner because, u cannot pass further args to smart_divide.#inner has the same no.of args as that of the original func-divide
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b
print(divide(2,0))
#@smart_divide is same as writing divide = smart_divide(divide)

#Decorator is a higher order function
#A function which takes another function as input is a higher order function
#Closure, decorator etc

#Decorator should modify the behaviour of the decorated function
#Inner function returns the function call of the function which is passed, again an example of closure.

#Classes as decorators
#Classes should have init and call implemented
#init initialises with the function, call makes the class instance callable
#because the function is callable
#1.Class-based decorators without arguments
class CustomAttr:
    def __init__(self, obj):
        self.attr = "a custom function attribute"
        self.obj = obj

    def __call__(self):
        self.obj()
#Class is callable, but the object of the class is not callable, to make it callable use __call__method.
#Here func is a CustomAttr object
@CustomAttr
def func():
    pass
	
#>>> func
#<__main__.CustomAttr object at 0xb6f5ea8c>
#>>> func.attr
#'a custom function attribute'

#2.Class-based decorators with arguments
class CustomAttrArg:
    def __init__(self, value):
        self.value = value

    def __call__(self, obj):
        obj.attr = "a custom function attribute with value {}".format(self.value)
        return obj

@CustomAttrArg(1)
def func():
    pass