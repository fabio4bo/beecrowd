#Soma de Fatoriais

def fatorial(N):# tem essa função em math
    if N == 0 or N == 1:
        return 1
    else:
        return N * fatorial(N-1)

while True:
    try:
        numbers = input().split()
        print(fatorial(int(numbers[0])) + fatorial(int(numbers[1])))
    except EOFError:#eof
        break    