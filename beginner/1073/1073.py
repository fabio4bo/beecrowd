"""
BEE 1073 - Even Square - Level 1 - Beginner
"""

N = int(input())

for i in range(2, N + 1, 2):
    print(f'{i}^2 =', pow(i, 2))
