"""
BEE 1043 - Triangle - Level 2 - Beginner
"""

A, B, C = map(float, input().split())

if A + B > C and A + C > B and B + C > A:
    perimeter = A + B + C
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = ((A + B)/ 2) * C
    print(f"Area = {area:.1f}")