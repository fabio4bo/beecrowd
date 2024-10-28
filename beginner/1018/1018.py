"""
BEE 1018 - Banknotes - Level 4 - Beginner
"""

num = int(input())
cem = num // 100
aux = num % 100
cinquenta = aux // 50
aux %= 50
vinte = aux // 20
aux %= 20
dez = aux // 10
aux %= 10
cinco = aux // 5
aux %= 5
dois = aux // 2
aux %= 2
um = aux

print(
    f"{num}\n"
    f"{cem} nota(s) de R$ 100,00\n"
    f"{cinquenta} nota(s) de R$ 50,00\n"
    f"{vinte} nota(s) de R$ 20,00\n"
    f"{dez} nota(s) de R$ 10,00\n"
    f"{cinco} nota(s) de R$ 5,00\n"
    f"{dois} nota(s) de R$ 2,00\n"
    f"{um} nota(s) de R$ 1,00"
)
