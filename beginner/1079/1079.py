"""
BEE 1079 - Wighted Averages - Level 1 - Beginner
"""

N = int(input())

for i in range(N):
    n = [float(x) for x in input().strip().split(' ')]
    average = (2 * n[0] + 3 * n[1] + 5 * n[2]) / 10
    print(f'{average:.1f}')
