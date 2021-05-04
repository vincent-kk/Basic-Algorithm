import sys

input = sys.stdin.readline


def makeOne(X: int):
    cache = [-1] * (X + 1)
    cache[0] = cache[1] = 0

    for N in range(2, X + 1):
        local_minimum = N
        if N % 3 == 0:
            local_minimum = min(local_minimum, cache[N // 3])
        if N % 2 == 0:
            local_minimum = min(local_minimum, cache[N // 2])
        local_minimum = min(local_minimum, cache[N - 1])
        cache[N] = local_minimum + 1
    return cache[X]
    # def findStep(N: int):
    #     if N == 1:
    #         return 0
    #     if N in cache:
    #         return cache[N]

    #     local_minimum = N
    #     if N % 3 == 0:
    #         local_minimum = min(local_minimum, findStep(N // 3))
    #     if N % 2 == 0:
    #         local_minimum = min(local_minimum, findStep(N // 2))
    #     local_minimum = min(local_minimum, findStep(N - 1))
    #     cache[N] = local_minimum + 1
    #     return cache[N]

    # return findStep(X)


i = int(input())
print(makeOne(i))