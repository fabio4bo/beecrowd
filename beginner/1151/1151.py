"""
BEE 1151 -Easy Fibonacci - Level 2 - Beginner
"""


def fibonacci(number):
    p = 0
    c = 1

    for i in range(number - 1):
        print(p, end=" ")
        c, p = p, c
        c += p
    print(p)


n = int(input().strip())

fibonacci(n)
