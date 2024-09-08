"""
BEE 1199 - Conversão Simples de Base - Level 3 - Mathematics
"""

from re import X


while True:
    try:
        number = input()

        if number[0:2] == "0x":
            print(int(number, 0))

        elif int(number) == -1:
            break
        else:
            print(f"0x{int(number):X}")
    except EOFError:
        break
