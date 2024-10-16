"""
BEE 1143 -Squared and Cubic - Level 1 - Beginner
"""

n = int(input())

for i in range(1, n + 1):
    square = pow(i, 2)
    cube = pow(i, 3)

    print(f"{i} {square} {cube}")
