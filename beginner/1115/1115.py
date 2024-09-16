"""
BEE 1115 - Quadrant - Level 1 - Beginner
"""

while True:
    try:
        X, Y = map(int, input().split())
        if not X or not Y:
            break

        if X > 0:
            if Y > 0:
                print("primeiro")
            else:
                print("quarto")
        else:
            if Y > 0:
                print("segundo")
            else:
                print("terceiro")

    except EOFError:
        break
