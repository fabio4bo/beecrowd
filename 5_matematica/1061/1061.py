"""
BEE 1061 - Tempo de um Evento - Nível 3 - Matemática
"""

dia_em_seg = 24 * 60 * 60

dia_inicio = int(input().strip().split(" ")[1])
hora_inicio = [int(i) for i in input().strip().split(" : ")]
dia_termino = int(input().strip().split(" ")[1])
hora_termino = [int(i) for i in input().strip().split(" : ")]


tempo_dia1 = dia_em_seg - (hora_inicio[0] * 3600 + hora_inicio[1] * 60 + hora_inicio[2])
tempo_ultimo_dia = hora_termino[0] * 3600 + hora_termino[1] * 60 + hora_termino[2]

tempo_dia1e2 = tempo_dia1 + tempo_ultimo_dia
w = dia_termino - dia_inicio - 1
w += tempo_dia1e2 // dia_em_seg
x = tempo_dia1e2 % dia_em_seg // 3600
y = tempo_dia1e2 % dia_em_seg % 3600 // 60
z = tempo_dia1e2 % dia_em_seg % 3600 % 60


print(f"{w} dia(s)\n{x} hora(s)\n{y} minuto(s)\n{z} segundo(s)")
