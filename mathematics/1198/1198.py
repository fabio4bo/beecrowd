"""
BEE 1198 - O Bravo Guerreiro Hashmat - Level 5 - Mathematics
"""

while True:
    try:
        x, y = [int(i) for i in input().strip().split(" ")]

        print(abs(x - y))

    except EOFError:  # eof
        break
