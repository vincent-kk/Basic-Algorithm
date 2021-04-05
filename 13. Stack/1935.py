import sys
from typing import List

input = sys.stdin.readline


def doCalc(x: float, y: float, op: str):
    if op == "+":
        return x + y
    if op == "-":
        return y - x
    if op == "*":
        return x * y
    if op == "/":
        return y / x

    raise Exception("Wrong Operater")


def solution(line: List[str], nums: List[float]):
    number = {}
    index = 0
    operand: List[float] = []

    for op in line:
        if op.isalpha():
            if op not in number:
                number[op] = nums[index]
                index += 1
            operand.append(number.get(op))
        else:
            x = operand.pop()
            y = operand.pop()
            calc = doCalc(x, y, op)
            operand.append(calc)
    return "%0.2f" % (operand[0])


if __name__ == "__main__":
    N = int(input())
    line = list(input()[:-1])
    nums = [float(input()) for _ in range(N)]
    print(solution(line, nums))