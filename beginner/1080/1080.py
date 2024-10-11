"""
BEE 1080 - Highest and Position - Level 2 - Beginner
"""

lista = []
for i in range(100):
    N = int(input())
    lista.append(N)

print(max(lista), lista.index(max(lista)) + 1, sep='\n')
