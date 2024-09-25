"""
BEE 1060 - Positive Numbers - Level 1 - Beginner
"""

positive = 0

for i in range(6):
    number = float(input())
    if number > 0:
        positive += 1
print(f"{positive} valores positivos")
