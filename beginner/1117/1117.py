"""
BEE 1117 -Score Validation - Level 1 - Beginner
"""

while True:
    n = float(input())
    if 0 <= n <= 10:
        break
    print("nota invalida")
while True:
    m = float(input())
    if 0 <= m <= 10:
        break
    print("nota invalida")

print(f"media = {(n+m) / 2:.2f}")
