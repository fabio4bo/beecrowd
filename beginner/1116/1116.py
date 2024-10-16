"""
BEE 1116 -Dividing X by Y - Level 1 - Beginner
"""

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    if y == 0:
        print("divisao impossivel")
    else:
        print(f"{x / y:.1f}")
