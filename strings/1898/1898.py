"""
BEE 1898 -Kickback Sum - Level 9 - Strings - Accepted
"""

from math import floor


def truncate(f, n):  # para não arredondar decimal
    return floor(f * 10**n) / 10**n


def get_decimal(text):
    ponto = text.find(".")
    decimal = ""
    for i in text[ponto + 1 :]:
        if i.isdigit():
            decimal += i
        else:
            break
    return decimal


text_1 = "".join(i for i in input() if i.isdigit() or i == ".")
text_2 = "".join(i for i in input() if i.isdigit() or i == ".")

ponto = text_1.find(".")
if ponto == -1:
    number_1 = int(text_1[11:])
else:
    decimal1 = get_decimal(text_1)
    number_1 = truncate(float("".join([text_1[11 : ponto + 1], decimal1])), 2)

ponto = text_2.find(".")
if ponto == -1:
    number_2 = int(text_2)
else:
    decimal = get_decimal(text_2)
    number_2 = truncate(float("".join([text_2[: ponto + 1], decimal])), 2)


print(f"cpf {text_1[:11]}")
print(f"{number_1 + number_2:.2f}")
