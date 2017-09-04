#Diff_bw_filter_map. Explanation of zip
#1. Filter just filters out and returns the items in sequence which follows the fn criteria
#2. Map applies that fn to the sequence and returns the output of - applying that fn on individual elements of the sequence 
#3. Using one liner lambda and giving it a name -s
#4. zip. zip(*zipped_list)



y=list(range(10))  #list of single digit numbers
x=list(range(10,100))   #list of double digit numbers

s=lambda x:x>=10 and x<=99 #Defining a function which takes only double digit numbers


f=list(filter(s,y))
#gives []
m=list(map(s,y))
#gives [False, False, False, False, False, False, False, False, False, False]
print(f,m)

'''O/p is

[] [False, False, False, False, False, False, False, False, False, False]
'''

f1=list(filter(s,x))
m1=list(map(s,x))
print(f1,m1)


'''O/p is 
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
 90, 91, 92, 93, 94, 95, 96, 97, 98, 99] [True, True, True, True, True, True, Tr
ue, True, True, True, True, True, True, True, True, True, True, True, True, True
, True, True, True, True, True, True, True, True, True, True, True, True, True,
True, True, True, True, True, True, True, True, True, True, True, True, True, Tr
ue, True, True, True, True, True, True, True, True, True, True, True, True, True
, True, True, True, True, True, True, True, True, True, True, True, True, True,
True, True, True, True, True, True, True, True, True, True, True, True, True, Tr
ue, True, True, True]
'''

#Zip

l=[1, 2, 3]
l1=[4,5,6]
z=list(zip(l1,l))
#gives [(4, 1), (5, 2), (6, 3)]
#z[0](4, 1)
#type(z[0])=tuple

#So, zip combines two sequences and merges them in pairs, and stores the individual pairs in tuple

#Case1- If sequences are of unequal length

l2=[7,8]
l3=[9,10,11]
z1=list(zip(l2,l3))
#gives [(7, 9), (8, 10)]
#it is truncated to the least size, that is - 2

#zip(*zipped_list)
#zip with * will unpack a zipped_list(lists of x*y dimensions) = Equivalent to unpacking multidimensional lists
#Zip to zip up two sequences, *of the zipped result to unzip the zipped result

x = [1, 2, 3]
y = [4, 5, 6]
zipped = list(zip(x, y))
#gives [(1, 4), (2, 5), (3, 6)]

x2, y2 = zip(*zip(x, y))
#gives x2 as (1, 2, 3), y2 as (4, 5, 6)



