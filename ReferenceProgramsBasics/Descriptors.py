#Descriptors explanation

#A normal Python dictionary stores references to objects it uses as keys.
#Those references by themselves are enough to prevent the object from being garbage collected.
#To prevent Book instances from hanging around after we are finished with them, we use the WeakKeyDictionary from the weakref standard module.
#Once the last strong reference to the instance passes away, the associated key-value pair will be discarded.
#The weakref module supports weak references to objects.
#A normal reference increments the reference count on the object and prevents it from being garbage collected.


#Normal Book class
class Book(object):
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

#The descriptor class Price which puts constraints on the the attribute's(price's) value to be between 0 to 100
from weakref import WeakKeyDictionary

class Price(object):
    def __init__(self):
        #self.default = 0 #This is needed to just print the default value
        self.values = WeakKeyDictionary() #explanation below

    def __get__(self, instance, owner):
        #instance is the instance of Boook Class
        #owner is the Book Class
        #return self.values.get(instance, self.default) #This is needed to just print the default value, if the key is not found
        return self.values.get(instance)

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        self.values[instance] = value   
        #Writing to the dictionary self.values i.e.if we do b.price =12, it is saving the the value 12 in the dictionary self.values under the key which is the current instance.
        print(self.values)

    def __delete__(self, instance):
        del self.values[instance]

class Book(object):
    price = Price()
    #An instance of a descriptor must be added to a class as a class attribute, not as an instance attribute.
    # Therefore, to store different data for each instance, the descriptor needs to maintain a dictionary that maps instances to instance-specific values.
    #In the implementation of Price, that dictionary is self.values.
 
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

''' When we do 
>>> b = Book("William Faulkner", "The Sound and the Fury", 12)
>>> b.price=-12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 58, in __set__
ValueError: Price must be between 0 and 100.
'''

'''
When we try to evaluate b.price and retrieve the value, Python recognizes that price is a descriptor and calls Book.price.__get__.
When we try to change the value of the price attribute, e.g. b.price = 23 , Python again recognizes that price is a descriptor and substitutes the assignment with a call to Book.price.__set__.
And when we try to delete the price attribute stored against an instance of Book, Python automatically interprets that as a call to Book.price.__delete__.
'''
class Publisher(object):
    def __init__(self, name):
        self.__name = name
 
    def get_name(self):
        print("getting name")
        return self.__name
 
    def set_name(self, value):
        print("setting name")
        self.__name = value
 
    def delete_name(self):
        print("deleting name")
        del self.__name
 
    name = property(get_name, set_name, delete_name, "Publisher name")
    #Instead of having a totally different class for descriptor, use this one-liner function and write the descriptor in the same class
