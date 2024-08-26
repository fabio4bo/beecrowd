"""
BEE 1805 - Soma Natural - Nível 6 - Matemática
"""

"""
Resolve-se com a soma dos termos de uma PA
a1 = termo inicial
an = último termo
n = quantidade de elementos; 
Pode-se obter n com (an - a1 + 1)
fórmula da soma dos termos: sm = ((a1 + an) * n) // 2
"""
entrada = input().split(" ")

a1 = int(entrada[0])
an = int(entrada[1])
n = an - a1 + 1

soma_dos_termos = ((a1 + an) * n) // 2

print(soma_dos_termos)
