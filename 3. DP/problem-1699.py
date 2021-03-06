import sys
from functools import cache

input = sys.stdin.readline


def sumOfPoweredNums(N: int):
    # @cache
    # def findPoweredNum(n: int):
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     i = 1
    #     local_minimum = float("inf")
    #     while i * i < n:
    #         local_minimum = min(local_minimum, findPoweredNum(n - (i * i)))
    #         i += 1
    #     return local_minimum + 1

    # return findPoweredNum(N)

    cache = [0] * (N + 1)
    for n in range(1, N + 1):
        i = 1
        cache[n] = n
        while i * i < n:
            cache[n] = min(cache[n], cache[n - (i * i)] + 1)
            i += 1
    return cache[N]


# N = int(input())
# print(sumOfPoweredNums(N))


# import sys

N = int(sys.stdin.readline())

dp = [0] * 100001

for i in range(1, N + 1):
    dp[i] = i
    for j in range(1, i):
        if (j * j) > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
print(dp[N])