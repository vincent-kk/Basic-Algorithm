import sys
from typing import List
from functools import cache

input = sys.stdin.readline


def findMinimum(N: int, target: int, coins: List[int]):
    if N == 0:
        return -1
    cache = [-1] * (target + 1)
    for budget in range(1, target + 1):
        if budget in coins:
            cache[budget] = 1
            continue
        local_minimum = -2
        for coin in coins:
            if cache[max(budget - coin, 0)] < 0:
                continue
            local_minimum = (
                cache[budget - coin]
                if local_minimum < 0
                else min(local_minimum, cache[budget - coin])
            )
        cache[budget] = local_minimum + 1
    return cache[target]
    # @cache
    # def takeCoin(n: int):
    #     if n == 0:
    #         return -1
    #     if n in coins:
    #         return 1
    #     local_minimum = -2
    #     for coin in coins:
    #         temp = takeCoin(max(n - coin, 0))
    #         if temp < 0:
    #             continue
    #         local_minimum = temp if local_minimum < 0 else min(local_minimum, temp)
    #     return local_minimum + 1

    # return takeCoin(target)


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
print(findMinimum(n, k, coins))
