"""
BEE 1149 - Summing Consecutive Integers - Level 1 - Beginner
"""

v = []
v = [int(x) for x in input().split(" ") if not (int(x) <= 0 and len(v) < 2)]

a = v[0]
n = v[1]
soma = 0
for i in range(n):
    soma += a + i

print(soma)
