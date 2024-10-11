"""
BEE 1072 - Interval 2 - Level 1 - Beginner
"""

N = int(input())

n_in = 0
n_out = 0
for i in range(N):
    X = int(input())

    if 10 <= X <= 20:
        n_in += 1
    else:
        n_out += 1

print(f'{n_in} in')
print(f'{n_out} out')
