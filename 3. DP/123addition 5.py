import sys

input = sys.stdin.readline


def run(n):
    if n == 0:
        return(0)
    d = [[0]*3 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, 4):
            if i-j < 0:
                continue
            elif i-j == 0:
                d[i][j-1] = 1
            else:
                if j == 1:
                    d[i][j-1] = 0 if (i < 1) else (d[i - 1]
                                                   [1] + d[i-1][2]) % 1000000009
                elif j == 2:
                    d[i][j-1] = 0 if (i < 2) else (d[i - 2]
                                                   [0] + d[i-2][2]) % 1000000009
                elif j == 3:
                    d[i][j-1] = 0 if (i < 3) else (d[i - 3]
                                                   [0] + d[i-3][1]) % 1000000009
                else:
                    pass
    return d


t = int(input())
d = run(100001)
for i in range(t):
    n = int(input())
    print(sum(d[n]) % 1000000009)
