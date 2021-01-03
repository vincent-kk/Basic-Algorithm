import sys

input = sys.stdin.readline


def run(n):
    if n == 0:
        return(0)
    dp = [[0]*3 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, 4):
            if i-j < 0:
                continue
            elif i-j == 0:
                dp[i][j-1] = 1
            else:
                if j == 1:
                    dp[i][j-1] = 0 if (i < 1) else (dp[i - 1][0])
                elif j == 2:
                    dp[i][j-1] = 0 if (i < 2) else (dp[i - 2][0] + dp[i-2][1])
                elif j == 3:
                    dp[i][j-1] = 0 if (i < 3) else (dp[i - 3]
                                                    [0] + dp[i-3][1]+dp[i-3][2])
                else:
                    pass
    return dp


t = int(input())
d = run(10001)
for i in range(t):
    n = int(input())
    print(sum(d[n]))
