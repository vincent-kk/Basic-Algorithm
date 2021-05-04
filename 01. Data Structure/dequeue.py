
import sys
import collections

input = sys.stdin.readline

d = collections.deque([])
n = int(input())

for _ in range(n):
    raw = input()[:-1]
    if raw == "pop_front":
        print(d.popleft() if (len(d) > 0) else -1)
    elif raw == "pop_back":
        print(d.pop() if (len(d) > 0) else -1)
    elif raw == "front":
        print(d[0] if (len(d) > 0) else -1)
    elif raw == "back":
        print(d[-1] if (len(d) > 0) else -1)
    elif raw == "size":
        print(len(d))
    elif raw == "empty":
        print(0 if len(d) > 0 else 1)
    else:
        op, arg = raw.split()
        if op == 'push_front':
            d.appendleft(int(arg))
        elif op == 'push_back':
            d.append(int(arg))
