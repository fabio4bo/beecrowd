"""
BEE 1068 - Parenthesis Balance I - Level 5 - Data Structures and Libraries
"""

from collections import deque


def result(parentheses):
    stack = deque()
    for p in parentheses:
        if p == "(":
            stack.append(p)  # open
        elif p == ")":
            if len(stack) == 0:  # close before open
                return "incorrect"
            stack.pop()  # close
    if len(stack) > 0:
        return "incorrect"
    else:
        return "correct"


while True:
    try:
        print(result(input()))
    except EOFError:  # eof
        break
