"""
BEE 2191 - Saldo de Gols - Level 8 - Ad-hoc
"""

testes = 0
while True:
    try:
        n = int(input())

        if n == 0:
            break

        testes += 1
        s_maior = -1
        s_atual = 0
        primeiro = 0
        temp_primeiro = 0
        ultimo = 0

        for i in range(n):
            x, y = [int(i) for i in input().strip().split(" ")]
            s = x - y
            s_atual += s

            if s_atual < 0:
                s_atual = 0
                temp_primeiro = i + 1
            if s_atual >= s_maior:
                s_maior = s_atual
                primeiro = temp_primeiro
                ultimo = i

        print(f"Teste {testes}")
        if s_maior > 0:
            print(f"{primeiro+1} {ultimo+1}")
            print()
        else:
            print("nenhum")
            print()
    except EOFError:  # eof
        break
