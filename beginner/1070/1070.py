"""
BEE 1070 - Seis Números Ímpares - Level 1 - Beginner
"""

X = int(input())

if X % 2 == 0:
    X += 1

for i in range(0, 12, 2):
    print(X+i)
