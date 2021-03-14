import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, M: int, tasks: List[int]):

    low, high = max(tasks), sum(tasks)

    while high > low + 1:
        pivot = (low + high) // 2

        free = pivot
        disks = 1
        for task in tasks:
            free -= task
            if free < 0:
                disks += 1
                free = pivot - task
            if free == 0:
                disks += 1
                free = pivot

        if disks > M:
            low = pivot
        else:
            high = pivot

    return (low + high) // 2


N, M = map(int, input().split())
tasks = list(map(int, input().split()))

print(solution(N, M, tasks))
