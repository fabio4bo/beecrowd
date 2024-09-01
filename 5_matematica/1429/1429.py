"""
BEE 1429 - Fatorial de Novo! - Nível 1 - Matemática
"""


def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


while True:
    try:
        entrada = list(input())

        if int(entrada[0]) == 0:
            break
        soma = 0
        t = len(entrada)
        for i in range(t):
            soma += int(entrada[i]) * fatorial(t - i)

        print(soma)

    except EOFError:  # eof
        break
