"""
BEE 1026 -To Carry or not to Carry - Level 5 - Ad-hoc
"""


def dec_to_bin(number):
    n = number
    n_bin = ""
    while n != 0:
        n_bin += str(n % 2)
        n //= 2
    n_bin = n_bin[::-1]

    # s = "0" * (32 - len(n_bin))
    # return s + n_bin
    # s = n_bin.zfill(32)
    return n_bin


def to_int(n):
    return int(dec_to_bin(n))


n1, n2 = map(int, input().split())
t = max(len(n1), len(n2))
