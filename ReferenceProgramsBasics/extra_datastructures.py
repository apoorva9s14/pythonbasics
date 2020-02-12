# Covers Datastructures other than the builtins
# Namedtuple, Struct


################################################
# Named Tuple
################################################
from collections import namedtuple

Car = namedtuple('Car', ['color','mileage'])

my_car = Car('red', 3812.4)
# my_car.color, my_car.mileage
# my_car[0], my_car[1]


################################################
# Struct
################################################
from struct import Struct
# pack and unpack Struct
MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)
print(data)
# will print blob of data
MyStruct.unpack(data)
