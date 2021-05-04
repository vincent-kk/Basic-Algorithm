from sys import stdin
from typing import Deque, List
from collections import deque

input = stdin.readline


def solution(N: int, M: int, priority: List[int]):
    printer = deque()
    for i, p in enumerate(priority):
        printer.append((i, p))
    priority.sort()
    order = 0
    while len(printer) > 0:
        task = printer.popleft()

        if task[1] < priority[-1]:
            printer.append(task)
        else:
            priority.pop()
            order += 1
            if task[0] == M:
                break
    return order


if __name__ == "__main__":
    L = int(input())
    for _ in range(L):
        N, M = map(int, input().split())
        priority = list(map(int, input().split()))
        print(solution(N, M, priority))
