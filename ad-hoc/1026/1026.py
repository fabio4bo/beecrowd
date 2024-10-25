"""
BEE 1026 -To Carry or not to Carry - Level 5 - Ad-hoc
"""

while True:
    try:
        x, y = map(int, input().split())

        print(x ^ y)
    except EOFError:
        break
