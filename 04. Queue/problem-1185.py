import sys
from collections import deque

input = sys.stdin.readline


def solution(n: int, step: int):
    origen = deque(range(1, n + 1))
    result = []
    while len(origen) > 0:
        for _ in range(step - 1):
            origen.append(origen.popleft())
        result.append(origen.popleft())
    return result


N, S = map(int, input().split())
out = solution(N, S)
print("<", end="")
for o in out[:-1]:
    print(o, end=", ")
print(out[-1], end=">")
