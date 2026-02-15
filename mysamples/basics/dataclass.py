# Dataclass makes creation of instance attributes easier
from dataclasses import dataclass


@dataclass
class Sample:
    inst_arg: int
    class_arg = 100

    def inst_method(self,x):
        return self.inst_arg + x

    @classmethod
    def class_method(cls,x):
        return cls.class_arg + x

s = Sample(10)
print(s.inst_method(1))
print(s.class_method(1))