import sys

input = sys.stdin.readline

left = []
right = []

init = input()[:-1]
n = int(input())

for ch in init:
    left.append(ch)

for _ in range(n):
    raw = input()[:-1]
    if raw == "L":
        if (len(left) > 0):
            right.append(left.pop())
    elif raw == "D":
        if (len(right) > 0):
            left.append(right.pop())
    elif raw == "B":
        if (len(left) > 0):
            left.pop()
    else:
        op, arg = raw.split()
        left.append(arg)

for ch in left:
    print(ch, end='')
for ch in reversed(right):
    print(ch, end='')