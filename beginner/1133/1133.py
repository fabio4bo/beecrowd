"""
BEE 1133 -Rest of a Division - Level 3 - Beginner
"""

x = int(input())
y = int(input())

if x > y:
    y, x = x, y

for i in range(x + 1, y):
    r = i % 5

    if r == 2 or r == 3:
        print(i)
