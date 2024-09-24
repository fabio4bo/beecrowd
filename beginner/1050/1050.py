"""
BEE 1050 - DDD - Level 2 - Beginner
"""

ddd = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte",
}

in_ddd = int(input())

if in_ddd in ddd:
    print(ddd[in_ddd])
else:
    print("DDD nao cadastrado")
