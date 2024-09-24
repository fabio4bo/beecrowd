"""
BEE 1837 - Preface - Level 7 - Beginner
"""

A, B = map(int, input().split())

remainder = A % abs(B)
if A > 0:
    quotient = A / B
else:
    if B > 0:
        quotient = A // B
    if B < 0:
        quotient = abs(A // abs(B))
print(int(quotient), remainder)