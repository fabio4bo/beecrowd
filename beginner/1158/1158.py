"""
BEE 1158 -Sum of Consecutive Odd Numbers III - Level 1 - Beginner
"""

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    if not (x % 2 == 0):
        x -= 1

    s = sum([(x + i) for i in range(1, y * 2, 2)])

    print(s)
