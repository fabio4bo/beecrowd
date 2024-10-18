"""
BEE 1174 -Array Selection I - Level 3 - Beginner
"""

list = [0] * 100

for i in range(len(list)):
    list[i] = float(input().strip())

for i in range(len(list)):
    if list[i] <= 10:
        print(f"A[{i}] = {list[i]}")
