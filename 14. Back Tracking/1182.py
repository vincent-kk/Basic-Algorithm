import sys
from typing import List

input = sys.stdin.readline


def solution(N, S, array: List[int]):
    answer = 0

    def dfs(prev_sum: int, index: int):
        if index == N:
            return

        if prev_sum + array[index] == S:
            nonlocal answer
            answer += 1

        dfs(prev_sum, index + 1)
        dfs(prev_sum + array[index], index + 1)

    dfs(0, 0)

    return answer


N, S = map(int, input().split())
array = list(map(int, input().split()))

print(solution(N, S, array))
