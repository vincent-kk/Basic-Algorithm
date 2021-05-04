from sys import stdin
from functools import lru_cache

input = stdin.readline

MAX_SIZE = 11

dp = [0]*MAX_SIZE
dp[0] = dp[1] = 1
dp[2] = 2
dp[3] = 4


@lru_cache(maxsize=None)
def printAnswer(N: int, K: int):
    if dp[N] < K:
        print(-1)
        return
    i = 0
    while True:
        i += 1
        if dp[N - i] >= K:
            if N-i > 0:
                print(i, end='+')
                printAnswer(N-i, K)
            else:
                print(i, end='')
            break
        K -= dp[N-i]
    return


for i in range(4, MAX_SIZE):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

n, k = map(int, input().split())
printAnswer(n, k)
