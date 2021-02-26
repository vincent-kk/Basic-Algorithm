import sys
import heapq
from typing import List


input = sys.stdin.readline


def solution(n: int, k: int, senssors: List):
    if n <= k:
        return 0
    senssors.sort()
    coverage = []
    for i in range(n - 1):
        # coverage.append(senssors[i + 1] - senssors[i])
        heapq.heappush(coverage, senssors[i] - senssors[i + 1])

    # coverage.sort()

    for _ in range(k - 1):
        # coverage.pop()
        heapq.heappop(coverage)
    # return sum(coverage)
    return -sum(coverage)


N = int(input())
K = int(input())
senssors = list(map(int, input().split()))

print(solution(N, K, senssors))
