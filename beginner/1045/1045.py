"""
BEE 1045 - Triangle Types - Level 4 - Beginner
"""

A, B, C = map(float, input().split())
if B > A:
    A, B = B, A
if C > A:
    A, C = C, A

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if pow(A, 2) == pow(B, 2) + pow(C, 2):
        print("TRIANGULO RETANGULO")
    if pow(A, 2) > pow(B, 2) + pow(C, 2):
        print("TRIANGULO OBTUSANGULO")
    if pow(A, 2) < pow(B, 2) + pow(C, 2):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B != C or A == C != B or B == C != A:
        print("TRIANGULO ISOSCELES")