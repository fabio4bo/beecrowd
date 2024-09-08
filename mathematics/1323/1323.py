"""
BEE 1323 - Feynman - Level 1 - Mathematics
"""


# Em um quadrado NxN
def quantidade_quadrados(n):
    if n == 1:
        return 1
    return n**2 + quantidade_quadrados(n - 1)


while True:
    try:
        n = int(input())

        if n == 0:
            break
        print(quantidade_quadrados(n))

    except EOFError:  # eof
        break
