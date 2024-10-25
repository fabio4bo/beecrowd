"""
BEE 1159 -Sum of Consecutive Even Numbers - Level 2 - Beginner
"""

while True:
    x = int(input())

    if x == 0:
        break

    if x % 2 == 0:
        x -= 1

    s = sum([(x + i) for i in range(1, 11, 2)])

    print(s)
