#Figurinhas
#20:12

#MDC com Algoritmo de Euclides com 2 números apenas
#Ai, mas não precisa aprender matemática.
def mdc(A, B):
    if B == 0: #base, quando o resto da divisão for zero, para porque achamos o mdc
        return A
    return mdc(B, A % B)


quantity = int(input())

for i in range(quantity):
    numbers = input().split()
    print(mdc(int(numbers[0]), int(numbers[1])))

# TODO
# ?
# !
# //
# * hi 

