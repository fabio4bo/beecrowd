"""
BEE 1099 - Sum of Consecutive Odd Numbers II - Level 1 - Beginner
"""

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    soma = 0

    if y < x:
        y, x = x, y

    if x % 2 != 0:
        x += 1

    for i in range(x + 1, y, 2):
        soma += i

    print(soma)
