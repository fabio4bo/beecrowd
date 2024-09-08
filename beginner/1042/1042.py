"""
BEE 1042 - Simple Sort - Level 2 - Beginner
"""

numbers = [int(i) for i in input().strip().split(" ")]

original_sort = [i for i in numbers]
numbers.sort()

for i in numbers:
    print(i)
print()
for i in original_sort:
    print(i)
