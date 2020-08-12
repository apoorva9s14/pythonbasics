# Abstract Base Class implements abstract methods
# which "must" be over ridden by the child class
# Uses -
# To check if there are any incomplete implementations
# To enhance the functionality already provided by the base class

# Two ways to implement Abstract base class
# abc module - ABCMeta, ABC

# directly inherit from ABC, and use @abstractmethod decorator
# ABC in-turn has ABCMeta as its MetaClass
from abc import ABC, abstractmethod, ABCMeta

#  The first method, direct inherit from ABC
class BaseClassInheritanceWay(ABC):
     @abstractmethod
     def myabs(self,x,y):
         pass
class MyAbc(BaseClassInheritanceWay):
    pass

# >>> c = Ab()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't instantiate abstract class Ab with abstract methods myabs


class MyAbcInheritance(BaseClassInheritanceWay):
    def myabs(self,x):
        return x

class BaseClassMetaclassWay(metaclass=ABCMeta):
    @abstractmethod
    def myabs(selfself,x):
        return


class MyAbcMetaclass:
    def myabs(self,x,y):
        return x+y
    # pass

BaseClassMetaclassWay.register(MyAbcMetaclass)

test_obj = MyAbcMetaclass()
# print(MyAbcInheritance.__mro__)
# print(MyAbcMetaclass.__mro__)
print(set(MyAbcInheritance.__mro__).difference(set(MyAbcMetaclass.__mro__)))

#  For MyAbcMetaclass no inherited classes, hence it is a mixin
print('Subclass:', issubclass(MyAbcMetaclass, BaseClassMetaclassWay))
print('Instance:', isinstance(MyAbcMetaclass(), BaseClassMetaclassWay))

# d = BaseClassInheritanceWay()
# This gives Error as we cannot instantiate Abstract Base Classes