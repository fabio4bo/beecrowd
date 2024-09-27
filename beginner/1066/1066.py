"""
BEE 1066 - Even, Odd, Positive and Negative - Level 1 - Beginner
"""

even = 0
odd = 0
positive = 0
negative = 0
for i in range(5):
    number = int(input())

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1

print(
    f'{even} valor(es) par(es)\n'
    f'{odd} valor(es) impar(es)\n'
    f'{positive} valor(es) positivo(s)\n'
    f'{negative} valor(es) negativo(s)'
)