def mul_as_recursive_add(x,y):
    if x > y:
        y, x = x, y
        # To make x  the smallest of both
        # to perform addition of y , x times
    def add(x,y):
        if x == 0:
            return y
        x = x - 1
        y1 = y + add(x, y)
        return y1

print(mul_as_recursive_add(5,2))