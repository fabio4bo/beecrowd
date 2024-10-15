"""
BEE 1235 - Inside Out - Level 5 - Strings
"""

n = int(input())

for i in range(n):
    text = input()  # presentation error if you put strip() here
    t = len(text)
    half = len(text) // 2

    right = text[half:]
    left = text[0:half]

    new_string = left[::-1] + right[::-1]

    print(new_string)