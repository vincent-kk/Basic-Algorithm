import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, M: int, trees: List[int]):
    low, high = 0, max(trees)
    while high > low + 1:
        pivot = (low + high) // 2
        local_sum = 0
        for tree in trees:
            if pivot >= tree:
                continue
            local_sum += tree - pivot

        if local_sum > M:
            low = pivot
        elif local_sum < M:
            high = pivot
        else:
            break

    return (low + high) // 2


N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(solution(N, M, trees))
