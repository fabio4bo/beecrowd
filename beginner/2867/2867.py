"""
BEE 2867 - Digits - Level 5 - Beginner
"""

C = int(input())


for i in range(C):
    N, M = map(int, input().split())

    digits = len(str(int(pow(N, M))))

    print(digits)