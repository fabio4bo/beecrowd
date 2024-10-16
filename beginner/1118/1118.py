"""
BEE 1118 -Several Scores with Validation - Level 3 - Beginner
"""

while True:

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

    while True:
        print("novo calculo (1-sim 2-nao)")
        y = int(input())
        if y == 1 or y == 2:
            break

    if y == 2:
        break
