#Explain default arguments and significance of None
#The default value is evaluated only once. When the default is a mutable object such as a list, dictionary, or instances of most classes.
#It gets changed with subsequent function calls,instead if we use None to be default and then convert it to list and use it
#With every function call, instead of storing the accumulated values, it comes back to None value
#For example, the following function accumulates the arguments passed to it on subsequent calls:

chosenMaster="ashwin"
def contactMaster(data="",url= str(chosenMaster)+"todolist"):
    print(url)

chosenMaster="apoorva"
contactMaster()

#Output is ashwintodolist. Default arguments are evaluated when the function is defined not when it is executed. 
#At the time of fn definition, the value of chosenMaster is ashwin, hence ashwin is taken.

def f(a, L=[]):
    print(id(L))
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
''' output is 
[1]
[1, 2]
[1, 2, 3]
id would be same in all the cases of execution'''

def f1(a, L=None):
    print(id(L))
    if L is None:
        L = []
    L.append(a)
    return L
print(f1(1))
print(f1(2))
#Prior to this call L has [1], but once it is default to None. It takes the fresh value 2.This is the significance of None.

print(f(3))
''' output is 
[1]
[2]
[3]
Here also the id is same'''