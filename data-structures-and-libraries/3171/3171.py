"""
BEE 3171 - String Led - Level 1 - Data Structures and Libraries
"""

def result(n, l):
    lista = []
    ol = []
    liga = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i != j:
                lista.append([i, j])
    for i in range(l):
        nl = [int(i) for i in input().split()]

        if nl in lista:
            ol.append(nl[0])
            ol.append(nl[1])
    ml = {i for i in range(1, n+1)}
    return  ml == set(ol) and liga >= l

N, L = map(int, input().split())

print(result(N, L))