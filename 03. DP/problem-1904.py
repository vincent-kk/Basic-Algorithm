import sys

input = sys.stdin.readline


def findBinery(N: int):
    cache = [-1] * (N + 1)

    # base
    cache[1] = 1
    if N > 1:
        cache[2] = 2

    # steps
    for i in range(3, N + 1):
        cache[i] = ((cache[i - 1] % 15746) + (cache[i - 2] % 15746)) % 15746

    return cache[N]


i = int(input())
print(findBinery(i))