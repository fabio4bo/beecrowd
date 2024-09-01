"""
BEE 1555 - Funções - Nível 1 - Matemática
"""
def Rafael (x , y):
    return(3 * x) ** 2 + y ** 2

def Beto (x, y):
    return 2 * (x * x) + (5 * y) ** 2

def Carlos (x, y):
    return -100 * x + y ** 3

n = int(input())

for i in range(n):
    x, y = [int(i) for i in input().strip().split()]

    rafael = Rafael(x, y)
    beto = Beto(x, y)
    carlos = Carlos(x, y)

    maior = rafael;
    nome = "Rafael"

    if beto > maior:
        maior = beto
        nome = "Beto"
    
    if carlos > maior:
        maior = carlos
        nome = "Carlos"
    
    print(f"{nome} ganhou")
    




