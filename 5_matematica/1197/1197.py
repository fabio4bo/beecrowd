"""
BEE 1197 - Volta à Faculdade de Física - Nível 1 - Matemática 
"""

while True:
    try:
        velocidade, tempo = [int(i) for i in input().strip().split(" ")]
        print(2 * velocidade * tempo)
    except EOFError:
        break
