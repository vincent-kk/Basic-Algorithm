import sys
from typing import List

input = sys.stdin.readline


def solution(M: int, costs: List[int]):

    low, high = 0, max(costs)
    if sum(costs) <= M:
        return high

    while high > low + 1:
        pivot = (low + high) // 2
        total = 0
        for cost in costs:
            total += cost if cost < pivot else pivot

        if total < M:
            low = pivot
        elif total > M:
            high = pivot
        else:
            break

    return (low + high) // 2


N = int(input())
costs = list(map(int, input().split()))
M = int(input())

print(solution(M, costs))
