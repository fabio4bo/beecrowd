"""
BEE 1131 -Grenais - Level 1 - Beginner
"""

inter = 0
gremio = 0
draws = 0
grenais = 0
while True:
    x, y = map(int, input().split())

    if x == y:
        draws += 1
    elif x > y:
        inter += 1
    elif y > x:
        gremio += 1
    grenais += 1

    print("Novo grenal (1-sim 2-nao)")

    r = int(input())

    if r == 2:
        break

if inter > gremio:
    rf = "Inter venceu mais"
elif gremio > inter:
    rf = "Gremio venceu mais"
else:
    rf = "Não houve vencedor"

print(f"{grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{draws}")
print(rf)
