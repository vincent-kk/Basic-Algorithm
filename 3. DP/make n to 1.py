import sys

input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)

for i in range(n+1):
    if i < 2:
        continue
    d[i] = d[i-1] + 1
    if d[i] > d[i//2] and i % 2 == 0:
        d[i] = d[i//2] + 1
    if d[i] > d[i//3] and i % 3 == 0:
        d[i] = d[i//3] + 1
print(d[n])
