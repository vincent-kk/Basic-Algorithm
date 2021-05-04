import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, M: int, budgets: List[int]):
    low, high = max(budgets), sum(budgets)
    optimal = high

    while high > low:
        pivot = (low + high) // 2

        free = 0
        withdraw = 1
        for budget in budgets:
            if free + budget > pivot:
                free = budget
                withdraw += 1
            else:
                free += budget

        if withdraw > M:
            low = pivot + 1
        else:
            high = pivot - 1
            optimal = high if optimal > high else optimal

    return optimal


if __name__ == "__main__":
    N, M = map(int, input().split())
    budgets = [int(input()) for _ in range(N)]

    print(solution(N, M, budgets))
