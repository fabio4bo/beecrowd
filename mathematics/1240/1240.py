"""
BEE 1240 - Encaixa ou Não I - Level 2 - Mathematics
"""

def resposta(a, b):
    t = len(a) - len(b)

    if a[t:] == b:
        return "encaixa"
    else:
        return "nao encaixa"
    
n = int(input())

for _ in range(n):
    a, b = [i for i in input().strip().split(" ")]
    
    print(resposta(a, b))
