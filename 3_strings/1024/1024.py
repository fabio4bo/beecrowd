#Criptografia
#usar função

#se for letra, muda para o terceiro caractere ASCII a frente A->D B->E
def first_step(texto):
    texto = list(texto)
    for i in range(len(texto)):
        if texto[i].isalpha():
            texto[i] = chr(ord(texto[i])+3)
    return ''.join(texto)

#inverte
def second_step(texto):
    novo_texto = texto[::-1] #usar isso fez a solução ter mais tempo de execução #0.919, por quê?
    return novo_texto

#inserindo no inicio, igual lista. como o tempo foi 0.694
def second_step2(texto): 
    tamanho_texto = len(texto)
    novo_texto = ""
    for i in texto:
        novo_texto = i + novo_texto
    return novo_texto

#metade direita: muda o caractere para o próximo na tabela ASCII. A->B C->D 
def third_step(texto):
    tamanho_texto = len(texto)
    texto_novo = texto[0:tamanho_texto//2]#metade esquerda

    for i in range(tamanho_texto//2, tamanho_texto):#metade direita
        texto_novo = texto_novo + chr(ord(texto[i])-1)
    return texto_novo

def encriptar(texto):
    texto = first_step(texto)
    texto = second_step(texto)
    texto = third_step(texto)

    return texto
#pesquisar formas de simplificar ainda mais


quantidade = int(input())

for i in range(quantidade):
    texto = input()
    print(encriptar(texto))
