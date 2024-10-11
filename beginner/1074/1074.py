"""
BEE 1074 - Even or Odd - Level 2 - Beginner
"""

N = int(input())

for i in range(N):
    X = int(input())

    if X % 2 == 0:
        if X > 0:
            print('EVEN POSITIVE')
        if X == 0:
            print('NULL')
        if X < 0:
            print('EVEN NEGATIVE')
    else:
        if X > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')
