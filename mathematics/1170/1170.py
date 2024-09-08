"""
BEE 1170 - Blobs - Level 3 - Mathematics
"""
#usa o algortimo de piso de um logaritmo
import math


def usando_math(n):
    return math.ceil(math.log2(n))


def usando_algoritmo_bruto(n):
    cont = 0
    while n > 1:
        n /= 2
        cont += 1
    return cont


n = int(input())

for i in range(n):
    c = float(input())
    print(f"{usando_algoritmo_bruto(c)} dias")
