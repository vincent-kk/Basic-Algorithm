import sys

# from functools import cache

input = sys.stdin.readline


def solution(N: int, K: int):
    __cache__ = {}
    __cache__[(1, 1)] = 1
    __cache__[(1, 0)] = 1

    for n in range(2, N + 1):
        for k in range(n + 1):
            if k == n or k == 0:
                __cache__[(n, k)] = 1
            else:
                if k == 0:
                    __cache__[(n, k)] = __cache__[(n - 1, k)]
                else:
                    __cache__[(n, k)] = (
                        __cache__[(n - 1, k)] % 10007
                        + __cache__[(n - 1, k - 1)] % 10007
                    ) % 10007

    return __cache__[(N, K)]


N, K = map(int, input().split())
print(solution(N, K))