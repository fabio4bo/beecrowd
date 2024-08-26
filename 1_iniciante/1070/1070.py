"""
BEE 1070 - Seis Números Ímpares - Nível 1 - Iniciante
"""

X = int(input())

if X % 2 == 0:
    X += 1

for i in range(0, 12, 2):
    print(X+i)
