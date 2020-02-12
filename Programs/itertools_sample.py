# >>> list(itertools.zip_longest([1,2],[3,4,5]))
# [(1, 3), (2, 4), (None, 5)]
# >>> list(zip([1,2],[3,4,5]))
# [(1, 3), (2, 4)]
import itertools


# -------------------------------------------------------------------
# Combinations --> nCr = n!/r!*(n-r)!
# combination of r things out of n things
# myncr_combinations = itertools.combinations([1,2,3,4,5], 3)
# myncr_list = list(myncr_combinations)
# print(len(myncr_list))


# To find what all combinations give sum of 100
# three $20 dollar bills, five $10 dollar bills,
# two $5 dollar bills, and five $1 dollar bills.

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
makes_100 = []
for n in range(1, len(bills) + 1):
    for combination in itertools.combinations(bills, n):
        if sum(combination) == 100:
            makes_100.append(combination)


print(makes_100)
# -------------------------------------------------------------------
# Counting with itertools

evens = itertools.count(step=2)
odds = itertools.count(start=1, step=2)
# Default start is 0
# Generates infinite iterator of even numbers