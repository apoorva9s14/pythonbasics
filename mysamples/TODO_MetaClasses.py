"""
MetaClass defines the behaviour of class  just like
Class defines the behaviour of instance

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


    @classmethod
    def __prepare__(mcs, *args, **kwargs):
        print("In MC Prepare")
        print("Prepare mcs", mcs)
        print("PREPARE *args", *args)
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
        return object.__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        """This call makes the instance callable
        Args are the args of instance"""
        print("CALL Cls", self)
        print("CALL *args", *args)
        for k, v in kwargs.items():
            print("CALL *kwargs", k, v)

    @classmethod
    def __prepare__(mcs, *args, **kwargs):
        print("In CLASS Prepare")
        print("Prepate mcs", mcs)
        print("PREPARE *args", *args)
        for k, v in kwargs.items():
            print("NEW **kwargs", k, v)


mymet_instance = ExampleClass(1,2)
mymet_instance()
