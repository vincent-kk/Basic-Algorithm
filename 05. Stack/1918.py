import sys
from typing import List

input = sys.stdin.readline


def getPriority(op: str):
    if op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2
    return -1


def solution(line: List[str]):
    stack = []
    postfix = []

    for op in line:
        if op.isalpha():
            postfix.append(op)
        else:
            if op == "(":
                stack.append(op)
            elif op == ")":
                while len(stack):
                    s = stack.pop()
                    if s == "(":
                        break
                    postfix.append(s)
            else:
                while len(stack):
                    if getPriority(op) > getPriority(stack[-1]):
                        break
                    postfix.append(stack.pop())
                stack.append(op)

    while len(stack) > 0:
        s = stack.pop()
        if s == "(" or s == ")":
            continue
        postfix.append(s)
    return "".join(postfix)


if __name__ == "__main__":
    line = list(input()[:-1])
    print(solution(line))
