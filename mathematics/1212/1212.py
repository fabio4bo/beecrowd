"""
BEE 1212 - Aritmética Primária - Level 8 - Mathematics
"""

while True:
    try:
        x, y = [int(i) for i in input().strip().split(" ")]
        if x == 0 and y == 0:  # Wrong answer (85%) se for OR
            break
        cont = 0
        aux = 0
        while x or y:  # Wrong answer (5%) se for AND
            if (x % 10) + (y % 10) + aux > 9:
                cont += 1
                aux = 1
            else:
                aux = 0
            x //= 10
            y //= 10

        if cont == 0:
            texto = "No carry operation."
        elif cont == 1:
            texto = "1 carry operation."
        else:
            texto = f"{cont} carry operations."
        print(texto)
    except EOFError:  # eof
        break
