class SampleClass(object):
    _cls_instances_list = []

    def __new__(cls, *args, **kwargs):
        """Static Method"""
        print("In New")
        print("NEW Cls", cls)
        print("NEW *args", *args)
        for k, v in kwargs.items():
            print("NEW **kwargs", k, v)
        return object.__new__(cls)

    def __call__(self, *args, **kwargs):
        """This call makes the instance callable
        Args are the args of instance"""
        print("CALL Cls", self)
        print("CALL *args", *args)
        for k, v in kwargs.items():
            print("CALL *kwargs", k, v)


s = SampleClass(1, 2, {"a": 1}, x=1)
s(1, 2, x=1)


