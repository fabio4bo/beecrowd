"""
BEE 1047 - Game Time with Minutes - Level 9 - Beginner
"""

i_hora, i_minute, f_hora, f_minute = map(int, input().split())

r_hora = (24 - i_hora) - (24 - f_hora)
r_minute = (f_minute - i_minute) % 60

if r_hora == 0 and r_minute == 0:
    r_hora = 24
if (60 - i_minute + f_minute) // 60 == 0:
    r_hora -= 1
if r_hora < 0:
    r_hora += 24

print(f"O JOGO DUROU {r_hora} HORA(S) E {r_minute} MINUTO(S)")