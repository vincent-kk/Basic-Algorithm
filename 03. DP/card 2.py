import sys

input = sys.stdin.readline


def run(n, p):
    if n == 0:
        return 0
    d = [-1] * (n+1)
    d[0] = 0
    p = [0] + p
    for i in range(1, n+1):
        for j in range(1, i+1 if (i+1 < len(p))else len(p)):
            if d[i] < 0 or d[i-j]+p[j] < d[i]:
                d[i] = d[i-j]+p[j]
    return d[n]


n = int(input())
p = list(map(int, input().split()))

print(run(n, p))
