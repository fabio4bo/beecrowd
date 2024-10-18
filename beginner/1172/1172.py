"""
BEE 1172 -Array Replacement I - Level 1 - Beginner
"""

list = []
for i in range(10):
    num = int(input().strip())

    if num <= 0:
        list.append(1)
    else:
        list.append(num)

for i in range(len(list)):
    print(f'X[{i}] = {list[i]}')
