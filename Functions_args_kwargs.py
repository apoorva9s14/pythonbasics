#Explain *args and *kwargs
#Significance of *



#def sum(a, b):
#    print("sum is", a+b)
#This accepts only two arguments

#*args
def sum(*values):
    s = 0
    print(type(values))
    for i in values:
        s += i
    print("sum is", s)
#This can accept variable number of arguments,0 or more.

sum(1,2)

t=(1,2)
sum(*t)
#Example of unpacking

'''
Output
<class 'tuple'>
sum is 3
<class 'tuple'>
sum is 3
'''

#*args - function parameters are passed as tuple
#sum(1,2) and sum(*t) are both same because *t unpacks the tuple and assigns the respective values
#For unpacking make sure that you have all the required arguments to unpack.If not, it throws an error

def f(x,y,z):
    print(x)
    print(y)
    print(z)

t=(1,2)
f(*t)
#TypeError: f() missing 1 required positional argument: 'z'

def functionA(*a, **kw):
       print(a)
       print(kw)


functionA(1, 2, 3, 4, 5, 6, a=2, b=3, c=5)
 
'''Output
(1, 2, 3, 4, 5, 6)
{'a': 2, 'c': 5, 'b': 3}
'''
lis=[1, 2, 3, 4]
dic={'a': 10, 'b':20}
functionA(*lis, **dic)  #it is similar to functionA(1, 2, 3, 4, a=10, b=20)
print(*lis)
print(**dic)

'''Output(1, 2, 3, 4)
{'a': 10, 'b': 20}
'''


