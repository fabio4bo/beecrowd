"""
BEE 1113 -Ascending and Descending - Level 1 - Beginner
"""

while True:
    try:
        x, y = map(int, input().split())

        if x == y:
            break

        if x > y:
            print("Decrescente")
        elif x < y:
            print("Crescente")
    except EOFError:
        break
