"""
BEE 1071 - Sum of Consecutive Odd Numbers I - Level 2 - Beginner
"""
X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

odd_sum = 0
for i in range(X+1, Y):
    if i % 2 == 1:
        odd_sum+=i

print(odd_sum)