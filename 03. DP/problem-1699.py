import sys
import collections

input = sys.stdin.readline


def sumOfPoweredNums(N: int):
    cache = collections.defaultdict(int)
    for n in range(1, N + 1):
        i = 1
        cache[n] = n
        while True:
            if i * i > n:
                break
            if cache[n] > cache[n - (i * i)] + 1:
                cache[n] = cache[n - (i * i)] + 1
            i += 1
    return cache[N]


N = int(input())
print(sumOfPoweredNums(N))


# import sys

# N = int(sys.stdin.readline())

# dp = [0] * 100001

# for i in range(1, N + 1):
#     dp[i] = i
#     for j in range(1, i):
#         if (j * j) > i:
#             break
#         if dp[i] > dp[i - j * j] + 1:
#             dp[i] = dp[i - j * j] + 1
# print(dp[N])