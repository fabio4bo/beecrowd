"""
BEE 1279 - Ano Bissexto ou Ano não Bissexto - Level 6 - Mathematics
"""


def is_bissexto(year):
    if year % 4 == 0 and not year % 100 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


def is_huluculu(year):
    return True if year % 15 == 0 else False


def is_bulukulu(year):
    return True if year % 55 == 0 and is_bissexto(year) else False


flag = False
while True:
    try:
        if flag:
            print()
        year = int(input())
        
        if is_bissexto(year):
            print("This is leap year.")
        if is_huluculu(year):
            print("This is huluculu festival year.")
        if is_bulukulu(year):
            print("This is bulukulu festival year.")

        if not is_bissexto(year) and not is_huluculu(year) and not is_bulukulu(year):
            print("This is an ordinary year. ")

        flag = True
    except EOFError:  # eof
        break
