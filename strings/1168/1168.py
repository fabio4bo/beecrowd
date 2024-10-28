"""
BEE 1168 - LED - Level 3 - Strings
"""

d = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

n = int(input())

for i in range(n):
    count = 0
    numbers = [int(i) for i in list(input())]

    for n in numbers:
        count += d[n]

    print(f"{count} leds")
