d = {1:[1], 2:[2], 3:[3]}
#####Call By Ref####
for key, val in d.items():
    val[0] = 1
print(d)
# prints
# {1: [1], 2: [1], 3: [1]}

d = {1:[1], 2:[2], 3:[3]}
#####Call By Value####
for key, val in d.items():
    val = 1
print(d)
# prints
# same d
