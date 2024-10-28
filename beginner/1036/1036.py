"""
BEE 1036 - Bhaskara's Formula - Level 3 - Beginner
"""

from math import sqrt

a, b, c = map(float, input().split())

delta = pow(b, 2) - (4 * a * c)

if a > 0 and b > 0 and c > 0 and delta >= 0:
    r1 = (-b + (sqrt(delta))) / (2 * a)
    r2 = (-b - (sqrt(delta))) / (2 * a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
else:
    print("Impossivel calcular")
