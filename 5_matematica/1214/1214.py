"""
BEE 1214 - Acima da Média - Nível 3 - Matemática
"""

c = int(input())

for _ in range(c):
    medias = [float(i) for i in input().strip().split(" ")]
    
    media_da_turma = sum(medias[1:]) / medias[0] 

    acima_da_media = len([i for i in medias[1:] if i > media_da_turma])

    percentagem = acima_da_media / medias[0] * 100
    print(f"{percentagem:.3f}%")
