"""
BEE 1038 - Snack - Level 1 - Beginner
"""

dic = {
    1: 4,
    2: 4.5,
    3: 5,
    4: 2,
    5: 1.5,
}

code, qty = map(int, input().split())

total = dic[code] * qty
print(f"Total: R$ {total:.2f}")
