"""
BEE 1134 -Type of Fuel - Level 1 - Beginner
"""

type_fuel = {
    1: 0,
    2: 0,
    3: 0,
}

while True:
    t = int(input())

    if t == 4:
        break
    if 0 < t < 4:
        type_fuel[t] += 1

print("MUITO OBRIGADO")
print(f"Alcool: {type_fuel[1]}")
print(f"Gasolina: {type_fuel[2]}")
print(f"Diesel: {type_fuel[3]}")
