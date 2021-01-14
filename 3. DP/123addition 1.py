import sys

input = sys.stdin.readline


def run(n):
    if n == 0:
        print(1)
        exit(0)
    d = [0] * (n+1)
    d[0] = 1
    d[1] = 1
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2] + (d[i-3] if (i > 2) else 0)
    return d[n]


t = int(input())

for i in range(t):
    n = int(input())
    print(run(n))
