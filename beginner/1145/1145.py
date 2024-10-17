"""
BEE 1145 -Logical Sequence 2 - Level 2 - Beginner
"""

x, y = map(int, input().split())


for i in range(1, y + 1):
    if i % x == 0:
        print(i)
    else:
        print(i, end=" ")
