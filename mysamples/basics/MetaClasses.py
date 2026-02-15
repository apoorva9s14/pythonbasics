"""
MetaClass defines the behaviour of class  just like
Class defines the behaviour of instance

Metaclass is same as type, it takes 3 inputs
the classname you want to create
Baseclasses of that class
Attribute dict of the class
These 3 inputs are passed to new of the metaclass, which inturn
calls new of type super class

__prepare__ is called at the very beginning
If you define __call__ in Class, it makes the instance Callable

"""


class MetaClass(type):

    def __init__(cls, *args, **kwargs):
        print("In MC init")
        print("Cls", cls)
        print("INIT *args", *args)
        for k, v in kwargs.items():
            print("INIT **kwargs", k, v)

    def __new__(cls, *args, **kwargs):
        """Static Method"""
        print("In MC New")
        print("NEW Cls", cls)
        print("NEW *args", *args)
        for k, v in kwargs.items():
            print("NEW **kwargs", k, v)
        return type.__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        """This call makes the instance callable
        Args are the args of instance"""
        print("IN MC CALL")
        print("CALL Cls", self)
        print("CALL *args", *args)
        for k, v in kwargs.items():
            print("CALL *kwargs", k, v)


    # @classmethod
    def __prepare__(mcs, *args, **kwargs):
        print("In MC Prepare")
        print("Prepare mcs", mcs)
        print("PREPARE *args", *args, "**kwargs", **kwargs)
        for k, v in kwargs.items():
            print("NEW **kwargs", k, v)
        return {}


class BaseClass(int):
    pass


class ExampleClass(metaclass=MetaClass):

    def __init__(self, *args, **kwargs):
        print("In CLASS init")
        print("INIT *args", *args)
        for k, v in kwargs.items():
            print("INIT **kwargs", k, v)

    def __new__(cls, *args, **kwargs):
        """Static Method"""
        print("In CLASS New")
        print("NEW Cls", cls)
        print("NEW *args", *args)
        for k, v in kwargs.items():
            print("NEW **kwargs", k, v)
        return type.__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        """This call makes the instance callable
        Args are the args of instance"""
        print("72 CALL Cls", self)
        print("CALL *args", *args)
        for k, v in kwargs.items():
            print("CALL *kwargs", k, v)

    @classmethod
    def __prepare__(mcs, *args, **kwargs):
        print("In CLASS Prepare")
        print("Prepare mcs", mcs)
        print("PREPARE *args", *args)
        for k, v in kwargs.items():
            print("NEW **kwargs", k, v)


mymet_instance = ExampleClass(1,2)
mymet_instance()


# Useful URLS:
# https://yasoob.me/2013/09/20/all-about-the-metaclasses-in-python/