"""
BEE 1051 - Taxes - Level 2 - Beginner
"""


def increase_tax(salary):
    tax = 0
    if 0 <= salary <= 2000:
        return "Isento"
    elif 2000 < salary <= 3000:
        tax = (salary - 2000) * 0.08
    elif 3000 < salary <= 4500:
        tax = 1000 * 0.08
        salary -= 3000
        tax += salary * 0.18
    elif 4500 < salary:
        tax = 1000 * 0.08
        tax += 1500 * 0.18
        salary -= 4500
        tax += salary * 0.28

    return f"R$ {tax:.2f}"


salary = float(input())
print(increase_tax(salary))
