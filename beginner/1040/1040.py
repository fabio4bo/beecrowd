"""
BEE 1040 - Average 3 - Level 5 - Beginner
"""

n1, n2, n3, n4 = map(float, input().split())

r_average = (2 * n1 + 3 * n2 + 4 * n3 + n4) / 10

print(f"Media: {r_average:.1f}")

if r_average >= 7:
    print("Aluno aprovado.")
elif r_average < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame_score = float(input())
    print(f"Nota do exame: {exame_score:.1f}")
    r_ex = (exame_score + r_average) / 2

    if r_ex >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {r_ex:.1f}")
