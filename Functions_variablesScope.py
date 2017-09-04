#Explain local and global scope of functions and its variables

x=5
#A global variable

f=100
#You define f as an integer, and next as a function, so whichever comes first is overwritten, now f is a function
def f():
	x2= x
	#x2 is a local variable
	
	x2+=1
	#Making changes on x2 doesnt effect x, because we have copied x to x2
	
	print(x2)
	#This print works fine as it is in local scope

f()
#prints 6

f=100
f()
print(f)
f()
#TypeError: 'int' object is not callable
#Integer value is overwritten by function value

print(x2) 
#NameError: name 'x2' is not defined. because it is in local scope

print(x)

#Significance of global nonlocal and how it changes the values.

#Normal Scope
x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 0

#Using nonlocal
x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 2
# global: 0

#Using global
x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 2