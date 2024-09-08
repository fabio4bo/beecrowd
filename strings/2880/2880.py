mensagem = list(input())
crib = list(input())

tamanho_mensagem = len(mensagem)
tamanho_crib = len(crib)
cont = 0

for i in range(tamanho_mensagem-tamanho_crib+1):
    boole = False
    substring_aux = mensagem[i:tamanho_crib+i]
    for j in range(len(tamanho_crib)):
        if(crib[j] == substring_aux[j]):
            boole = True;break
    if boole == False:
        cont+=1
print(cont)