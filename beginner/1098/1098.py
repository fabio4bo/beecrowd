"""
BEE 1098 - Sequence IJ 4 - Level 1 - Beginner
"""

from decimal import Decimal, getcontext

getcontext().prec = 2
i = Decimal(0)

while i <= Decimal(2):
    for j in range(1, 4):
        if float(i).is_integer():
            print(f"I={i:.0f} J={j+i:.0f}")
        else:
            print(f"I={i:.1f} J={j+i:.1f}")
    i += Decimal(0.2)
