entrada = input()

words = entrada.split()
new_text = ""
for i in range(len(words)):
    for j in range(1, len(words[i]), 2):
        new_text = new_text + words[i][j]    
    if i < len(words)-1:#para não colocar espaço no final. Presentation Error
        new_text = new_text + " "    
print(new_text)
