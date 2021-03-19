import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, M: int, targets: List[int]):
    queue = list(range(1, N + 1))
    length = N
    position = 0
    operations = 0
    for target in targets:
        target = queue.index(target)
        forword = abs(position - target)
        backword = length + (
            (target - position) if position > target else (position - target)
        )

        if forword < backword:
            operations += forword
        else:
            operations += backword
        queue.pop(target)
        position = target
        length -= 1
    return operations


N, M = map(int, input().split())
targets = list(map(int, input().split()))
print(solution(N, M, targets))
