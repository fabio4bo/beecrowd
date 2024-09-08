"""
BEE 1585 - Fazendo Pandorgas - Level 1 - Mathematics
"""
import math
n = int(input())

for i in range(n):
    x, y = [int(i) for i in input().strip().split(" ")]
    result = x / 2.0 * y
    print(f"{math.floor(result)} cm2")
