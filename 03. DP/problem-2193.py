import sys

input = sys.stdin.readline


def countPinartNumbers(N: int):
    cache = [[0, 0] for _ in range(N + 1)]
    cache[1] = [0, 1]
    for d in range(2, N + 1):
        cache[d][0] = cache[d - 1][0] + cache[d - 1][1]
        cache[d][1] = cache[d - 1][0]
    return cache[N][0] + cache[N][1]


i = int(input())
print(countPinartNumbers(i))
