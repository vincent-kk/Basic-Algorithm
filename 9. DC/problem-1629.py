import sys
from functools import cache

input = sys.stdin.readline


def solution(N: int, P: int, M: int):
    @cache
    def power_and_mod(P):
        if P == 1:
            return N % M
        return (power_and_mod(P // 2) % M) * (power_and_mod(P // 2 + P % 2) % M) % M

    return power_and_mod(P)


A, B, C = map(int, input().split())

print(solution(A, B, C))
