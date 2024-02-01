N = 1
esferas = N

lista = [x for x in range(1, N+1)]
lista2 = []
for i in lista:
    soma = 0
    for j in range(1, i+1):
        if i % j == 0:
            soma+=1
    if soma % 2 == 1:
        lista2.append(lista.pop(i))

for i in lista2:
    print(i)