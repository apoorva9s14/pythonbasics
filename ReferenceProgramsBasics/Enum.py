import enum
from enum import Enum


class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3


# Iterable Class
# With object name and object value
for shake in Shake:
    print(shake)
    print(shake.value)
