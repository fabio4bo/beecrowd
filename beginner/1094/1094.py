"""
BEE 1094 - Experiments - Level 3 - Beginner
"""


dic = {
    'C': 0,
    'R': 0,
    'S': 0,
}

n = int(input())

for i in range(n):
    valor, key = [x for x in input().strip().split(' ')]

    dic[key] += int(valor)

total = dic["C"] + dic["R"] + dic["S"]
c = dic['C']
r = dic['R']
s = dic['S']

pc = c / total * 100
pr = r / total * 100
ps = s / total * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')

print(f'Percentual de coelhos: {pc:.2f} %')
print(f'Percentual de ratos: {pr:.2f} %')
print(f'Percentual de sapos: {ps:.2f} %')