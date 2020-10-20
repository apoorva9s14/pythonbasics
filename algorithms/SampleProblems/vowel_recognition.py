# https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/practice-problems/algorithm/vowel-game-f1a1047c/submissions/
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from itertools import combinations
# t = int(input())
t = 1
inp_strs = ["MOUURVqrpL"]
# for i in range(t):
#     inp_strs.append(input())
# print(inp_strs)
def find_all_substr(inp_str):
    res = [inp_str[x:y] for x, y in combinations(range(len(inp_str) + 1), r = 2)]
    return set(res)
def find_vowels(inp_str):
    vowel_count = 0
    for each_vowel in "aeiouAEIOU":
        if each_vowel in inp_str:
            vowel_count += inp_str.count(each_vowel) 
    return vowel_count

def vowel_count(inp_str):
    sub_strs = find_all_substr(inp_str)
    vowel_count = 0
    for each_str in sub_strs:
        vowel_count+= find_vowels(each_str)
    return vowel_count

for each_str in inp_strs:
    print(vowel_count(each_str))

for _ in range(1):

        string = "MOUURVqrpL"

        vowels, length = 0, len(string)

        for i in range(length):

                 vowels+=(length-i)*(i+1) if string[i].lower() in 'aeiou' else 0

        print(vowels)