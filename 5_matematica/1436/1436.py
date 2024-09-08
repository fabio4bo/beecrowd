"""
BEE 1436 - Jogo do Tijolo - Level 2 - Mathematics
"""

t = int(input())

for i in range(t):
    ages = [int(i) for i in input().strip().split(" ")]
    ages.pop(0)
    ages.sort()
    print(f"Case {i+1}: {ages[len(ages) // 2]}") # Mediana
