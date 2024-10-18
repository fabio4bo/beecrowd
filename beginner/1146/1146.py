"""
BEE 1146 -Growing Sequences - Level 3 - Beginner
"""

while True:
    x = int(input())

    if x == 0:
        break

    s = "".join(f"{i} " if i != x else f"{i}" for i in range(1, x + 1))

    print(s)
