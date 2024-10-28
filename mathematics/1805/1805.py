"""
BEE 1805 - Soma Natural - Level 6 - Mathematics
"""

"""
Resolve-se com a soma dos termos de uma PA
a1 = termo inicial
an = último termo
n = quantidade de elementos;
Pode-se obter n com (an - a1 + 1) nesse caso porque a razão é 1

an = a1 + (n - 1) * r

fórmula da soma dos termos: Sm = ((a1 + an) * n) // 2
"""
a1, an = map(int, input().split())

n = an - a1 + 1

soma_dos_termos = ((a1 + an) * n) // 2

print(soma_dos_termos)
