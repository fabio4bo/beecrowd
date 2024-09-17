"""
BEE 1120 - Contract Revision - Level 5 - Strings
"""

while True:
    try:
        d, n = [i for i in input().strip().split(" ")]

        if d == "0" and n == "0":
            break

        new_s = "0"

        for i in n:
            if i != d:
                new_s += i

        print(int(new_s))
    except EOFError:
        break
