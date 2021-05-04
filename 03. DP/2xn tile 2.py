import sys

input = sys.stdin.readline

n = int(input())
if n < 2:
    print(n)
    exit(0)
d = [0] * (n+1)
d[1] = 1
d[2] = 3

for i in range(n+1):
    if i < 3:
        continue
    d[i] = (d[i-1] % 10007 + (d[i-2]*2) % 10007) % 10007

print(d[n])
