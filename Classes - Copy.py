
class Abc:  
    " A Sample Class "  #Doc string for class
    def __init__(self,a=0,b=0): #a,b are keyword args
        self.a = a              #Instance object(self).keyword args to be passed to the whole class
        self.b = b              #Whatever you define in init can be passed to the whole functions of class, use them directly by self.var_name.but while instantiating the object, make sure to pass them to the class like o=A(args)
    def add(self,c):            #c is just passed to this function definition 
        return self.a + self.b + c
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def __str__(self):          #the string representation for the class==print(OBJECTNAME). For the child class also, same __str__ method of the parent class is used, if no __str__ method is defined in the child class
        return "This is the object of class Abc"   #this __str__ method should return only "String type", if there is no return type mentioned in this method, it throws a traceback error.
    def __del__(self):
        class_name = self.__class__.__name__   #To retrieve the class name obj.__class__.__name__
        print(class_name, "destroyed")

obj = Abc()
print(obj)
#print(obj.__doc__)
#print(obj.add.__doc__)
#print(Abc.__dict__)     #Class's dict will have all the function details, name.
print(Abc.__name__)
print(Abc.__module__)
print(Abc.__base__)

del obj

#will print <class '__main__.A'>

#{'add': <function Abc.add at 0x00D68078>, '__module__': '__main__', '__init__':
#<function Abc.__init__ at 0x00D681E0>, 'mul': <function Abc.mul at 0x00D68810>,
#'__str__': <function Abc.__str__ at 0x00D684F8>, '__doc__': ' This is what the c
#lass does. ', 'sub': <function Abc.sub at 0x00D68420>}

#print(obj.__dict__)     # Object dict will have only a,b
#{'a': 0, 'b': 0}   



            
obj = Abc(70,80)    #Passing values of a,b
print(obj.add(10))  #Passing c,Apart from the memberships args,(class args) you can also pass extra args 
print(obj.sub())    #Need not pass anything, because class's default args are already passed to all the fns.
#Instead of passsing arguments to each individual fns in class,pass them to a class direclty, all those arguments can be used by the fns inside class.
print(obj.mul())

print('******Diamond Inheritance**********')
class A:
    def f2(self):
        print("I am function 2 of class A")
    def f3(self):
        print("I am function 3 of class A")
class B(A):
    '''
    def f2(self):
        print("I am function 2 of class B") #Overriding by child C
    '''
    def f4(self):
        print("I am function 4 of class B")
class C(A):
    def f1(self):
        print("I am function 1 of class C")
    def f2(self):
        print("I am function 2 of class C")
    def f3(self):
        print("I am function 3 of class C")

class D(B,C):
    '''
    def f2(self):
        print("I am function 2 of class D")
    def f3(self):
        print("I am function 3 of class D")
    '''
    pass


objD = D()
objD.f2()   #Example showing Multiple inheritance and L-R priority.
objD.f3()   #Diamond inheritance. MRO - D B C A



'''
Importance of self. If you are passing self to all the functions in the class, while creating an object for the class
you have to define it as class_name(). The () indicates that () is for the self argument, which is by default passed by python to all
the functions in the class, so while creating the object, you need not write self(self).
objB = B()
objB.f2()

If you want to skip self, you create the object without passing any arguments to the class, i.e.obj=class_name
objB = B
objB.f2()
'''

print('******Multi-level Inheritance**********')
# Multi-level Inheritance
class A:  #Super parent
    def f1(self):
        print("This is function 1 of Class A")
    def f2(self):
        print("This is function 2 of Class A")


class B(A):   #Parent
    def f2(self):
        print("This is function 2 of Class B")

class C(B):pass  #Child

objC = C()
objC.f1()


print('******Data Hiding**********')
class Abc:
    __x=10             #Hidden variable
    def __fun(self):   #Hidden function
        print("Hello")

obj = Abc()
print(obj._Abc__x)   #to retrieve hidden attribute obj._classname__attributename
#print(obj.__x)      #even this hack is not helpful, you have to follow the syntax given above 
print(obj._Abc__fun)
#'''

print('******Operator overloading**********')
# Operator overloading

class OpOverload:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        a=self.a+other.a
        b=self.b+other.b
        #global v
        v=OpOverload(a,b)
        return v
    def __str__(self):
        return "Overloaded addition of %d and %d is " % (self.a,self.b)
        #return v

obj1 = OpOverload(2,3)
obj2 = OpOverload(4,5)
print(obj1+obj2)



import math
 
class Circle:
 
    def __init__(self, radius):
        self.__radius = radius
 
    #def setRadius(self, radius):
    #    self.__radius = radius
    #
    def getRadius(self):
        return self.__radius
    
    def area(self):
        return math.pi * self.__radius ** 2
 
    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius )
 
c1 = Circle(4)
#print(c1.getRadius())
 
c2 = Circle(5)
#print(c2.getRadius())
#print(type(c2.getRadius()))

 
c3 = c1 + c2 # This became possible because we have overloaded + operator by adding a    method named __add__ and
#by this we can add two objects of this class
print(c3.area())


'''
class A:
	def __init__(self,p1,p2):
		self.p1=p1
		self.p2=p2
	def add(self):
		p3=[]
		l1=len(self.p1)
		l2=len(self.p2)
		if l1 == l2:
			for i in range(l1):
				p3.append(self.p1[i]+self.p2[i])
			return p3
		elif l1>l2:
			L2=self.p2
			#print(L2)
			for i in range(l1-l2):
				print(i)
				L2.append(0)
			#print(L2)
			for i in range(l1):
				p3.append(self.p1[i]+self.p2[i])
			return p3
		elif l2>l1:
			L1=self.p1
			for i in range(l2-l1):
				L1.append(0)
			for i in range(l2):
				p3.append(self.p1[i]+self.p2[i])
			return p3
			
		
a=A([1,2,3],[1,2,3,4,5,6,7])
print(a.add())
'''
'''
#Another example of inheritance

class Person:
	def __init__(self, idNumber):
		#self.firstName = firstName
		#self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		#print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    d={1:'A',2:'B',3:'C',4:'D'}
    def __init__(self,idNumber,ns,scores):
	    Person.__init__(self, idNumber)  #Using parent's init function, so that u need not do, self.idnumber=idnumber again
	    #self.idNumber = idNumber
	    self.scores = scores
	    self.ns=ns
    def calculate(self):
	    d={1:'A',2:'B',3:'C',4:'D'}
	    g=sum(self.scores)//self.ns
	    print(g)
	    print(d[g])		
		
'''
















