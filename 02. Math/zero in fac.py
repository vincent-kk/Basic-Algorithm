import sys

input = sys.stdin.readline

n = int(input())

step = 5
result = 0
while n > step:
    for i in range(1, n+1):
        if i == 0:
            continue
        if i % step == 0:
            result += 1
    step *= 5
print(result)
