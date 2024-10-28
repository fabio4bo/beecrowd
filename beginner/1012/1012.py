"""
BEE 1012 - Area - Level 2 - Beginner
"""

pi = 3.14159
a, b, c = map(float, input().split())

area_tr = (a * c) / 2
print(f"TRIANGULO: {area_tr:.3f}")

area_c = pi * (c * c)
print(f"CIRCULO: {area_c:.3f}")

area_tz = ((a + b) * c) / 2
print(f"TRAPEZIO: {area_tz:.3f}")

area_q = b * b
print(f"QUADRADO: {area_q:.3f}")

area_r = a * b
print(f"RETANGULO: {area_r:.3f}")
