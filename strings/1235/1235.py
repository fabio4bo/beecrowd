"""
BEE 1235 - Inside Out - Level 5 - Strings
"""

n = int(input())

for i in range(n):
    texto = input().strip().upper()
    t = len(texto)
    # print(t)
    metade = t // 2

    if t % 2 == 0:
        p1 = texto[metade:]
        p2 = texto[:metade]
    else:
        p1 = texto[:metade].strip()
        p2 = texto[metade:]

    ns = (p2[::-1]+p1[::-1]).strip()
    print(ns)