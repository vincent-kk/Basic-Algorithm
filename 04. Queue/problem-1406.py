import sys
from collections import deque
from typing import List

input = sys.stdin.readline


def solution(string: str, operations: List[str]):
    left, right = deque(string), deque([])
    for op in operations:
        if op[0] == "P":
            left.append(op[1])
        else:
            if op[0] == "B" and left:
                left.pop()
            if op[0] == "L" and left:
                right.appendleft(left.pop())
            if op[0] == "D" and right:
                left.append(right.popleft())

    for ch in right:
        left.append(ch)

    return "".join(left)


string = input().rstrip()
N = int(input())
operations = [input().rsplit() for _ in range(N)]
print(solution(string, operations))