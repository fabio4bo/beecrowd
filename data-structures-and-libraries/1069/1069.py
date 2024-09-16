"""
BEE 1069 - Diamonds and Sand - Level 3 - Data Structures and Libraries
"""

from collections import deque


def mining(source):
    stack = deque()
    diamond = 0
    for p in source:
        if p == "<":
            stack.append(p)
        elif p == ">":
            if len(stack) > 0:
                diamond += 1
                stack.pop()
    return diamond

N = int(input())

for i in range(N):
    print(mining(input()))