"""
BEE 1169 - Trigo no Tabuleiro - Level 4 - Mathematics
"""


def resultado(n):
    graos = pow(2, n)

    return graos // 12.0 // 1000.0


n = int(input())

for _ in range(n):
    x = int(input())

    print(f"{int(resultado(x))} kg")
