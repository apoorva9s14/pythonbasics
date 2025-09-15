def happy_number(n):
    h=set()
    s=get_square(n)
    while s not in h:
        n=s
        h.add(s)
        s=get_square(n)
    print(h)
def get_square(n):
    s=0
    while n>0:
            d= n%10
            n//=10
            s=s+(d**2)
    return s
print(get_square(13))