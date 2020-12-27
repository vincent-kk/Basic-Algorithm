
import sys
import collections

input = sys.stdin.readline

s = collections.deque([])
n = int(input())

for _ in range(n):
    raw = input()[:-1]
    if raw == "pop":
        print(s.popleft() if (len(s) > 0) else -1)
    elif raw == "front":
        print(s[0] if (len(s) > 0) else -1)
    elif raw == "back":
        print(s[-1] if (len(s) > 0) else -1)
    elif raw == "size":
        print(len(s))
    elif raw == "empty":
        print(0 if len(s) > 0 else 1)
    else:
        op, arg = raw.split()
        s.append(int(arg))
