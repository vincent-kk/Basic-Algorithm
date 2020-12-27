
import sys
import collections

input = sys.stdin.readline

q = collections.deque([])
n = int(input())

for _ in range(n):
    raw = input()[:-1]
    if raw == "pop":
        print(q.popleft() if (len(q) > 0) else -1)
    elif raw == "front":
        print(q[0] if (len(q) > 0) else -1)
    elif raw == "back":
        print(q[-1] if (len(q) > 0) else -1)
    elif raw == "size":
        print(len(q))
    elif raw == "empty":
        print(0 if len(q) > 0 else 1)
    else:
        op, arg = raw.split()
        q.append(int(arg))
