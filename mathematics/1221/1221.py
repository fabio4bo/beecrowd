"""
BEE 1221 - Primo Rápido - Level 6 - Mathematics
"""

import math


def prime(n):
    primo = True # ?

    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n > 2:
        raiz = math.ceil(math.sqrt(n)) + 1

        for i in range(2, raiz):
            if n % i == 0:
                return False
    return True


n = int(input())

for i in range(n):
    x = int(input())

    if prime(x):
        print("Prime")
    else:
        print("Not Prime")
