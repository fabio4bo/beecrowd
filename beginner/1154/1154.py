"""
BEE 1154 -Ages - Level 1 - Beginner
"""

v = []
while True:
    n = int(input())

    if n < 0:
        break
    v.append(n)

soma = sum(v)
t = len(v)
print(f"{soma/t:.2f}")
