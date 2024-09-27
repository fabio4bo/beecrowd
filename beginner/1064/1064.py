"""
BEE 1064 - Positives and Average - Level 2 - Beginner
"""

positives = 0
numbers_sum = 0
for i in range(6):
    number = float(input())

    if number > 0:
        positives += 1
        numbers_sum += number

print(f'{positives} valores positivos')
print(f'{numbers_sum / positives:.1f}')