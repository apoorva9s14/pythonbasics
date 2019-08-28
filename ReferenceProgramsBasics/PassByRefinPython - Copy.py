
#ids for the argument inside and outside are same, which shows that the argument is
#passed by reference
def changeme( mylist ):
    "This changes a passed list into this function"
    mylist.append([1,2,3,4])
    print("Values inside the function: ", mylist,id(mylist))
    return
# Now you can call changeme function
mylist = [10,20,30]
print(id(mylist))
changeme( mylist )
print("Values outside the function: ", mylist,id(mylist))
