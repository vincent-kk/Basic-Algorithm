
import collections
import sys

input = sys.stdin.readline

raw = input()
n, step = raw.split()

queue = collections.deque(range(1, int(n)+1))
result = []

while len(queue) > 0:
    for _ in range(int(step) - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print('<', end='')
for n in result[:-1]:
    print(n, end=', ')
print(result[-1], end='>')
print('')
