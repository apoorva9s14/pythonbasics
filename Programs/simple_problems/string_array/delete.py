l =  {1, 3, 6, 10, 11, 15}
least_sum = 1
suml = 0
for i in l:
    suml = suml+ i
    if suml < least_sum:
        least_sum = suml
print(least_sum)
