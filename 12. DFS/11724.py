import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
edges = defaultdict(list)
for _ in range(M):
    s, d = map(int, input().split())
    edges[s].append(d)
    edges[d].append(s)

visited = set()
components = 0
for node in range(1, N + 1):
    if node not in visited:
        stack = [node]
        while stack:
            this = stack[-1]
            remove = True
            for near in edges[this]:
                if near not in visited:
                    visited.add(near)
                    stack.append(near)
                    remove = False
                    break
            if remove:
                stack.pop()
        components += 1

print(components)