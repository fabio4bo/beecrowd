"""
BEE 1161 - Soma de Fatoriais - Level 5 - Mathematics
"""


def fatorial(N):
    if N == 0 or N == 1:
        return 1
    return N * fatorial(N - 1)


while True:
    try:
        numbers = input().split()
        print(fatorial(int(numbers[0])) + fatorial(int(numbers[1])))
    except EOFError:  # eof
        break
