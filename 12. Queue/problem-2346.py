import sys
from typing import Deque, List
from collections import deque

input = sys.stdin.readline


def solution(N: int, balloons: Deque[int]):
    result = []
    while True:
        pos, op = balloons.popleft()
        result.append(pos + 1)

        if not balloons:
            break
        if op > 0:
            balloons.rotate(-(op - 1))
        else:
            balloons.rotate(-op)
    return " ".join(map(str, result))


N = int(input())
B = deque(enumerate(map(int, input().split())))
print(solution(N, B))