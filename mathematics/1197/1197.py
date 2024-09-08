"""
BEE 1197 - Volta à Faculdade de Física - Level 1 - Mathematics 
"""

while True:
    try:
        velocidade, tempo = [int(i) for i in input().strip().split(" ")]
        print(2 * velocidade * tempo)
    except EOFError:
        break
