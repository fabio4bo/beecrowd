"""
BEE 1021 - Banknotes and Coins - Level 6 - Beginner
"""

n = float(input())
moedas = int((n % 1) * 100)
n = int(n)

print(f"NOTAS:")
print(f"{n // 100} nota(s) de R$ 100.00")
n %= 100
print(f"{n // 50} nota(s) de R$ 50.00")
n %= 50
print(f"{n // 20} nota(s) de R$ 20.00")
n %= 20
print(f"{n // 10} nota(s) de R$ 10.00")
n %= 10
print(f"{n // 5} nota(s) de R$ 5.00")
n %= 5
print(f"{n // 2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{n % 2} moeda(s) de R$ 1.00")
print(f"{moedas // 50} moeda(s) de R$ 0.50")
moedas %= 50
print(f"{moedas // 25} moeda(s) de R$ 0.25")
moedas %= 25
print(f"{moedas // 10} moeda(s) de R$ 0.10")
moedas %= 10
print(f"{moedas // 5} moeda(s) de R$ 0.05")
print(f"{moedas % 5} moeda(s) de R$ 0.01")