import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, K: int, D: int, rules: List[int]):
    return rules


if __name__ == "__main__":
    N, K, D = map(int, input().split())
    rules = [list(map(int, input().split())) for _ in range(K)]
    print(solution(N, K, D, rules))
